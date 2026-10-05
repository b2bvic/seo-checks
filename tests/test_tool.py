def test_block_all_and_rule_before_agent_are_reported(tool):
    blocks, sitemaps, issues = tool.parse_robots("Allow: /public\nUser-agent: *\nDisallow: /\nSitemap: https://example.com/sitemap.xml")
    assert len(blocks) == 1
    assert sitemaps == ["https://example.com/sitemap.xml"]
    assert {issue["severity"] for issue in issues} >= {"ERROR", "CRITICAL"}


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
