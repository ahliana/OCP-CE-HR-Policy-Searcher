"""Tests for the LegiScan structured policy source."""

import json
from unittest.mock import patch

import pytest

from src.sources import legiscan
from src.sources.legiscan import LegiscanSource


class _FakeResponse:
    def __init__(self, json_data=None, json_exc=None):
        self._json_data = json_data
        self._json_exc = json_exc

    def raise_for_status(self):
        pass

    def json(self):
        if self._json_exc:
            raise self._json_exc
        return self._json_data


class _FakeAsyncClient:
    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = []

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc_info):
        return False

    async def get(self, url, params=None, **kwargs):
        self.calls.append(params)
        if not self._responses:
            raise AssertionError("no more fake responses queued")
        return self._responses.pop(0)


def _search_response(hits: dict) -> _FakeResponse:
    return _FakeResponse(json_data={"searchresult": {**hits, "summary": {}}})


def _bill_response(bill: dict | None) -> _FakeResponse:
    return _FakeResponse(json_data={"bill": bill} if bill is not None else {})


@pytest.fixture(autouse=True)
def _seen_file(tmp_path, monkeypatch):
    monkeypatch.setattr(legiscan, "SEEN_FILE", tmp_path / "legiscan_seen.json")


@pytest.fixture(autouse=True)
def _api_key(monkeypatch):
    monkeypatch.setenv("LEGISCAN_API_KEY", "test-key")


class TestKeyMissing:
    @pytest.mark.asyncio
    async def test_missing_key_returns_empty_and_makes_no_call(self, monkeypatch):
        monkeypatch.delenv("LEGISCAN_API_KEY", raising=False)
        with patch("httpx.AsyncClient") as mock_client_cls:
            result = await LegiscanSource().fetch({})
        assert result == []
        mock_client_cls.assert_not_called()


class TestHappyPath:
    @pytest.mark.asyncio
    async def test_official_url_lifecycle_and_content(self):
        hit = {
            "bill_id": 101,
            "change_hash": "hashA",
            "title": "SB 1",
            "last_action": "Signed by Governor",
        }
        bill = {
            "title": "SB 1 -- Waste Heat Recovery",
            "description": "Requires waste heat recovery at data centers.",
            "state_link": "https://legislature.state.gov/bills/sb1",
            "status_text": "",
        }
        fake_client = _FakeAsyncClient([_search_response({"0": hit}), _bill_response(bill)])
        with patch("httpx.AsyncClient", return_value=fake_client):
            results = await LegiscanSource().fetch(
                {"source_params": {"terms": ["waste heat"]}}
            )

        assert len(results) == 1
        r = results[0]
        assert r.url == "https://legislature.state.gov/bills/sb1"
        assert "legiscan.com" not in r.url
        assert r.lifecycle_stage == "enacted"
        assert r.content and "Waste Heat Recovery" in r.content


class TestMalformed:
    @pytest.mark.asyncio
    async def test_malformed_search_response_returns_empty(self):
        fake_client = _FakeAsyncClient([_FakeResponse(json_exc=json.JSONDecodeError("bad", "", 0))])
        with patch("httpx.AsyncClient", return_value=fake_client):
            results = await LegiscanSource().fetch({"source_params": {"terms": ["x"]}})
        assert results == []


class TestCap:
    @pytest.mark.asyncio
    async def test_max_documents_respected(self):
        hits = {
            "0": {"bill_id": 1, "change_hash": "h1", "title": "A", "last_action": ""},
            "1": {"bill_id": 2, "change_hash": "h2", "title": "B", "last_action": ""},
        }
        bill = {
            "title": "Bill",
            "description": "desc",
            "state_link": "https://legislature.state.gov/bills/x",
            "status_text": "",
        }
        fake_client = _FakeAsyncClient(
            [_search_response(hits), _bill_response(bill), _bill_response(bill)]
        )
        with patch("httpx.AsyncClient", return_value=fake_client):
            results = await LegiscanSource().fetch(
                {"source_params": {"terms": ["x"], "max_documents": 1}}
            )
        assert len(results) == 1


class TestNoStateLinkSkipped:
    @pytest.mark.asyncio
    async def test_bill_without_state_link_is_skipped(self):
        hit = {"bill_id": 5, "change_hash": "h5", "title": "C", "last_action": ""}
        bill = {"title": "C", "description": "desc", "status_text": ""}  # no state_link
        fake_client = _FakeAsyncClient([_search_response({"0": hit}), _bill_response(bill)])
        with patch("httpx.AsyncClient", return_value=fake_client):
            results = await LegiscanSource().fetch({"source_params": {"terms": ["x"]}})
        assert results == []


class TestUnchangedSkipped:
    @pytest.mark.asyncio
    async def test_unchanged_change_hash_skips_getbill_call(self, tmp_path):
        seen_file = tmp_path / "legiscan_seen.json"
        seen_file.write_text(json.dumps({"9": "same-hash"}), encoding="utf-8")
        legiscan.SEEN_FILE = seen_file

        hit = {"bill_id": 9, "change_hash": "same-hash", "title": "D", "last_action": ""}
        fake_client = _FakeAsyncClient([_search_response({"0": hit})])
        with patch("httpx.AsyncClient", return_value=fake_client):
            results = await LegiscanSource().fetch({"source_params": {"terms": ["x"]}})

        assert results == []
        assert len(fake_client.calls) == 1  # only the search call, getBill never called


class TestApiCallBudget:
    @pytest.mark.asyncio
    async def test_budget_stops_cleanly(self):
        hit = {"bill_id": 11, "change_hash": "h11", "title": "E", "last_action": ""}
        fake_client = _FakeAsyncClient([_search_response({"0": hit})])
        with patch("httpx.AsyncClient", return_value=fake_client):
            results = await LegiscanSource().fetch(
                {"source_params": {"terms": ["term1", "term2"], "max_api_calls": 1}}
            )
        assert results == []
        assert len(fake_client.calls) == 1
