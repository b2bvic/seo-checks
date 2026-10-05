import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_each_skill_has_unique_name_and_description():
    names = []
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = path.read_text()
        assert text.startswith("---\n"), path
        header = text.split("---", 2)[1]
        name = re.search(r"^name: (.+)$", header, re.MULTILINE)
        description = re.search(r"^description: (.+)$", header, re.MULTILINE)
        assert name and description, path
        assert name.group(1) == path.parent.name
        names.append(name.group(1))
        assert "## " in text, path
    assert len(names) == len(set(names)) == 6
