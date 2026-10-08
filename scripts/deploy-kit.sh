#!/usr/bin/env bash
# Manual fallback deploy for the starter kit (kit/) to Cloudflare Pages project `caihl-kit`.
# Normally unnecessary: a push to `main` deploys kit/ automatically. Use this only if the
# GitHub connection is broken. Only kit/ goes live. Never deploy the repo root.
set -euo pipefail
cd "$(dirname "$0")/.."

required=(kit/index.html kit/message.txt kit/practice-document.pdf kit/_headers)
missing=0
for f in "${required[@]}"; do
  if [ ! -s "$f" ]; then
    echo "deploy-kit: missing or empty: $f" >&2
    missing=1
  fi
done
if [ "$missing" -ne 0 ]; then
  echo "deploy-kit: aborting, kit/ is incomplete." >&2
  exit 1
fi

# The CSP in kit/_headers pins the page's inline script by hash. Refuse to deploy a mismatch.
expected=$(python3 - <<'PY'
import re, hashlib, base64
s = open("kit/index.html").read()
m = re.search(r"<script>(.*?)</script>", s, re.S)
print("sha256-" + base64.b64encode(hashlib.sha256(m.group(1).encode()).digest()).decode())
PY
)
if ! grep -q "script-src '$expected'" kit/_headers; then
  echo "deploy-kit: kit/_headers script hash does not match kit/index.html." >&2
  echo "deploy-kit: expected $expected" >&2
  exit 1
fi

npx wrangler pages deploy kit --project-name caihl-kit --commit-dirty=true
