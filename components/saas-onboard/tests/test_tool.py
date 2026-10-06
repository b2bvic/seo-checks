def test_auth_noindex_check_uses_returned_html(tool):
    missing, _ = tool.check_noindex("<html></html>", "https://example.com/login")
    protected, _ = tool.check_noindex('<meta name="robots" content="noindex">', "https://example.com/login")
    assert missing[0]["type"] == "AUTH_PAGE_INDEXED"
    assert protected == []


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
