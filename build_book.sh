#!/usr/bin/env bash
# build_book.sh — Local helper to build the mdBook documentation.
# Copies wiki/ content into src/wiki/ before building.
#
# Usage:
#   ./build_book.sh          # build only
#   ./build_book.sh serve    # build and serve with live-reload

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "📂 Copying wiki files into src/wiki/ ..."
mkdir -p src/wiki
cp wiki/*.md src/wiki/
echo "   Copied $(ls src/wiki/*.md | wc -l | tr -d ' ') files."

if ! command -v mdbook &>/dev/null; then
    echo ""
    echo "⚠️  mdbook not found. Install it from:"
    echo "   https://rust-lang.github.io/mdBook/guide/installation.html"
    echo ""
    echo "   Quick install (Linux/macOS):"
    echo "   curl -sSL https://github.com/rust-lang/mdBook/releases/download/v0.4.40/mdbook-v0.4.40-x86_64-unknown-linux-gnu.tar.gz | tar -xz && mv mdbook ~/.local/bin/"
    exit 1
fi

if [[ "${1:-}" == "serve" ]]; then
    echo "🚀 Starting mdBook dev server (live-reload) ..."
    mdbook serve --open
else
    echo "📖 Building mdBook ..."
    mdbook build
    echo "✅ Done! Output is in the book/ directory."
fi
