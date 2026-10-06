#!/usr/bin/env python3
"""Run each imported pytest suite separately and record counts and reasons."""

import argparse
import importlib.util
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from seo_checks import COMMANDS


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / ".test-results")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    results = []
    components = [(repo, ROOT / "components" / repo) for repo, _, _ in COMMANDS.values()]
    components.append(("sws-skills", ROOT / "prompts"))
    for repo, path in components:
        xml_path = output / f"{repo}.xml"
        xml_path.unlink(missing_ok=True)
        command = [sys.executable, "-m", "pytest", "-q", "tests", "-p", "no:cacheprovider", f"--junitxml={xml_path}"]
        modules = ["pytest"]
        if repo not in ("link-suggest", "sws-skills"):
            modules += ["click", "requests"]
            if repo not in ("citation-check", "sitemap-check", "robots-check", "redirect-trace"):
                modules += ["bs4", "lxml"]
        missing = [name for name in modules if importlib.util.find_spec(name) is None]
        record = dict(component=repo, cwd=str(path.relative_to(ROOT)), command=shlex.join(command),
                      passed=0, failed=0, errors=0, skipped=0, not_run=0)
        if missing:
            record.update(status="skipped", reason="Required test dependencies are unavailable: " + ", ".join(missing))
            # The untouched suites use plain, non-parametrized test functions.
            import ast
            record["not_run"] = sum(
                isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
                for file in (path / "tests").glob("test*.py")
                for node in ast.parse(file.read_text()).body
            )
            (output / f"{repo}.log").write_text(record["reason"] + "\n")
        else:
            env = os.environ.copy()
            env.update(PYTHONDONTWRITEBYTECODE="1", PYTEST_DISABLE_PLUGIN_AUTOLOAD="1", TMPDIR=str(output))
            try:
                completed = subprocess.run(command, cwd=path, env=env, text=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
                (output / f"{repo}.log").write_text(completed.stdout)
                record.update(returncode=completed.returncode, status="passed" if completed.returncode == 0 else "failed")
                if xml_path.exists():
                    suites = ET.parse(xml_path).getroot().iter("testsuite")
                    for suite in suites:
                        count = {key: int(suite.get(key, "0")) for key in ("tests", "failures", "errors", "skipped")}
                        record["failed"] += count["failures"]
                        record["errors"] += count["errors"]
                        record["skipped"] += count["skipped"]
                        record["passed"] += max(0, count["tests"] - count["failures"] - count["errors"] - count["skipped"])
                else:
                    record.update(status="failed", reason="pytest did not produce a count report")
            except subprocess.TimeoutExpired:
                record.update(status="failed", reason="Test suite exceeded 120 seconds")
                (output / f"{repo}.log").write_text(record["reason"] + "\n")
        results.append(record)
        print(f"{repo}: {record['status']}, {record['passed']} passed, {record['failed']} failed, "
              f"{record['errors']} errors, {record['skipped']} skipped, {record['not_run']} not run", flush=True)
    (output / "summary.json").write_text(json.dumps(results, indent=2) + "\n")
    return int(any(record["status"] == "failed" for record in results))


if __name__ == "__main__":
    raise SystemExit(main())
