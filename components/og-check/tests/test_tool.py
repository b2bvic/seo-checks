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


def test_title_whitespace_with_inline_body_markup(tool):
    tags = tool.extract_meta(
        "<title>Stop \n re-explaining\t your business&nbsp; to AI.</title><h1>Stop<span>re-explaining</span> your business</h1>"
    )
    assert tags["_title"] == "Stop re-explaining your business to AI."
