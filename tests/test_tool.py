def test_directory_link_encodes_query_and_requires_manual_review(tool):
    result = tool.directory_search_link(tool.DIRECTORIES[0], "Example & Co", "Sample City")
    assert "Example+%26+Co" in result["url"]
    assert "Sample+City" in result["url"]
    assert result["status"] == "manual_review_required"


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
