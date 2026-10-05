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
