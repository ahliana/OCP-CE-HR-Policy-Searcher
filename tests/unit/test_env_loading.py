"""Tests for .env loading with explicit project-root path resolution.

All three entry points (agent, MCP server, API) resolve the .env file
relative to their own ``__file__`` so that credentials load correctly
even when the process working directory is *not* the project root
(e.g. when started as a Claude Code MCP subprocess).
"""

import base64
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest


# ---------------------------------------------------------------------------
# Project-root resolution
# ---------------------------------------------------------------------------

class TestProjectRootResolution:
    """Each entry point must resolve .env from the project root, not CWD."""

    @pytest.fixture(autouse=True)
    def _project_root(self):
        self.project_root = Path(__file__).resolve().parents[2]

    def test_agent_resolves_project_root(self):
        """src/agent/__main__.py should resolve project root 2 levels up."""
        agent_file = self.project_root / "src" / "agent" / "__main__.py"
        assert agent_file.exists()
        resolved = agent_file.resolve().parents[2]
        assert (resolved / ".env").exists() or (resolved / "config").is_dir()

    def test_mcp_server_resolves_project_root(self):
        """src/mcp/server.py should resolve project root 2 levels up."""
        server_file = self.project_root / "src" / "mcp" / "server.py"
        assert server_file.exists()
        resolved = server_file.resolve().parents[2]
        assert (resolved / ".env").exists() or (resolved / "config").is_dir()

    def test_api_app_resolves_project_root(self):
        """src/api/app.py should resolve project root 2 levels up."""
        api_file = self.project_root / "src" / "api" / "app.py"
        assert api_file.exists()
        resolved = api_file.resolve().parents[2]
        assert (resolved / ".env").exists() or (resolved / "config").is_dir()


class TestLoadDotenvUsesExplicitPath:
    """Entry points must call load_dotenv with an explicit file path."""

    @pytest.fixture(autouse=True)
    def _project_root(self):
        self.project_root = Path(__file__).resolve().parents[2]

    def _read_source(self, relative_path: str) -> str:
        return (self.project_root / relative_path).read_text(encoding="utf-8")

    def test_agent_uses_explicit_env_path(self):
        source = self._read_source("src/agent/__main__.py")
        assert 'load_dotenv(_project_root / ".env"' in source

    def test_mcp_server_uses_explicit_env_path(self):
        source = self._read_source("src/mcp/server.py")
        assert 'load_dotenv(_project_root / ".env"' in source

    def test_api_uses_explicit_env_path(self):
        source = self._read_source("src/api/app.py")
        assert 'load_dotenv(_project_root / ".env"' in source

    def test_all_use_override_true(self):
        """override=True is required so .env wins over stale system vars."""
        for path in [
            "src/agent/__main__.py",
            "src/mcp/server.py",
            "src/api/app.py",
        ]:
            source = self._read_source(path)
            assert "override=True" in source, f"{path} missing override=True"


class TestDotenvOverrideBehavior:
    """load_dotenv(override=True) should replace stale env vars."""

    def test_override_replaces_empty_env_var(self, tmp_path):
        from dotenv import load_dotenv

        env_file = tmp_path / ".env"
        env_file.write_text("TEST_OVERRIDE_KEY=from_file\n")

        with patch.dict(os.environ, {"TEST_OVERRIDE_KEY": ""}, clear=False):
            assert os.environ["TEST_OVERRIDE_KEY"] == ""
            load_dotenv(env_file, override=True)
            assert os.environ["TEST_OVERRIDE_KEY"] == "from_file"

    def test_override_replaces_stale_value(self, tmp_path):
        from dotenv import load_dotenv

        env_file = tmp_path / ".env"
        env_file.write_text("TEST_STALE_KEY=new_value\n")

        with patch.dict(os.environ, {"TEST_STALE_KEY": "old_value"}, clear=False):
            load_dotenv(env_file, override=True)
            assert os.environ["TEST_STALE_KEY"] == "new_value"

    def test_no_override_keeps_empty_value(self, tmp_path):
        """Without override, empty env var is kept (the bug scenario)."""
        from dotenv import load_dotenv

        env_file = tmp_path / ".env"
        env_file.write_text("TEST_NOOVERRIDE=from_file\n")

        with patch.dict(os.environ, {"TEST_NOOVERRIDE": ""}, clear=False):
            load_dotenv(env_file, override=False)
            assert os.environ["TEST_NOOVERRIDE"] == ""


# ---------------------------------------------------------------------------
# Google Sheets credential validation
# ---------------------------------------------------------------------------

class TestSheetsClientCredentialValidation:
    """SheetsClient.connect() should reject clearly invalid credentials."""

    def test_rejects_none_credentials(self):
        from src.output.sheets import SheetsClient

        client = SheetsClient(credentials_b64=None, spreadsheet_id="test-id")
        with pytest.raises(ValueError, match="GOOGLE_CREDENTIALS looks invalid"):
            client.connect()

    def test_rejects_empty_credentials(self):
        from src.output.sheets import SheetsClient

        client = SheetsClient(credentials_b64="", spreadsheet_id="test-id")
        with pytest.raises(ValueError, match="GOOGLE_CREDENTIALS looks invalid"):
            client.connect()

    def test_rejects_short_credentials(self):
        from src.output.sheets import SheetsClient

        client = SheetsClient(credentials_b64="dG9vc2hvcnQ=", spreadsheet_id="x")
        with pytest.raises(ValueError, match="length="):
            client.connect()

    def test_rejects_bad_base64(self):
        from src.output.sheets import SheetsClient

        # 100 chars of non-base64
        bad = "!" * 100
        client = SheetsClient(credentials_b64=bad, spreadsheet_id="test-id")
        with pytest.raises(Exception):
            client.connect()

    def test_accepts_valid_base64_credentials(self):
        """Valid base64 should pass the length check (will fail at Google auth)."""
        from src.output.sheets import SheetsClient

        creds_dict = {"type": "service_account", "project_id": "test"}
        valid_b64 = base64.b64encode(
            __import__("json").dumps(creds_dict).encode()
        ).decode()

        client = SheetsClient(credentials_b64=valid_b64, spreadsheet_id="test-id")
        # Should pass validation but fail at Google auth (no real credentials)
        with pytest.raises(Exception) as exc_info:
            client.connect()
        # Should NOT be a ValueError about invalid credentials
        assert "GOOGLE_CREDENTIALS looks invalid" not in str(exc_info.value)


# ---------------------------------------------------------------------------
# Config loader credential plumbing
# ---------------------------------------------------------------------------

class TestConfigLoaderCredentials:
    """ConfigLoader should pass env vars through to OutputSettings."""

    def test_google_credentials_from_env(self):
        with patch.dict(os.environ, {"GOOGLE_CREDENTIALS": "test_b64_value"}, clear=False):
            from src.core.config import ConfigLoader
            config = ConfigLoader(config_dir="config")
            config.load()
            assert config.settings.output.google_credentials_b64 == "test_b64_value"

    def test_spreadsheet_id_from_env(self):
        with patch.dict(os.environ, {"SPREADSHEET_ID": "sheet_123"}, clear=False):
            from src.core.config import ConfigLoader
            config = ConfigLoader(config_dir="config")
            config.load()
            assert config.settings.output.spreadsheet_id == "sheet_123"

    def test_missing_credentials_default_to_none(self):
        with patch.dict(
            os.environ,
            {"GOOGLE_CREDENTIALS": "", "SPREADSHEET_ID": ""},
            clear=False,
        ):
            # Remove them entirely so they default
            env = os.environ.copy()
            env.pop("GOOGLE_CREDENTIALS", None)
            env.pop("SPREADSHEET_ID", None)
            with patch.dict(os.environ, env, clear=True):
                from src.core.config import ConfigLoader
                config = ConfigLoader(config_dir="config")
                config.load()
                assert config.settings.output.google_credentials_b64 is None


# ---------------------------------------------------------------------------
# Dependency checks
# ---------------------------------------------------------------------------

class TestDotenvDependency:
    """python-dotenv must be listed as a project dependency."""

    def test_dotenv_in_pyproject(self):
        pyproject = Path(__file__).resolve().parents[2] / "pyproject.toml"
        if pyproject.exists():
            assert "python-dotenv" in pyproject.read_text()
        else:
            pytest.skip("No pyproject.toml found")

    def test_dotenv_importable(self):
        from dotenv import load_dotenv
        assert callable(load_dotenv)
