def test_decorative_missing_and_generic_images_are_distinct(tool):
    images = tool.audit_images('<img src="a"><img src="b" alt=""><img src="c" alt="image"><img src="d" alt="Blue bicycle">', "https://example.com")
    assert [image["status"] for image in images] == ["MISSING", "EMPTY", "GENERIC", "OK"]


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output


def test_inline_markup_does_not_change_image_alt_attributes(tool):
    html = '<h1>Stop<span>re-explaining</span> your business</h1><a><span><img src="a.png" alt="Stop re-explaining your business"></span></a>'
    images = tool.audit_images(html, "https://example.com")
    assert images[0]["alt"] == "Stop re-explaining your business"
    assert images[0]["status"] == "OK"
