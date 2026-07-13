"""Tests for ScanManager domain-default handling."""

from unittest.mock import MagicMock

import pytest

from src.orchestration.scan_manager import ScanManager


def _settings_with_min_score(value: float) -> MagicMock:
    settings = MagicMock()
    settings.analysis.min_keyword_score = value
    return settings


class TestKeywordScoreDefault:
    """settings.analysis.min_keyword_score must reach the keyword gate.

    Historically the settings value was loaded but never read: domains
    without an explicit min_keyword_score silently fell back to the
    stricter keywords.yaml threshold (5.0) instead of the documented 3.0.
    """

    def test_domain_without_score_gets_settings_default(self):
        domain = {"id": "d1", "base_url": "https://a.gov"}
        result = ScanManager._with_keyword_score_default(
            domain, _settings_with_min_score(3.0)
        )
        assert result["min_keyword_score"] == 3.0

    def test_domain_with_explicit_score_keeps_it(self):
        domain = {"id": "d1", "base_url": "https://a.gov", "min_keyword_score": 2.0}
        result = ScanManager._with_keyword_score_default(
            domain, _settings_with_min_score(3.0)
        )
        assert result["min_keyword_score"] == 2.0

    def test_original_domain_dict_not_mutated(self):
        domain = {"id": "d1", "base_url": "https://a.gov"}
        ScanManager._with_keyword_score_default(domain, _settings_with_min_score(3.0))
        assert "min_keyword_score" not in domain

    def test_deep_scan_default_wins_over_settings(self):
        # _with_deep_scan_defaults runs first (sets 2.0); settings must not override
        domain = ScanManager._with_deep_scan_defaults(
            {"id": "d1", "base_url": "https://a.gov"}
        )
        result = ScanManager._with_keyword_score_default(
            domain, _settings_with_min_score(3.0)
        )
        assert result["min_keyword_score"] == 2.0


class TestDomainChannel:
    """_domain_channel() classifies a domain by its source_type."""

    def test_absent_source_type_is_crawl(self):
        domain = {"id": "d1", "base_url": "https://a.gov"}
        assert ScanManager._domain_channel(domain) == "crawl"

    def test_explicit_crawl_source_type_is_crawl(self):
        domain = {"id": "d1", "source_type": "crawl"}
        assert ScanManager._domain_channel(domain) == "crawl"

    def test_eurlex_nim_is_transposition(self):
        domain = {"id": "d1", "source_type": "eurlex_nim"}
        assert ScanManager._domain_channel(domain) == "transposition"

    def test_other_source_type_is_law_apis(self):
        domain = {"id": "d1", "source_type": "riksdagen"}
        assert ScanManager._domain_channel(domain) == "law_apis"


def _manager_with_domains(domains: list[dict]) -> ScanManager:
    config = MagicMock()
    config.get_enabled_domains.return_value = domains
    return ScanManager(config=config, broadcaster=MagicMock())


class TestStartScanChannels:
    """start_scan() filters domains by channel and records the choice.

    dry_run=True is used throughout so start_scan returns synchronously
    (job already COMPLETED) without spawning the background scan task.
    """

    @pytest.mark.asyncio
    async def test_default_channel_is_crawl_only(self):
        domains = [
            {"id": "crawl1", "name": "Crawl 1"},
            {"id": "api1", "name": "Api 1", "source_type": "riksdagen"},
        ]
        manager = _manager_with_domains(domains)
        job = await manager.start_scan(dry_run=True)
        assert job.domain_count == 1
        assert [dp.domain_id for dp in job.progress.domains] == ["crawl1"]
        assert job.options["channels"] == ["crawl"]

    @pytest.mark.asyncio
    async def test_law_apis_channel_selects_only_source_type_domains(self):
        domains = [
            {"id": "crawl1", "name": "Crawl 1"},
            {"id": "api1", "name": "Api 1", "source_type": "riksdagen"},
            {"id": "api2", "name": "Api 2", "source_type": "govinfo"},
            {"id": "eurlex1", "name": "EurLex", "source_type": "eurlex_nim"},
        ]
        manager = _manager_with_domains(domains)
        job = await manager.start_scan(dry_run=True, channels=["law_apis"])
        assert job.domain_count == 2
        assert {dp.domain_id for dp in job.progress.domains} == {"api1", "api2"}

    @pytest.mark.asyncio
    async def test_transposition_channel_selects_eurlex_nim(self):
        domains = [
            {"id": "crawl1", "name": "Crawl 1"},
            {"id": "eurlex1", "name": "EurLex", "source_type": "eurlex_nim"},
        ]
        manager = _manager_with_domains(domains)
        job = await manager.start_scan(dry_run=True, channels=["transposition"])
        assert job.domain_count == 1
        assert job.progress.domains[0].domain_id == "eurlex1"

    @pytest.mark.asyncio
    async def test_options_records_requested_channels(self):
        manager = _manager_with_domains([])
        job = await manager.start_scan(dry_run=True, channels=["crawl", "law_apis"])
        assert job.options["channels"] == ["crawl", "law_apis"]

    @pytest.mark.asyncio
    async def test_news_only_channel_yields_zero_domains(self):
        domains = [
            {"id": "crawl1", "name": "Crawl 1"},
            {"id": "api1", "name": "Api 1", "source_type": "riksdagen"},
        ]
        manager = _manager_with_domains(domains)
        job = await manager.start_scan(dry_run=True, channels=["news"])
        assert job.domain_count == 0
        assert job.options["channels"] == ["news"]
