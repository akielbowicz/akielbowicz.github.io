#!/usr/bin/env bash
# Regenerate out/2cents.pdf from cv/2cents.md
# 2 landscape A4 pages, 2 columns each, IBM Plex Mono, white bg.
# Structure comes from <div class="slide"> blocks inside the markdown.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT="out/2cents.pdf"
CSS="scripts/slides.css"

# Ensure output directory exists
mkdir -p out dist/cv

# Generate HTML from cv/2cents.md using pandoc
pandoc cv/2cents.md \
  --standalone \
  --from markdown+raw_html \
  --css "$CSS" \
  -t html5 \
  -o /tmp/2cents.html

# Generate PDF using weasyprint (via uvx, so it works in CI without pre-install)
uvx --from weasyprint weasyprint -u "file://$ROOT/" -s "$CSS" /tmp/2cents.html "$OUT"

# Copy to dist/cv/ for GitHub Pages
cp "$OUT" dist/cv/2cents.pdf

echo "✓ $OUT"