"""Tests for KeywordMatcher — matching, scoring, URL bonuses, and relevance."""

import pytest

from src.core.keywords import KeywordMatcher


def _make_config(**overrides):
    """Create a minimal keyword config for testing."""
    config = {
        "keywords": {
            "heat_recovery": {
                "weight": 3.0,
                "terms": {
                    "en": ["heat recovery", "waste heat", "heat reuse"],
                    "de": ["Abwärme", "Wärmerückgewinnung"],
                },
            },
            "data_center": {
                "weight": 2.0,
                "terms": {
                    "en": ["data center", "data centre", "server farm"],
                },
            },
            "energy_policy": {
                "weight": 1.5,
                "terms": {
                    "en": ["energy efficiency", "energy law"],
                },
            },
        },
        "thresholds": {
            "minimum_keyword_score": 5.0,
            "minimum_matches": 2,
        },
        "exclusions": ["job posting", "career opportunity"],
        "stricter_requirements": {},
    }
    config.update(overrides)
    return config


@pytest.fixture
def matcher():
    return KeywordMatcher(_make_config())


class TestKeywordMatch:
    def test_matches_english_terms(self, matcher):
        text = "This policy requires heat recovery from data center operations."
        result = matcher.match(text)
        assert result.score > 0
        assert len(result.matches) >= 2
        categories = set(result.categories_matched)
        assert "heat_recovery" in categories
        assert "data_center" in categories

    def test_matches_german_compound_words(self, matcher):
        text = "Die Abwärme von Rechenzentren muss genutzt werden."
        result = matcher.match(text)
        assert any(m.term == "Abwärme" for m in result.matches)

    def test_no_match_irrelevant_text(self, matcher):
        text = "The weather today is sunny and warm."
        result = matcher.match(text)
        assert result.score == 0
        assert len(result.matches) == 0

    def test_exclusion_returns_zero_score(self, matcher):
        text = "Job posting for data center heat recovery engineer."
        result = matcher.match(text)
        assert result.is_excluded
        assert result.score == 0

    def test_score_reflects_weights(self, matcher):
        text = "heat recovery"  # weight 3.0
        result = matcher.match(text)
        assert result.score == 3.0

    def test_multiple_categories_add_up(self, matcher):
        text = "data center heat recovery energy efficiency"
        result = matcher.match(text)
        assert result.score >= 6.5  # 3.0 + 2.0 + 1.5


class TestUrlBonus:
    def test_gov_tld_bonus(self, matcher):
        bonus = matcher.url_bonus("https://www.energy.gov/policy")
        assert bonus >= 1.0

    def test_gov_uk_tld_bonus(self, matcher):
        bonus = matcher.url_bonus("https://www.legislation.gov.uk/act/2024")
        assert bonus >= 1.0

    def test_bill_path_bonus(self, matcher):
        bonus = matcher.url_bonus("https://example.com/legislation/act123")
        assert bonus >= 1.5

    def test_no_bonus_for_regular_url(self, matcher):
        bonus = matcher.url_bonus("https://example.com/about")
        assert bonus == 0.0

    def test_bill_number_bonus(self, matcher):
        bonus = matcher.url_bonus("https://example.com/bills/HB123")
        # bill path + bill number bonuses
        assert bonus >= 1.0


class TestIsRelevant:
    def test_relevant_when_above_threshold(self, matcher):
        text = "data center heat recovery energy efficiency"
        result = matcher.match(text)
        assert matcher.is_relevant(result)

    def test_not_relevant_low_score(self, matcher):
        text = "heat recovery"  # Only one match category
        result = matcher.match(text)
        assert not matcher.is_relevant(result)

    def test_url_bonus_can_push_over_threshold(self, matcher):
        text = "heat recovery energy efficiency"  # score = 4.5 (below 5.0)
        result = matcher.match(text)
        # Without URL bonus: not enough score
        # With .gov bonus: 4.5 + 1.0 = 5.5 (above threshold)
        assert matcher.is_relevant(result, url="https://www.energy.gov/p")

    def test_min_score_override(self, matcher):
        text = "heat recovery"  # score 3.0, 1 match
        result = matcher.match(text)
        assert not matcher.is_relevant(result, min_score_override=2.0)  # only 1 match < min_matches

    def test_required_combinations(self):
        config = _make_config(
            stricter_requirements={
                "required_combinations": {
                    "enabled": True,
                    "combinations": [
                        {"primary": "heat_recovery", "secondary": "data_center"},
                    ],
                    "min_matches_per_category": 1,
                },
            },
        )
        matcher = KeywordMatcher(config)

        # Has both categories
        text = "data center waste heat reuse"
        result = matcher.match(text)
        assert matcher.is_relevant(result)

        # Missing one category
        text2 = "energy efficiency energy law"
        result2 = matcher.match(text2)
        assert not matcher.is_relevant(result2)


class TestBoostAndPenalty:
    def test_boost_increases_score(self):
        config = _make_config(
            stricter_requirements={
                "boost_keywords": {
                    "enabled": True,
                    "terms": ["mandatory"],
                    "boost_amount": 3.0,
                },
            },
        )
        matcher = KeywordMatcher(config)
        text = "mandatory heat recovery from data center"
        result = matcher.match(text)
        # Base score + 3.0 boost
        assert result.score >= 8.0

    def test_penalty_decreases_score(self):
        config = _make_config(
            stricter_requirements={
                "penalty_keywords": {
                    "enabled": True,
                    "terms": ["voluntary"],
                    "penalty_amount": 5.0,
                },
            },
        )
        matcher = KeywordMatcher(config)
        text = "voluntary heat recovery from data center"
        result = matcher.match(text)
        # Base score - 5.0 penalty
        assert result.score < 5.0


class TestNearMiss:
    def test_near_miss_at_sixty_percent(self, matcher):
        text = "heat recovery"  # score 3.0, threshold 5.0, 60% = 3.0
        result = matcher.match(text)
        assert matcher.check_near_miss(result)

    def test_not_near_miss_too_low(self, matcher):
        text = "weather forecast"
        result = matcher.match(text)
        assert not matcher.check_near_miss(result)

    def test_not_near_miss_when_passes(self, matcher):
        text = "data center heat recovery energy efficiency"
        result = matcher.match(text)
        matcher.is_relevant(result)
        assert not matcher.check_near_miss(result)
