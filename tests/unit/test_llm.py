"""Tests for LLM helpers and ClaudeClient.to_policy()."""

from datetime import date

import pytest

from src.core.llm import (
    _extract_json, _coerce_types, ClaudeClient,
    SCREENING_PROMPT, ANALYSIS_PROMPT,
)
from src.core.models import PolicyAnalysis, PolicyType, CostInfo


# --- _extract_json ---

class TestExtractJson:
    def test_raw_json(self):
        text = '{"relevant": true, "confidence": 8}'
        result = _extract_json(text)
        assert '"relevant": true' in result

    def test_json_in_code_block(self):
        text = 'Here is the result:\n```json\n{"relevant": true}\n```'
        result = _extract_json(text)
        assert result == '{"relevant": true}'

    def test_json_in_generic_code_block(self):
        text = '```\n{"relevant": false}\n```'
        result = _extract_json(text)
        assert result == '{"relevant": false}'

    def test_json_with_surrounding_text(self):
        text = 'The analysis shows: {"is_relevant": true, "score": 9} end.'
        result = _extract_json(text)
        assert '"is_relevant": true' in result

    def test_nested_braces(self):
        text = '{"outer": {"inner": 1}}'
        result = _extract_json(text)
        assert result == '{"outer": {"inner": 1}}'


# --- _coerce_types ---

class TestCoerceTypes:
    def test_string_true_to_bool(self):
        result = _coerce_types({"is_relevant": "true"})
        assert result["is_relevant"] is True

    def test_string_yes_to_bool(self):
        result = _coerce_types({"is_relevant": "yes"})
        assert result["is_relevant"] is True

    def test_string_ja_to_bool(self):
        result = _coerce_types({"is_relevant": "ja"})
        assert result["is_relevant"] is True

    def test_string_false_to_bool(self):
        result = _coerce_types({"is_relevant": "false"})
        assert result["is_relevant"] is False

    def test_int_to_bool(self):
        result = _coerce_types({"is_relevant": 1})
        assert result["is_relevant"] is True

    def test_float_score_to_int(self):
        result = _coerce_types({"relevance_score": 7.5})
        assert result["relevance_score"] == 7

    def test_string_score_to_int(self):
        result = _coerce_types({"relevance_score": "8/10"})
        assert result["relevance_score"] == 8

    def test_score_clamped_to_10(self):
        result = _coerce_types({"relevance_score": 15})
        assert result["relevance_score"] == 10

    def test_score_clamped_to_0(self):
        result = _coerce_types({"relevance_score": -5})
        assert result["relevance_score"] == 0

    def test_null_values_normalized(self):
        result = _coerce_types({
            "policy_name": "null",
            "jurisdiction": "N/A",
            "summary": "None",
            "effective_date": "n/a",
        })
        assert result["policy_name"] is None
        assert result["jurisdiction"] is None
        assert result["summary"] is None
        assert result["effective_date"] is None

    def test_missing_relevance_explanation(self):
        result = _coerce_types({})
        assert result["relevance_explanation"] == "No explanation provided"

    def test_policy_type_default_when_not_relevant(self):
        result = _coerce_types({"is_relevant": False, "policy_type": None})
        assert result["policy_type"] == "not_relevant"

    def test_policy_type_default_when_relevant(self):
        result = _coerce_types({"is_relevant": True, "policy_type": "null"})
        assert result["policy_type"] == "unknown"


# --- ClaudeClient.to_policy ---

class TestToPolicy:
    @pytest.fixture
    def client(self):
        # Create without actual API key — we only test to_policy
        client = ClaudeClient.__new__(ClaudeClient)
        client.cost = CostInfo()
        return client

    def test_converts_analysis_to_policy(self, client):
        analysis = PolicyAnalysis(
            is_relevant=True,
            relevance_score=8,
            policy_type="law",
            policy_name="Energy Act",
            jurisdiction="Germany",
            summary="A law about energy",
            effective_date="2024-06-01",
            key_requirements="Must recover heat",
        )
        policy = client.to_policy(analysis, "https://a.gov/p1", "en", "dom1", "scan1")
        assert policy is not None
        assert policy.url == "https://a.gov/p1"
        assert policy.policy_name == "Energy Act"
        assert policy.jurisdiction == "Germany"
        assert policy.policy_type == PolicyType.LAW
        assert policy.effective_date == date(2024, 6, 1)
        assert policy.domain_id == "dom1"
        assert policy.scan_id == "scan1"

    def test_returns_none_when_not_relevant(self, client):
        analysis = PolicyAnalysis(
            is_relevant=False,
            policy_name="Something",
        )
        assert client.to_policy(analysis, "https://a.gov", "en") is None

    def test_returns_none_when_no_name(self, client):
        analysis = PolicyAnalysis(
            is_relevant=True,
            policy_name="",
        )
        assert client.to_policy(analysis, "https://a.gov", "en") is None

    def test_invalid_policy_type_becomes_unknown(self, client):
        analysis = PolicyAnalysis(
            is_relevant=True,
            policy_name="Test",
            policy_type="not_a_real_type",
        )
        policy = client.to_policy(analysis, "https://a.gov", "en")
        assert policy.policy_type == PolicyType.UNKNOWN

    def test_invalid_date_ignored(self, client):
        analysis = PolicyAnalysis(
            is_relevant=True,
            policy_name="Test",
            effective_date="not-a-date",
        )
        policy = client.to_policy(analysis, "https://a.gov", "en")
        assert policy.effective_date is None

    def test_missing_jurisdiction_defaults_to_unknown(self, client):
        analysis = PolicyAnalysis(
            is_relevant=True,
            policy_name="Test",
            jurisdiction="",
        )
        policy = client.to_policy(analysis, "https://a.gov", "en")
        assert policy.jurisdiction == "Unknown"


# --- ClaudeClient.update_cost_estimate ---

class TestUpdateCostEstimate:
    def test_cost_with_both_models(self):
        client = ClaudeClient.__new__(ClaudeClient)
        client.cost = CostInfo(
            input_tokens=100_000,
            output_tokens=10_000,
            screening_calls=50,
            analysis_calls=10,
        )
        client.update_cost_estimate()
        assert client.cost.total_usd > 0

    def test_cost_with_only_analysis(self):
        client = ClaudeClient.__new__(ClaudeClient)
        client.cost = CostInfo(
            input_tokens=50_000,
            output_tokens=5_000,
            screening_calls=0,
            analysis_calls=5,
        )
        client.update_cost_estimate()
        assert client.cost.total_usd > 0

    def test_cost_zero_tokens(self):
        client = ClaudeClient.__new__(ClaudeClient)
        client.cost = CostInfo()
        client.update_cost_estimate()
        assert client.cost.total_usd == 0


# --- Prompt content tests ---

class TestPromptContent:
    """Verify expanded prompts cover broader policy types."""

    def test_screening_mentions_reporting(self):
        assert "reporting" in SCREENING_PROMPT.lower()

    def test_screening_mentions_cost_benefit(self):
        assert "cost-benefit" in SCREENING_PROMPT.lower()

    def test_screening_mentions_tax_incentives(self):
        assert "tax incentiv" in SCREENING_PROMPT.lower()

    def test_screening_mentions_multi_language(self):
        assert "NO" in SCREENING_PROMPT or "any language" in SCREENING_PROMPT.lower()

    def test_analysis_mentions_reporting(self):
        assert "reporting" in ANALYSIS_PROMPT.lower()

    def test_analysis_mentions_cost_benefit(self):
        assert "cost-benefit" in ANALYSIS_PROMPT.lower()

    def test_analysis_mentions_tax_incentives(self):
        assert "tax incentiv" in ANALYSIS_PROMPT.lower()

    def test_analysis_mentions_eed(self):
        assert "EED" in ANALYSIS_PROMPT
