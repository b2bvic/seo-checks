def test_stop_words_do_not_contribute_to_density(tool):
    words = tool.tokenize("The river and the river flow.")
    assert words == ["river", "river", "flow"]
    assert tool.ngrams(words, 2) == ["river river", "river flow"]


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
