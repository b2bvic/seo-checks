def test_crawl_counts_internal_and_external_links(tool, monkeypatch):
    monkeypatch.setattr(tool, "fetch", lambda url: '<a href="/target/#section">Internal</a><a href="https://other.example/page">External</a>')
    inbound, outbound, external = tool.crawl_links(["https://example.com/source"], "example.com")
    assert inbound["https://example.com/target"] == 1
    assert outbound["https://example.com/source"] == 1
    assert external["https://example.com/source"] == 1


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
