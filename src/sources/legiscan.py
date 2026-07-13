"""LegiScan structured policy source — US state legislation.

Searches LegiScan's getSearchRaw op for candidate bills, then resolves
each hit's official state legislature URL via getBill (LegiScan itself is
only an aggregator; its own bill pages are never used as the citation of
record). Full bill text is deliberately never fetched (getBillText) to
conserve the API quota — screening/analysis works off title + description
+ last action instead. Disabled entirely (returns []) until
LEGISCAN_API_KEY is set.
"""

import json
import logging
import os
from pathlib import Path

import httpx

from ..core.models import CrawlResult, PageStatus
from . import register_source
from ._common import TIMEOUT_SECONDS, USER_AGENT
from .base import PolicySource

logger = logging.getLogger(__name__)

API_KEY_ENV = "LEGISCAN_API_KEY"
BASE_URL = "https://api.legiscan.com/"
DEFAULT_TERMS = ["waste heat", "district heating", "data center energy"]
DEFAULT_MAX_DOCUMENTS = 25
DEFAULT_MAX_API_CALLS = 40

# Cache of bill_id -> change_hash so unchanged bills are skipped on rerun.
SEEN_FILE = Path("data") / "legiscan_seen.json"


def _load_seen() -> dict:
    if not SEEN_FILE.exists():
        return {}
    try:
        return json.loads(SEEN_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        logger.warning("Failed to read %s: %s", SEEN_FILE, e)
        return {}


def _save_seen(seen: dict) -> None:
    SEEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = SEEN_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(seen, indent=2), encoding="utf-8")
    tmp.replace(SEEN_FILE)


def _lifecycle_from_bill(bill: dict, last_action: str) -> str:
    text = " ".join(
        str(part) for part in (bill.get("status_text", ""), last_action) if part
    ).lower()
    if any(k in text for k in ("signed", "enacted", "chaptered")):
        return "enacted"
    if "committee" in text:
        return "in_committee"
    if "passed" in text:
        return "passed"
    if "introduced" in text:
        return "proposed"
    return "proposed"


class _CallBudget:
    """Tracks API calls against a per-fetch cap; stops cleanly once spent."""

    def __init__(self, max_calls: int):
        self.max_calls = max_calls
        self.calls = 0

    def spend(self) -> None:
        self.calls += 1

    @property
    def exhausted(self) -> bool:
        return self.calls >= self.max_calls


@register_source
class LegiscanSource(PolicySource):
    """Fetches US state bills from api.legiscan.com, citing the official state link."""

    id = "legiscan"

    async def fetch(self, domain: dict) -> list[CrawlResult]:
        api_key = os.environ.get(API_KEY_ENV)
        if not api_key:
            logger.info("source disabled: %s not set", API_KEY_ENV)
            return []

        params = domain.get("source_params", {})
        terms = params.get("terms") or DEFAULT_TERMS
        max_documents = params.get("max_documents", DEFAULT_MAX_DOCUMENTS)
        max_api_calls = params.get("max_api_calls", DEFAULT_MAX_API_CALLS)

        seen = _load_seen()
        results: list[CrawlResult] = []
        budget = _CallBudget(max_api_calls)

        async with httpx.AsyncClient(
            timeout=TIMEOUT_SECONDS, headers={"User-Agent": USER_AGENT}
        ) as client:
            for term in terms:
                if len(results) >= max_documents or budget.exhausted:
                    break
                for bill_id, hit in await self._search(client, term, api_key, budget):
                    if len(results) >= max_documents or budget.exhausted:
                        break
                    result = await self._to_crawl_result(client, api_key, bill_id, hit, seen, budget)
                    if result:
                        results.append(result)

        _save_seen(seen)
        return results

    async def _search(
        self, client: httpx.AsyncClient, term: str, api_key: str, budget: "_CallBudget"
    ) -> list[tuple[int, dict]]:
        try:
            resp = await client.get(
                BASE_URL,
                params={"key": api_key, "op": "getSearchRaw", "state": "ALL", "query": term},
            )
            budget.spend()
            resp.raise_for_status()
            data = resp.json()
        except (httpx.HTTPError, ValueError) as e:
            logger.warning("LegiScan search failed for term %r: %s", term, e)
            return []

        searchresult = data.get("searchresult") if isinstance(data, dict) else None
        if not isinstance(searchresult, dict):
            return []

        hits = []
        for key, hit in searchresult.items():
            if key == "summary" or not isinstance(hit, dict):
                continue
            bill_id = hit.get("bill_id")
            if bill_id is not None:
                hits.append((bill_id, hit))
        return hits

    async def _to_crawl_result(
        self,
        client: httpx.AsyncClient,
        api_key: str,
        bill_id: int,
        hit: dict,
        seen: dict,
        budget: "_CallBudget",
    ) -> CrawlResult | None:
        change_hash = hit.get("change_hash")
        if seen.get(str(bill_id)) == change_hash:
            return None  # unchanged since last run

        try:
            resp = await client.get(
                BASE_URL, params={"key": api_key, "op": "getBill", "id": bill_id}
            )
            budget.spend()
            resp.raise_for_status()
            data = resp.json()
        except (httpx.HTTPError, ValueError) as e:
            logger.warning("LegiScan getBill failed for %s: %s", bill_id, e)
            return None

        bill = data.get("bill") if isinstance(data, dict) else None
        if not isinstance(bill, dict):
            return None
        state_link = bill.get("state_link")
        if not state_link:
            return None  # no official URL to cite -- skip

        title = bill.get("title") or hit.get("title", "")
        description = bill.get("description", "")
        last_action = hit.get("last_action", "")
        content = " ".join(part for part in (title, description, last_action) if part)

        seen[str(bill_id)] = change_hash
        return CrawlResult(
            url=state_link,
            status=PageStatus.SUCCESS,
            content=content,
            title=title,
            lifecycle_stage=_lifecycle_from_bill(bill, last_action),
        )
