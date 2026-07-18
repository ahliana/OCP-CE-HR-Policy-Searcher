"""World-map coverage — read-only aggregate of where PolicyPulse has looked.

``GET /api/coverage`` answers "which countries have tracked sources or found
policies, and what sits above the country level" in one shot, so the map can
color countries before anyone types a word. Nothing is precomputed or stored:
every count is derived at request time from the canonical jurisdiction
registry (``src/core/jurisdictions.py``) applied to the existing policy data
and domain configs. Adding a source or finding a policy changes the response
with no schema change and no backfill.

Attribution rules (uniform for policies and sources):
- ``resolve_text`` / registry slug -> a ``Jurisdiction``.
- ``country_of`` rolls ``country``/``us_state``/``subnational`` up to a
  country, keyed by ``iso_numeric`` (the world-atlas join key).
- Jurisdictions with no map shape become ``supranational`` (off-map) entries
  keyed by slug: ``supranational``/``group`` kinds (the EU, a future ``global``
  IGO bucket) AND countries the registry carries without an ``iso_numeric``
  (e.g. Kosovo). "EU" is never hardcoded — whatever the registry returns is
  handled, and null-iso countries never land in ``countries`` under a None key.
- Source counts attribute a domain to a country once per country, however many
  of its ``region`` tags roll up there. Off-map entries carry a ``sources``
  count too, but only for null-iso countries; supranational/group entries stay
  policy-driven (a broad ``region`` tag like ``nordic`` is not a chip).
"""

from fastapi import APIRouter, Depends

from ..deps import get_config, get_policy_store
from ...core import jurisdictions
from ...core.config import ConfigLoader
from ...storage.store import PolicyStore

router = APIRouter(prefix="/api", tags=["coverage"])

_MAX_TOP_POLICIES = 3


def _top_policy_names(policies: list[dict]) -> list[str]:
    """Up to three policy names for a bucket, highest relevance first."""
    ranked = sorted(
        policies,
        key=lambda p: (-(p.get("relevance_score") or 0), p.get("policy_name") or ""),
    )
    return [p.get("policy_name") or "" for p in ranked[:_MAX_TOP_POLICIES]]


def compute_coverage(policies: list[dict], domains: list[dict]) -> dict:
    """Aggregate policies and domain sources into per-jurisdiction coverage.

    Pure: takes already-loaded policy dicts and domain dicts, returns the
    response body plus a ``diagnostics`` block. The route strips diagnostics
    off ``/api/coverage`` and exposes them on ``/api/coverage/unresolved``.
    """
    # country iso_numeric -> aggregate; slug -> supranational aggregate
    country_policies: dict[str, list[dict]] = {}
    country_names: dict[str, str] = {}
    country_sources: dict[str, set[str]] = {}
    # "off-map" = jurisdictions with no choropleth shape: supranational/group
    # (the EU, a future global IGO bucket) AND countries the registry carries
    # without an iso_numeric (e.g. Kosovo, code XK). All are keyed by slug and
    # rendered as chips beside the map, never as a country fill — and never
    # under a None iso key, where null-iso territories would silently collide.
    offmap_policies: dict[str, list[dict]] = {}
    offmap_names: dict[str, str] = {}
    offmap_sources: dict[str, set[str]] = {}
    unresolved_policies: list[str] = []
    unresolved_slugs: set[str] = set()

    for policy in policies:
        raw = policy.get("jurisdiction")
        jur = jurisdictions.resolve_text(raw)
        if jur is None:
            unresolved_policies.append(raw)
            continue
        country = jurisdictions.country_of(jur)
        if country is not None and country.iso_numeric:
            country_names.setdefault(country.iso_numeric, country.name)
            country_policies.setdefault(country.iso_numeric, []).append(policy)
        elif country is not None:
            # A real country the registry has no iso_numeric for (Kosovo).
            offmap_names.setdefault(country.slug, country.name)
            offmap_policies.setdefault(country.slug, []).append(policy)
        elif jur.kind in ("supranational", "group"):
            offmap_names.setdefault(jur.slug, jur.name)
            offmap_policies.setdefault(jur.slug, []).append(policy)
        else:
            # Resolved but neither a country nor a supra/group kind — should
            # not happen with the current registry, but never silently drop it.
            unresolved_policies.append(raw)

    for domain in domains:
        did = domain.get("id")
        for slug in (domain.get("region") or []):
            jur = jurisdictions.get(slug)
            if jur is None:
                unresolved_slugs.add(slug)
                continue
            country = jurisdictions.country_of(jur)
            if country is not None and country.iso_numeric:
                country_names.setdefault(country.iso_numeric, country.name)
                country_sources.setdefault(country.iso_numeric, set()).add(did)
            elif country is not None:
                # Null-iso country source (Kosovo) -> off-map, keyed by slug,
                # so a country tracked-but-with-no-shape still shows coverage.
                offmap_names.setdefault(country.slug, country.name)
                offmap_sources.setdefault(country.slug, set()).add(did)
            # Group/supranational region tags (eu, nordic, apac, ...) do not
            # attribute a source anywhere; totals.sources still counts the
            # domain. Those off-map entries stay policy-driven.

    countries = [
        {
            "name": country_names[iso],
            "iso_numeric": iso,
            "sources": len(country_sources.get(iso, set())),
            "policies": len(country_policies.get(iso, [])),
            "top_policy_names": _top_policy_names(country_policies.get(iso, [])),
        }
        for iso in (country_names.keys() | country_sources.keys())
    ]
    countries.sort(key=lambda c: (-c["policies"], c["name"]))

    supranational = [
        {
            "name": offmap_names[slug],
            "slug": slug,
            "sources": len(offmap_sources.get(slug, set())),
            "policies": len(offmap_policies.get(slug, [])),
            "top_policy_names": _top_policy_names(offmap_policies.get(slug, [])),
        }
        for slug in (offmap_names.keys() | offmap_sources.keys())
    ]
    supranational.sort(key=lambda s: (-s["policies"], -s["sources"], s["name"]))

    return {
        "countries": countries,
        "supranational": supranational,
        "totals": {"sources": len(domains), "policies": len(policies)},
        "diagnostics": {
            "unresolved_policies": unresolved_policies,
            "unresolved_region_slugs": sorted(unresolved_slugs),
        },
    }


@router.get("/coverage")
def get_coverage(
    store: PolicyStore = Depends(get_policy_store),
    config: ConfigLoader = Depends(get_config),
):
    """Coverage aggregate for the world map: countries, supranational, totals."""
    result = compute_coverage(store.get_all(), config.get_enabled_domains("all"))
    return {k: result[k] for k in ("countries", "supranational", "totals")}


@router.get("/coverage/unresolved")
def get_coverage_unresolved(
    store: PolicyStore = Depends(get_policy_store),
    config: ConfigLoader = Depends(get_config),
):
    """Jurisdiction strings and region slugs the registry could not resolve.

    Surfaces a newly added source that forgot its registry row (or an LLM
    jurisdiction string with no alias) instead of it silently reading as
    "untracked". Both lists should be empty; the domain-slug guardrail test
    keeps the slug list empty in CI.
    """
    result = compute_coverage(store.get_all(), config.get_enabled_domains("all"))
    return result["diagnostics"]
