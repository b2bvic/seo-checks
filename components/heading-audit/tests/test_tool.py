def test_skipped_empty_and_duplicate_headings(tool):
    headings, issues = tool.audit_headings("<h1>Start</h1><h3></h3><h1>Again</h1>")
    assert len(headings) == 3
    details = [issue["detail"] for issue in issues]
    assert any("Multiple H1" in detail for detail in details)
    assert any("Skipped heading" in detail for detail in details)
    assert any("Empty H3" in detail for detail in details)


def test_valid_outline_has_no_issues(tool):
    assert tool.audit_headings("<h1>Start</h1><h2>Next</h2><h3>Detail</h3>")[1] == []


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output


def test_inline_heading_text_keeps_word_boundaries(tool):
    headings, issues = tool.audit_headings(
        "<h1>Stop<span>re-explaining</span> \n your\t business&nbsp; to AI.</h1>"
    )
    assert headings[0]["text"] == "Stop re-explaining your business to AI."
    assert issues == []
