def test_graph_product_and_missing_offer_fields(tool):
    schemas = tool.extract_jsonld('<script type="application/ld+json">{"@graph":[{"@type":"Product","name":"Widget","offers":{"price":"10"}}]}</script>')
    products = tool.find_products(schemas)
    assert len(products) == 1
    missing = {issue["field"] for issue in tool.audit_product(products[0]) if issue["severity"] == "MISSING"}
    assert missing == {"priceCurrency", "availability"}


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
