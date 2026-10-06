import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_markdown_preprocessing_without_model_download():
    source = (ROOT / "suggest_links.py").read_text()
    tree = ast.parse(source)
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "strip_markdown")
    namespace = {"re": re}
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(ROOT / "suggest_links.py"), "exec"), namespace)
    text = "---\ntitle: Demo\n---\n# Title\n**Bold** and [link](https://example.com)"
    assert namespace["strip_markdown"](text) == "Title\nBold and link"


def test_python_source_compiles():
    source = ROOT / "suggest_links.py"
    compile(source.read_text(), str(source), "exec")


def test_url_content_normalizes_inline_markup_without_model_download():
    from types import SimpleNamespace
    from bs4 import BeautifulSoup

    source = ROOT / "suggest_links.py"
    tree = ast.parse(source.read_text())
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "extract_from_url")
    response = SimpleNamespace(
        text="<nav>Ignore this</nav><main><h1>Stop<span>re-explaining</span> \n your\t business&nbsp; to AI.</h1></main>",
        raise_for_status=lambda: None,
    )
    namespace = {"BeautifulSoup": BeautifulSoup, "requests": SimpleNamespace(get=lambda *args, **kwargs: response)}
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(source), "exec"), namespace)
    assert namespace["extract_from_url"]("https://example.com") == "Stop re-explaining your business to AI."
