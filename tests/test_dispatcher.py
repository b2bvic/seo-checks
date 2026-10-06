"""Exercise the public dispatcher and its component argument forwarding."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from seo_checks import COMMANDS

ROOT = Path(__file__).resolve().parents[1]


def run(*args, cwd=None):
    return subprocess.run(
        [sys.executable, str(ROOT / "seo_checks.py"), *args],
        cwd=cwd, input="", text=True, capture_output=True, timeout=30,
    )


class DispatcherTests(unittest.TestCase):
    def test_top_level_help_lists_every_description(self):
        result = run("--help")
        self.assertEqual(result.returncode, 0, result.stderr)
        for command, (_, _, description) in COMMANDS.items():
            self.assertIn(command, result.stdout)
            self.assertIn(description, result.stdout)

    def test_unknown_command_returns_usage_error(self):
        result = run("unknown-component")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown subcommand", result.stderr)

    def test_relative_file_and_options_pass_through(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "words.txt").write_text("The river and the river flow.")
            result = run("word-freq", "words.txt", "--top", "1", "--json-output", cwd=directory)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["total_words"], 3)
        self.assertEqual(len(report["single_words"]), 1)
        self.assertEqual(report["single_words"][0]["word"], "river")
        self.assertEqual(report["single_words"][0]["count"], 2)

    def test_component_usage_error_propagates(self):
        result = run("robots", "--unknown-option")
        self.assertEqual(result.returncode, 2)
        self.assertIn("No such option", result.stderr)


def help_test(command):
    def test(self):
        result = run(command, "--help")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("usage:", result.stdout.lower())
        self.assertIn("--help", result.stdout)
    return test


for name in COMMANDS:
    setattr(DispatcherTests, "test_help_" + name.replace("-", "_"), help_test(name))


if __name__ == "__main__":
    unittest.main()
