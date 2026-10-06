"""Dispatch SEO checks without changing their component implementations."""

import argparse
import ast
import importlib.util
from pathlib import Path
import subprocess
import sys
import sysconfig

# command: (repository, Python entry file, description)
COMMANDS = {
    "sitemap": ("sitemap-check", "sitemap-check", "Parse XML sitemaps and optionally check URLs."),
    "robots": ("robots-check", "robots-check", "Inspect robots.txt directives and blocking rules."),
    "redirects": ("redirect-trace", "redirect-trace", "Trace HTTP redirects, loops, and HTTPS downgrades."),
    "headings": ("heading-audit", "heading-audit", "Check HTML heading order and empty headings."),
    "alt": ("alt-audit", "alt-audit", "Classify image alt text and dimension attributes."),
    "og": ("og-check", "og-check", "Check Open Graph and Twitter Card metadata."),
    "readability": ("readability", "readability", "Estimate Flesch readability from a URL or file."),
    "word-freq": ("word-freq", "word-freq", "Count filtered words and phrases in a URL or file."),
    "internal-links": ("internal-link-audit", "internal-link-audit", "Count internal links in a bounded sitemap crawl."),
    "thin-product": ("thin-product", "thin-product", "Find sampled pages below a unique-word threshold."),
    "link-suggest": ("link-suggest", "suggest_links.py", "Suggest anchor phrases with an optional downloaded model."),
    "citations": ("citation-check", "directory-search-links", "Generate directory search links for manual review."),
    "gbp": ("gbp-audit", "local-page-audit", "Check public local-business website markup."),
    "schema-product": ("product-schema", "product-schema", "Check Product JSON-LD fields."),
    "schema-course": ("course-schema", "course-schema", "Check Course and ItemList JSON-LD fields."),
    "schema-health": ("schema-health", "schema-health", "Check configured healthcare JSON-LD field profiles."),
    "hipaa-meta": ("hipaa-meta", "hipaa-meta", "Flag possible identifiers in metadata for human review."),
    "menu": ("menu-seo", "menu-seo", "Inspect restaurant menu markup and visible prices."),
    "spec-sheet": ("spec-sheet", "spec-sheet", "Inspect product specification markup and PDF links."),
    "saas-onboard": ("saas-onboard", "saas-onboard", "Check SaaS indexing directives and canonical paths."),
}


def component_path(repo, entry):
    """Locate source files in a checkout or an installed wheel."""
    checkout = Path(__file__).resolve().parent / "components" / repo / entry
    if checkout.is_file():
        return checkout
    return Path(sysconfig.get_path("data")) / "share" / "seo-checks" / repo / entry


def model_help(path, args):
    """Use the component's argparse parser without importing ML libraries."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    main_node = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")
    namespace = {"argparse": argparse}
    module = ast.Module(body=[main_node], type_ignores=[])
    exec(compile(module, str(path), "exec"), namespace)
    saved_argv = sys.argv
    sys.argv = ["seo-checks link-suggest", *args]
    try:
        namespace["main"]()
    except SystemExit as exc:
        return int(exc.code or 0)
    finally:
        sys.argv = saved_argv
    return 0


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    parser = argparse.ArgumentParser(
        prog="seo-checks",
        description="Run the imported SEO checks. Component arguments pass through unchanged.",
        epilog="Subcommands:\n" + "\n".join(f"  {name:17} {spec[2]}" for name, spec in COMMANDS.items())
        + "\n\nUse seo-checks <subcommand> --help for component options. Prompts are in prompts/.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("subcommand", nargs="?", help="Component command to run")
    if not args or args in (["--help"], ["-h"]):
        parser.print_help()
        return 0
    if args[0] not in COMMANDS:
        parser.error(f"unknown subcommand: {args[0]!r}")
    repo, entry, _ = COMMANDS[args[0]]
    path = component_path(repo, entry)
    if not path.is_file():
        parser.error(f"component entry file is missing: {repo}/{entry}; reinstall seo-checks")
    if repo == "link-suggest":
        if args[1:] in (["--help"], ["-h"]):
            return model_help(path, args[1:])
        missing = [name for name in ("torch", "transformers", "rapidfuzz") if importlib.util.find_spec(name) is None]
        if missing:
            print("link-suggest needs optional libraries: " + ", ".join(missing)
                  + '. Install them with python -m pip install "seo-checks[link-suggest]".'
                  + " Analysis also needs the dejanseo/google-links model.", file=sys.stderr)
            return 2
    # Inherit streams and the caller's directory so relative file arguments work.
    try:
        return subprocess.call([sys.executable, str(path), *args[1:]])
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
