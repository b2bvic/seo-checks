def test_duplicate_list_positions_are_invalid(tool):
    entries = [{"@type": "ListItem", "position": 1, "url": f"https://example.com/{i}"} for i in range(3)]
    assert any("unique" in error for error in tool.audit_item_list({"itemListElement": entries}, 0)["google_errors"])


def test_optional_fields_do_not_become_required_errors(tool):
    report = tool.audit_course({"name": "Course", "description": "Learn"}, "Course")
    assert report["google_errors"] == []
    assert report["schema_org_optional_absent"]


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
