def test_alias_uses_baseline_separate_from_additional(tool):
    issues = tool.audit("Chiropractic", {"name": "Example"})
    baseline = {issue["field"] for issue in issues if issue["severity"] == "BASELINE"}
    assert baseline == {"address", "telephone"}
    assert any(issue["severity"] == "ADDITIONAL" for issue in issues)


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
