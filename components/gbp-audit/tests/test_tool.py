from bs4 import BeautifulSoup


def test_page_signals_are_separate_from_profile_data(tool):
    soup = BeautifulSoup("<main>Example business</main>", "lxml")
    assert {issue["type"] for issue in tool.check_page_signals(soup)} == {"NO_EMBEDDED_MAP", "NO_VISIBLE_PHONE", "NO_VISIBLE_ADDRESS"}


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output


def test_inline_phone_with_whitespace_is_visible(tool):
    soup = BeautifulSoup(
        '<main><h1>Stop<span>re-explaining</span> your business</h1>'
        '<p><span>(919) \n 555</span> \t 1234</p><p>123 Main Street</p></main>',
        "lxml",
    )
    issues = tool.check_page_signals(soup)
    assert {issue["type"] for issue in issues} == {"NO_EMBEDDED_MAP"}
