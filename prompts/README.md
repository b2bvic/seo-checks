# Claude Code SEO content skills: sws-skills

`sws-skills` contains Markdown prompts for content teams using Claude Code. These are patterns a team can adapt for hosted-model writing and search workflows.

[Project page](https://scalewithsearch.com/code/seo-checks#sws-skills)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/seo-checks
cd seo-checks
cd prompts
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python -m pytest -q
```

These checks use synthetic input and perform no live sends.

## Usage

Copy a skill folder into the Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills
cp -r skills/anti-slop ~/.claude/skills/
```

## How it works

- Read prompts for freshness review, metadata editing, overlap analysis, and video scripts.
- Use the web2md prompt for page conversion instructions.
- Use anti-slop as a written output-review checklist.

## Limits

- The repository contains instructions rather than an automated SEO runtime.
- Skills require the tools and source access named in each prompt.
- Generated findings need human review.

## Related repositories

- [web2md](https://github.com/b2bvic/web2md)
- [twitter-bookmarks](https://github.com/b2bvic/twitter-bookmarks)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
