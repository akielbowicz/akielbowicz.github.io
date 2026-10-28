#!/usr/bin/env bash
# Regenerate out/2cents.pdf from cv/2cents.md
# 2 landscape A4 pages, 2 columns each via column-count CSS.
# Structure comes from <div class="slide"> blocks inside the markdown.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SRC="cv/2cents.md"
OUT="out/2cents.pdf"
CSS="scripts/slides.css"

pandoc "$SRC" \
  --standalone \
  --from markdown+raw_html \
  --css "$CSS" \
  -t html5 \
  -o /tmp/2cents.html

weasyprint -u "file://$ROOT/" -s "$CSS" /tmp/2cents.html "$OUT"

echo "✓ $OUT"
# Copy to dist/cv/ for GitHub Pages
mkdir -p "$ROOT/dist/cv"
cp "$OUT" "$ROOT/dist/cv/2cents.pdf"

