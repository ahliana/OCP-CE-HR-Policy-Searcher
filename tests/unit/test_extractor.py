"""Tests for HtmlExtractor."""

import pytest

from src.core.extractor import HtmlExtractor


@pytest.fixture
def extractor():
    # Use a non-existent config dir so defaults are used
    return HtmlExtractor(config_dir="__nonexistent__")


class TestExtractBasicContent:
    def test_extracts_text_from_body(self, extractor):
        html = "<html><body><p>Hello World</p></body></html>"
        result = extractor.extract(html)
        assert "Hello World" in result.text

    def test_word_count(self, extractor):
        html = "<html><body><p>one two three four five</p></body></html>"
        result = extractor.extract(html)
        assert result.word_count == 5

    def test_extracts_title_from_title_tag(self, extractor):
        html = "<html><head><title>Test Page</title></head><body><p>Content</p></body></html>"
        result = extractor.extract(html)
        assert result.title == "Test Page"

    def test_extracts_title_from_h1_fallback(self, extractor):
        html = "<html><body><h1>Main Heading</h1><p>Content</p></body></html>"
        result = extractor.extract(html)
        assert result.title == "Main Heading"

    def test_detects_language_from_html_attr(self, extractor):
        html = '<html lang="de"><body><p>Inhalt</p></body></html>'
        result = extractor.extract(html)
        assert result.language == "de"

    def test_returns_empty_text_for_empty_html(self, extractor):
        result = extractor.extract("")
        assert result.text == ""
        assert result.word_count == 0


class TestBoilerplateRemoval:
    def test_removes_nav(self, extractor):
        html = """
        <html><body>
            <nav><a href="/home">Home</a><a href="/about">About</a></nav>
            <main><p>Important policy content here</p></main>
        </body></html>
        """
        result = extractor.extract(html)
        assert "Important policy content" in result.text
        assert "Home" not in result.text

    def test_removes_footer(self, extractor):
        html = """
        <html><body>
            <main><p>Policy text</p></main>
            <footer><p>Copyright 2024</p></footer>
        </body></html>
        """
        result = extractor.extract(html)
        assert "Policy text" in result.text
        assert "Copyright" not in result.text

    def test_removes_script_and_style(self, extractor):
        html = """
        <html><body>
            <script>var x = 1;</script>
            <style>.red { color: red; }</style>
            <p>Real content</p>
        </body></html>
        """
        result = extractor.extract(html)
        assert "Real content" in result.text
        assert "var x" not in result.text
        assert ".red" not in result.text

    def test_removes_cookie_banner_by_class(self, extractor):
        html = """
        <html><body>
            <div class="cookie-consent">Accept cookies</div>
            <article><p>Policy details</p></article>
        </body></html>
        """
        result = extractor.extract(html)
        assert "Policy details" in result.text
        assert "Accept cookies" not in result.text

    def test_removes_sidebar_by_id(self, extractor):
        html = """
        <html><body>
            <div id="sidebar-nav">Links here</div>
            <article><p>Main content</p></article>
        </body></html>
        """
        result = extractor.extract(html)
        assert "Main content" in result.text
        assert "Links here" not in result.text


class TestMainContentDetection:
    def test_finds_main_tag(self, extractor):
        html = """
        <html><body>
            <div><p>Outer noise</p></div>
            <main><p>Main content here</p></main>
        </body></html>
        """
        result = extractor.extract(html)
        assert "Main content here" in result.text

    def test_finds_article_tag(self, extractor):
        html = """
        <html><body>
            <article><p>Article content</p></article>
            <aside><p>Sidebar stuff</p></aside>
        </body></html>
        """
        result = extractor.extract(html)
        assert "Article content" in result.text

    def test_finds_content_class(self, extractor):
        html = """
        <html><body>
            <div class="page-content"><p>Real stuff</p></div>
            <div class="ad-block"><p>Buy now</p></div>
        </body></html>
        """
        result = extractor.extract(html)
        assert "Real stuff" in result.text

    def test_falls_back_to_body(self, extractor):
        html = "<html><body><p>Just body</p></body></html>"
        result = extractor.extract(html)
        assert "Just body" in result.text


class TestMaxLength:
    def test_respects_max_length(self):
        extractor = HtmlExtractor.__new__(HtmlExtractor)
        extractor._remove_tags = []
        extractor._remove_patterns = []
        extractor._content_patterns = []
        extractor._max_length = 20

        html = "<html><body><p>" + "a" * 100 + "</p></body></html>"
        result = extractor.extract(html)
        assert len(result.text) <= 20
