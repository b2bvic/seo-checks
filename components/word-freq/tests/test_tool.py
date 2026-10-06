def test_stop_words_do_not_contribute_to_density(tool):
    words = tool.tokenize("The river and the river flow.")
    assert words == ["river", "river", "flow"]
    assert tool.ngrams(words, 2) == ["river river", "river flow"]


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output


def test_inline_content_text_normalizes_whitespace(tool):
    text = tool.extract_text(
        "<main><h1>Stop<span>re-explaining</span> \n your\t business&nbsp; to AI.</h1></main>"
    )
    assert text == "Stop re-explaining your business to AI."
    assert tool.tokenize(text) == ["stop", "re", "explaining", "business", "ai"]
