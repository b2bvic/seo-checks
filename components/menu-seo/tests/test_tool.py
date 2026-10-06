from bs4 import BeautifulSoup


def test_menu_pdf_and_visible_prices_are_reported(tool):
    soup = BeautifulSoup('<a href="menu.pdf">Lunch menu</a><p>Soup $5 Salad $6 Tea $2</p>', "lxml")
    issues, prices = tool.check_menu_accessibility(soup, "https://example.com")
    assert prices == 3
    assert any(issue["type"] == "PDF_MENU" for issue in issues)
    assert not any(issue["type"] == "NO_VISIBLE_PRICES" for issue in issues)


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output


def test_inline_menu_text_and_dietary_whitespace(tool):
    soup = BeautifulSoup(
        '<a href="lunch.pdf">Lunch<span>menu</span></a>'
        '<p><span>gluten \n\t free</span> soup</p><p>Tea $2 Soup $5 Salad $6</p>',
        "lxml",
    )
    issues, prices = tool.check_menu_accessibility(soup, "https://example.com")
    assert any(issue["type"] == "PDF_MENU" for issue in issues)
    assert prices == 3
    assert "gluten free" in tool.check_dietary_labels(soup)
