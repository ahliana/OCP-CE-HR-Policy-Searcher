"""Tests for GET /api/coverage (world-map coverage endpoint).

Coverage is computed at read time from the merged jurisdiction registry:
policies (data/policies.json) resolve via ``resolve_text`` and roll up to a
country via ``country_of``; policies that resolve above the country level land
in the ``supranational`` array. Source counts come from the domain configs'
``region`` tags via the same rollup.

These tests pin the same real jurisdiction strings that
``test_jurisdictions.py`` pins, and the invariant that every policy lands
somewhere: ``sum(country policies) + sum(supranational policies) == total``.
"""

import pytest
from fastapi.testclient import TestClient

from src.core import jurisdictions
from src.api.routes.coverage import compute_coverage


@pytest.fixture(autouse=True)
def _reset_registry_caches():
    """Force a fresh registry load and clear the miss counter between tests."""
    jurisdictions._by_slug = None
    jurisdictions._alias_index = None
    jurisdictions._alias_by_len = None
    jurisdictions._unresolved.clear()
    yield


def _pol(jurisdiction, name, score=5):
    """Minimal policy dict shaped like data/policies.json rows."""
    return {
        "jurisdiction": jurisdiction,
        "policy_name": name,
        "relevance_score": score,
        "url": f"https://example.gov/{name.replace(' ', '-').lower()}",
    }


def _iso(text):
    return jurisdictions.resolve_text(text).iso_numeric


def _by_iso(countries, iso):
    return next((c for c in countries if c["iso_numeric"] == iso), None)


def _by_slug(supra, slug):
    return next((s for s in supra if s["slug"] == slug), None)


class TestPolicyAttribution:
    """The real jurisdiction strings resolve to the right map bucket."""

    def test_sweden_eu_string_lands_on_sweden_not_eu(self):
        # The registry attributes "Sweden (EU)" to Sweden, not the EU bucket —
        # the exact case the design proposal calls out.
        cov = compute_coverage([_pol("Sweden (EU)", "SE heat rule")], [])
        swe = _by_iso(cov["countries"], _iso("Sweden"))
        assert swe is not None and swe["policies"] == 1
        assert cov["supranational"] == []

    def test_european_union_string_lands_supranational(self):
        cov = compute_coverage([_pol("European Union", "EED Article 26")], [])
        assert cov["countries"] == []
        eu = _by_slug(cov["supranational"], "eu")
        assert eu is not None and eu["policies"] == 1
        assert "iso_numeric" not in eu  # supranational has no country shape

    def test_three_us_spellings_collapse_to_one_country(self):
        cov = compute_coverage(
            [
                _pol("US", "a"),
                _pol("United States", "b"),
                _pol("United States (Federal)", "c"),
            ],
            [],
        )
        us = _by_iso(cov["countries"], _iso("US"))
        assert us is not None and us["policies"] == 3
        assert len(cov["countries"]) == 1

    def test_us_state_rolls_up_to_country(self):
        cov = compute_coverage(
            [_pol("Minnesota, USA", "MN"), _pol("California, USA", "CA")], []
        )
        us = _by_iso(cov["countries"], _iso("US"))
        assert us is not None and us["policies"] == 2

    def test_region_country_form_rolls_up(self):
        # "Wallonia, Belgium" -> Belgium; "Germany (Federal)" -> Germany.
        cov = compute_coverage(
            [_pol("Wallonia, Belgium", "w"), _pol("Germany (Federal)", "g")], []
        )
        assert _by_iso(cov["countries"], _iso("Belgium"))["policies"] == 1
        assert _by_iso(cov["countries"], _iso("Germany"))["policies"] == 1


class TestSumInvariant:
    """Every policy lands somewhere: country + supranational == total."""

    def test_sum_equals_total_over_mixed_strings(self):
        policies = [
            _pol("Sweden (EU)", "1"),
            _pol("Sweden", "2"),
            _pol("Denmark", "3"),
            _pol("Minnesota, USA", "4"),
            _pol("US", "5"),
            _pol("United States (Federal)", "6"),
            _pol("European Union", "7"),
            _pol("Wallonia, Belgium", "8"),
            _pol("Germany (Federal)", "9"),
        ]
        cov = compute_coverage(policies, [])
        country_total = sum(c["policies"] for c in cov["countries"])
        supra_total = sum(s["policies"] for s in cov["supranational"])
        assert country_total + supra_total == len(policies)
        assert cov["totals"]["policies"] == len(policies)


class TestTopPolicyNames:
    def test_top_names_capped_at_three_and_ranked_by_score(self):
        policies = [
            _pol("Sweden", "low", score=1),
            _pol("Sweden", "high", score=9),
            _pol("Sweden", "mid", score=5),
            _pol("Sweden", "lowest", score=0),
        ]
        cov = compute_coverage(policies, [])
        swe = _by_iso(cov["countries"], _iso("Sweden"))
        assert swe["policies"] == 4
        assert swe["top_policy_names"] == ["high", "mid", "low"]


class TestSourceAttribution:
    def _domains(self):
        return [
            {"id": "d1", "region": ["germany", "bayern"]},   # both -> Germany
            {"id": "d2", "region": ["us", "california"]},     # both -> US
            {"id": "d3", "region": ["eu"]},                   # supranational, no country
            {"id": "d4", "region": ["france"]},
            {"id": "d5", "region": []},                       # counts only in totals
        ]

    def test_domain_counted_once_per_country_despite_multiple_tags(self):
        cov = compute_coverage([], self._domains())
        assert _by_iso(cov["countries"], _iso("Germany"))["sources"] == 1
        assert _by_iso(cov["countries"], _iso("US"))["sources"] == 1
        assert _by_iso(cov["countries"], _iso("France"))["sources"] == 1

    def test_eu_only_source_does_not_create_a_country(self):
        cov = compute_coverage([], self._domains())
        # No country entry is created solely from an EU tag.
        assert all(c["iso_numeric"] is not None for c in cov["countries"])
        # EU has no policies here, so it is not a supranational entry either.
        assert cov["supranational"] == []

    def test_totals_sources_counts_every_domain(self):
        cov = compute_coverage([], self._domains())
        assert cov["totals"]["sources"] == 5

    def test_country_appears_with_sources_but_no_policies(self):
        cov = compute_coverage([], [{"id": "d1", "region": ["denmark"]}])
        dk = _by_iso(cov["countries"], _iso("Denmark"))
        assert dk is not None and dk["sources"] == 1 and dk["policies"] == 0


class TestDiagnostics:
    def test_unresolved_policy_string_is_reported(self):
        cov = compute_coverage([_pol("Kingdom of Atlantis", "x")], [])
        assert "Kingdom of Atlantis" in cov["diagnostics"]["unresolved_policies"]

    def test_unresolved_region_slug_is_reported(self):
        cov = compute_coverage([], [{"id": "d", "region": ["narnia"]}])
        assert "narnia" in cov["diagnostics"]["unresolved_region_slugs"]

    def test_clean_data_has_no_unresolved(self):
        cov = compute_coverage(
            [_pol("Sweden", "s")], [{"id": "d", "region": ["denmark"]}]
        )
        assert cov["diagnostics"]["unresolved_policies"] == []
        assert cov["diagnostics"]["unresolved_region_slugs"] == []


# --- Route wiring (registration + response shape) ---

class _FakeStore:
    def __init__(self, policies):
        self._policies = policies

    def get_all(self):
        return list(self._policies)


class _FakeConfig:
    def __init__(self, domains):
        self._domains = domains

    def get_enabled_domains(self, group="all"):
        return list(self._domains)


@pytest.fixture
def client(monkeypatch):
    monkeypatch.delenv("ADMIN_TOKEN", raising=False)
    from src.api.app import app
    from src.api import deps

    store = _FakeStore([_pol("Sweden (EU)", "s"), _pol("European Union", "e")])
    config = _FakeConfig([{"id": "d1", "region": ["sweden"]}])
    app.dependency_overrides[deps.get_policy_store] = lambda: store
    app.dependency_overrides[deps.get_config] = lambda: config
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


class TestRouteWiring:
    def test_coverage_endpoint_shape(self, client):
        resp = client.get("/api/coverage")
        assert resp.status_code == 200
        body = resp.json()
        assert set(body) == {"countries", "supranational", "totals"}
        assert body["totals"] == {"sources": 1, "policies": 2}
        swe = _by_iso(body["countries"], _iso("Sweden"))
        assert swe["policies"] == 1 and swe["sources"] == 1
        assert set(swe) == {"name", "iso_numeric", "sources", "policies",
                            "top_policy_names"}
        eu = _by_slug(body["supranational"], "eu")
        assert eu["policies"] == 1
        assert set(eu) == {"name", "slug", "policies", "top_policy_names"}

    def test_unresolved_endpoint(self, client):
        resp = client.get("/api/coverage/unresolved")
        assert resp.status_code == 200
        body = resp.json()
        assert body["unresolved_policies"] == []
        assert body["unresolved_region_slugs"] == []
