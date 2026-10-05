from bs4 import BeautifulSoup


def test_pdf_link_is_resolved_without_reading_pdf(tool):
    soup = BeautifulSoup('<a href="/data.pdf">Technical specifications</a>', "lxml")
    issues, links = tool.check_pdf_specs(soup, "https://example.com/product")
    assert issues[0]["type"] == "SPEC_IN_PDF"
    assert links[0]["url"] == "https://example.com/data.pdf"


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
