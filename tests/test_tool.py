def test_malformed_xml_returns_parse_issue(tool):
    urls, children, issues = tool.parse_sitemap("<broken", "https://example.com/sitemap.xml")
    assert urls == children == []
    assert issues[0]["severity"] == "CRITICAL"


def test_namespaced_url_and_index(tool):
    xml = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://example.com/a</loc><lastmod>2026-10-05</lastmod></url></urlset>'
    assert tool.parse_sitemap(xml, "unused")[0] == [{"url": "https://example.com/a", "lastmod": "2026-10-05"}]
    index = '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><sitemap><loc>https://example.com/a.xml</loc></sitemap></sitemapindex>'
    assert tool.parse_sitemap(index, "unused")[1] == ["https://example.com/a.xml"]


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
