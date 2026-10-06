#!/usr/bin/env bash
# Venv-activating wrapper — the skill calls this, never suggest_links.py directly
DIR="$(cd "$(dirname "$0")" && pwd)"

if [ ! -d "$DIR/.venv" ]; then
    echo "ERROR: Venv not found. Run: bash $DIR/setup.sh" >&2
    exit 1
fi

source "$DIR/.venv/bin/activate"
python "$DIR/suggest_links.py" "$@"
