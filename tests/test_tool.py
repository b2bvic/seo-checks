def test_relative_image_is_a_quality_warning(tool):
    tags = tool.extract_meta('<meta property="og:title" content="Title"><meta property="og:image" content="/image.png">')
    issues = tool.audit(tags)
    assert any(issue["field"] == "og:image" and issue["severity"] == "WARNING" for issue in issues)
    assert any(issue["field"] == "twitter:card" and issue["severity"] == "MISSING" for issue in issues)


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
