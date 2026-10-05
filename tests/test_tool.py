def test_decorative_missing_and_generic_images_are_distinct(tool):
    images = tool.audit_images('<img src="a"><img src="b" alt=""><img src="c" alt="image"><img src="d" alt="Blue bicycle">', "https://example.com")
    assert [image["status"] for image in images] == ["MISSING", "EMPTY", "GENERIC", "OK"]


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
