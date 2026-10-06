def test_unique_words_exclude_navigation(tool):
    total, unique = tool.count_content_words("<nav>Ignore these words</nav><main>River river flows</main>")
    assert (total, unique) == (3, 2)


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
