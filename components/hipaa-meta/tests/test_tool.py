from bs4 import BeautifulSoup


def test_possible_identifier_location_is_reported(tool):
    soup = BeautifulSoup('<meta name="description" content="Contact demo@example.com">', "lxml")
    issues = tool.check_meta_tags(soup, "https://example.com")
    assert issues[0]["type"] == "EMAIL_IN_META"
    assert issues[0]["location"] == "<meta name='description'>"


def test_sensitive_query_parameter_is_flagged(tool):
    soup = BeautifulSoup('<a href="/form?patient_id=demo">Form</a>', "lxml")
    assert tool.check_urls(soup, "https://example.com")[0]["type"] == "PII_IN_LINK_PARAM"


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
