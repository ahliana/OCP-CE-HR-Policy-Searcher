"""Tests for AsyncCrawler — URL filtering, link extraction, and diagnosis."""

import re
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from src.core.crawler import AsyncCrawler, _diagnose_response


# --- _diagnose_response ---

class TestDiagnoseResponse:
    def test_cloudflare_server(self):
        result = _diagnose_response(403, {"server": "cloudflare"}, "")
        assert "Cloudflare" in result

    def test_akamai_server(self):
        result = _diagnose_response(403, {"server": "AkamaiGHost"}, "")
        assert "Akamai" in result

    def test_body_pattern_access_denied(self):
        result = _diagnose_response(403, {}, "Access Denied - you are blocked")
        assert "Access Denied" in result

    def test_body_pattern_rate_limit(self):
        result = _diagnose_response(429, {}, "rate limit exceeded")
        assert "rate limited" in result

    def test_plain_status_code(self):
        result = _diagnose_response(500, {}, "")
        assert result == "HTTP 500"


# --- AsyncCrawler._should_skip_url ---

class TestShouldSkipUrl:
    def test_skips_matching_path(self):
        crawler = AsyncCrawler(url_skip_paths=["/login", "/admin"])
        assert crawler._should_skip_url("https://a.gov/login")
        assert crawler._should_skip_url("https://a.gov/admin/panel")

    def test_does_not_skip_normal_url(self):
        crawler = AsyncCrawler(url_skip_paths=["/login"])
        assert not crawler._should_skip_url("https://a.gov/policy")

    def test_skips_matching_pattern(self):
        crawler = AsyncCrawler(url_skip_patterns=[re.compile(r"/archive/\d+")])
        assert crawler._should_skip_url("https://a.gov/archive/2024/doc")

    def test_does_not_skip_non_matching_pattern(self):
        crawler = AsyncCrawler(url_skip_patterns=[re.compile(r"/archive/\d+")])
        assert not crawler._should_skip_url("https://a.gov/policy/heat")


# --- AsyncCrawler._extract_links ---

class TestExtractLinks:
    def test_extracts_same_domain_links(self):
        crawler = AsyncCrawler()
        html = """
        <html><body>
            <a href="/page2">Page 2</a>
            <a href="https://example.gov/page3">Page 3</a>
            <a href="https://other.com/external">External</a>
        </body></html>
        """
        links = crawler._extract_links(
            html, "https://example.gov/page1", "https://example.gov",
        )
        assert "https://example.gov/page2" in links
        assert "https://example.gov/page3" in links
        assert not any("other.com" in l for l in links)

    def test_skips_file_extensions(self):
        crawler = AsyncCrawler()
        html = """
        <html><body>
            <a href="/doc.pdf">PDF</a>
            <a href="/image.jpg">Image</a>
            <a href="/page">Page</a>
        </body></html>
        """
        links = crawler._extract_links(
            html, "https://example.gov/", "https://example.gov",
        )
        assert not any(l.endswith(".pdf") for l in links)
        assert not any(l.endswith(".jpg") for l in links)
        assert "https://example.gov/page" in links

    def test_blocked_patterns_filtered(self):
        crawler = AsyncCrawler()
        html = """
        <html><body>
            <a href="/policy/good">Good</a>
            <a href="/archive/old">Old</a>
        </body></html>
        """
        links = crawler._extract_links(
            html, "https://example.gov/", "https://example.gov",
            blocked_patterns=["/archive/*"],
        )
        assert "https://example.gov/policy/good" in links
        assert not any("archive" in l for l in links)

    def test_allowed_patterns_restrict(self):
        crawler = AsyncCrawler()
        html = """
        <html><body>
            <a href="/policy/heat">Policy</a>
            <a href="/about">About</a>
        </body></html>
        """
        links = crawler._extract_links(
            html, "https://example.gov/", "https://example.gov",
            allowed_patterns=["/policy/*"],
        )
        assert "https://example.gov/policy/heat" in links
        assert not any("about" in l for l in links)

    def test_removes_nav_links(self):
        crawler = AsyncCrawler()
        html = """
        <html><body>
            <nav><a href="/home">Home</a></nav>
            <div><a href="/content">Content</a></div>
        </body></html>
        """
        links = crawler._extract_links(
            html, "https://example.gov/", "https://example.gov",
        )
        assert "https://example.gov/content" in links
        # Nav links should be removed
        assert "https://example.gov/home" not in links

    def test_deduplicates_links(self):
        crawler = AsyncCrawler()
        html = """
        <html><body>
            <a href="/page">Link 1</a>
            <a href="/page">Link 2</a>
        </body></html>
        """
        links = crawler._extract_links(
            html, "https://example.gov/", "https://example.gov",
        )
        assert links.count("https://example.gov/page") == 1

    def test_normalizes_urls_strips_fragment(self):
        crawler = AsyncCrawler()
        html = '<html><body><a href="/page#section">Link</a></body></html>'
        links = crawler._extract_links(
            html, "https://example.gov/", "https://example.gov",
        )
        # Fragments should be stripped during normalization
        assert any("/page" in l and "#" not in l for l in links)

    def test_skips_non_http_schemes(self):
        crawler = AsyncCrawler()
        html = """
        <html><body>
            <a href="mailto:test@test.com">Email</a>
            <a href="javascript:void(0)">JS</a>
            <a href="/valid">Valid</a>
        </body></html>
        """
        links = crawler._extract_links(
            html, "https://example.gov/", "https://example.gov",
        )
        assert not any("mailto" in l for l in links)
        assert not any("javascript" in l for l in links)


# --- AsyncCrawler fetch and crawl (async tests using mocked httpx) ---

def _mock_response(status_code=200, text="", headers=None):
    """Create a mock httpx.Response."""
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.text = text
    resp.headers = headers or {}
    return resp


class TestAsyncCrawlerFetch:
    @pytest.mark.asyncio
    async def test_fetch_success(self):
        crawler = AsyncCrawler(delay_seconds=0, max_retries=1)
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=_mock_response(
            200, "<html><body>Hello</body></html>",
            headers={"content-type": "text/html"},
        ))
        result = await crawler._fetch_with_retry(mock_client, "https://example.gov/page")
        assert result.status.value == "success"
        assert "Hello" in result.content

    @pytest.mark.asyncio
    async def test_fetch_404(self):
        crawler = AsyncCrawler(delay_seconds=0, max_retries=1)
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=_mock_response(404, ""))
        result = await crawler._fetch_with_retry(mock_client, "https://example.gov/missing")
        assert result.status.value == "not_found"

    @pytest.mark.asyncio
    async def test_fetch_403(self):
        crawler = AsyncCrawler(delay_seconds=0, max_retries=1)
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=_mock_response(403, "Access denied"))
        result = await crawler._fetch_with_retry(mock_client, "https://example.gov/denied")
        assert result.status.value == "access_denied"

    @pytest.mark.asyncio
    async def test_fetch_429_rate_limited(self):
        crawler = AsyncCrawler(delay_seconds=0, max_retries=1)
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=_mock_response(429, "rate limit"))
        result = await crawler._fetch_with_retry(mock_client, "https://example.gov/api")
        assert result.status.value == "rate_limited"

    @pytest.mark.asyncio
    async def test_fetch_timeout_retries(self):
        crawler = AsyncCrawler(delay_seconds=0, max_retries=2)
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(side_effect=httpx.TimeoutException("timeout"))
        result = await crawler._fetch_with_retry(mock_client, "https://example.gov/slow")
        assert result.status.value == "timeout"
        assert mock_client.get.call_count == 2

    @pytest.mark.asyncio
    async def test_fetch_500_returns_unknown_error(self):
        crawler = AsyncCrawler(delay_seconds=0, max_retries=1)
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=_mock_response(500, "Server Error"))
        result = await crawler._fetch_with_retry(mock_client, "https://example.gov/error")
        assert result.status.value == "unknown_error"
