def test_counts_and_flesch_formula(tool):
    result = tool.analyze("The cat sat. The dog ran.")
    assert result["total_words"] == 6
    assert result["total_sentences"] == 2
    assert result["total_syllables"] == 6
    assert result["flesch_reading_ease"] == 100
    assert result["flesch_kincaid_grade"] == 0


def test_empty_input_does_not_divide_by_zero(tool):
    assert tool.analyze("")["total_words"] == 0


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output


def test_inline_content_text_normalizes_whitespace(tool):
    text = tool.extract_text(
        "<nav>Ignore this</nav><main><h1>Stop<span>re-explaining</span> \n your\t business&nbsp; to AI.</h1></main>"
    )
    assert text == "Stop re-explaining your business to AI."
    assert tool.analyze(text)["total_words"] == 6
