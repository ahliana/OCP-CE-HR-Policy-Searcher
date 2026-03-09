"""Tests for the agent tools and orchestrator."""

import asyncio
import json
import pytest

from src.agent.tools import get_all_tools, execute_tool, POLICY_TOOLS, WEB_SEARCH_TOOL
from src.agent.orchestrator import PolicyAgent, _build_system_prompt
from src.core.config import ConfigLoader
from src.orchestration.events import EventBroadcaster
from src.orchestration.scan_manager import ScanManager


@pytest.fixture
def config():
    c = ConfigLoader(config_dir="config")
    c.load()
    return c


@pytest.fixture
def scan_manager(config):
    broadcaster = EventBroadcaster()
    return ScanManager(config=config, broadcaster=broadcaster, data_dir="data")


class TestToolDefinitions:
    """Verify tool definitions match Anthropic API format."""

    def test_total_tool_count(self):
        tools = get_all_tools()
        assert len(tools) == 13

    def test_policy_tools_have_required_fields(self):
        for tool in POLICY_TOOLS:
            assert "name" in tool, f"Missing name in tool"
            assert "description" in tool, f"Missing description in {tool['name']}"
            assert "input_schema" in tool, f"Missing input_schema in {tool['name']}"
            schema = tool["input_schema"]
            assert schema["type"] == "object", f"Schema type not 'object' in {tool['name']}"
            assert "properties" in schema, f"Missing properties in {tool['name']}"

    def test_web_search_is_server_side(self):
        assert WEB_SEARCH_TOOL["type"] == "web_search_20250305"
        assert WEB_SEARCH_TOOL["name"] == "web_search"
        assert "input_schema" not in WEB_SEARCH_TOOL

    def test_add_domain_has_url_required(self):
        tools = get_all_tools()
        add_domain = next(t for t in tools if t.get("name") == "add_domain")
        assert "url" in add_domain["input_schema"]["required"]

    def test_no_duplicate_tool_names(self):
        tools = get_all_tools()
        names = [t["name"] for t in tools]
        assert len(names) == len(set(names))


class TestToolDispatch:
    """Test that execute_tool dispatches correctly."""

    @pytest.mark.asyncio
    async def test_list_domains(self, config, scan_manager):
        result = await execute_tool("list_domains", {"group": "all"}, config, scan_manager)
        assert "count" in result
        assert "domains" in result
        assert result["count"] > 0

    @pytest.mark.asyncio
    async def test_list_domains_with_region(self, config, scan_manager):
        result = await execute_tool("list_domains", {"region": "eu"}, config, scan_manager)
        assert "count" in result
        for d in result["domains"]:
            assert "eu" in d["region"]

    @pytest.mark.asyncio
    async def test_estimate_cost(self, config, scan_manager):
        result = await execute_tool("estimate_cost", {"domains": "quick"}, config, scan_manager)
        assert "domain_count" in result
        assert "estimated_cost_usd" in result
        assert result["estimated_cost_usd"] > 0

    @pytest.mark.asyncio
    async def test_match_keywords(self, config, scan_manager):
        result = await execute_tool(
            "match_keywords",
            {"text": "data center waste heat recovery policy"},
            config, scan_manager,
        )
        assert "score" in result
        assert result["score"] > 0
        assert len(result["matches"]) > 0

    @pytest.mark.asyncio
    async def test_get_policy_stats(self, config, scan_manager):
        result = await execute_tool("get_policy_stats", {}, config, scan_manager)
        assert "total" in result
        assert "by_jurisdiction" in result
        assert "by_type" in result

    @pytest.mark.asyncio
    async def test_unknown_tool(self, config, scan_manager):
        result = await execute_tool("nonexistent_tool", {}, config, scan_manager)
        assert "error" in result
        assert "Unknown tool" in result["error"]

    @pytest.mark.asyncio
    async def test_get_domain_config_not_found(self, config, scan_manager):
        result = await execute_tool("get_domain_config", {"domain_id": "fake_domain"}, config, scan_manager)
        assert "error" in result
        assert "not found" in result["error"]


class TestSystemPrompt:
    """Test system prompt generation."""

    def test_includes_domain_count(self, config):
        prompt = _build_system_prompt(config)
        assert "275" in prompt or "government websites" in prompt

    def test_includes_regions(self, config):
        prompt = _build_system_prompt(config)
        assert "eu" in prompt
        assert "us" in prompt

    def test_includes_tool_descriptions(self, config):
        prompt = _build_system_prompt(config)
        assert "list_domains" in prompt
        assert "start_scan" in prompt
        assert "web_search" in prompt
        assert "add_domain" in prompt
        assert "analyze_url" in prompt

    def test_non_technical_language(self, config):
        prompt = _build_system_prompt(config)
        assert "not programmers" in prompt
        assert "plain" in prompt
