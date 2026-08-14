#!/usr/bin/env bash
# Rebuild the public/ deploy folder from source files and deploy to Cloudflare Pages.
# Only the files listed here go live — never deploy the repo root directly
# (it contains PUBLISH.md, references/, and other files that must stay private).
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf public
mkdir -p public/.well-known public/critical-ai-health-literacy

cp index.html og-image.png critical-ai-health-literacy.zip public/
cp critical-ai-health-literacy/SKILL.md public/critical-ai-health-literacy/
cp site/_headers site/robots.txt site/404.html public/
cp site/security.txt public/.well-known/security.txt

npx wrangler pages deploy public --project-name caihl --commit-dirty=true
