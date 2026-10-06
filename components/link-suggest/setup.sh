#!/usr/bin/env bash
# One-shot setup: venv, dependencies, model pre-download
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$DIR/.venv"

echo "=== Link Suggester Setup ==="

# 1. Create venv
if [ ! -d "$VENV" ]; then
    echo "→ Creating virtual environment..."
    python3 -m venv "$VENV"
else
    echo "→ Venv already exists at $VENV"
fi

# 2. Activate and install deps
source "$VENV/bin/activate"
echo "→ Installing dependencies (torch CPU + transformers + utils)..."
pip install --upgrade pip -q
pip install -r "$DIR/requirements.txt" -q

# 3. Pre-download model to HuggingFace cache
echo "→ Pre-downloading dejanseo/google-links model (~1.2GB first time)..."
python3 -c "
from transformers import AutoTokenizer, AutoModelForTokenClassification
print('  Downloading tokenizer...')
AutoTokenizer.from_pretrained('dejanseo/google-links')
print('  Downloading model...')
AutoModelForTokenClassification.from_pretrained('dejanseo/google-links')
print('  Model cached successfully.')
"

echo ""
echo "=== Setup complete ==="
echo "Run: $DIR/run.sh --file <article.md>"
