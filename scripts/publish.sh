#!/usr/bin/env bash
# Execute all notebooks in place, then render and publish the Quarto site
# to the gh-pages branch. Run this after any notebook edit that should be
# reflected on the published site.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

echo "Executing notebooks..."
find notebooks -name '*.ipynb' -print0 | xargs -0 jupyter nbconvert --to notebook --execute --inplace

echo "Publishing to GitHub Pages..."
quarto publish gh-pages --no-browser --no-prompt
