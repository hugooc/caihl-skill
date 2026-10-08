#!/usr/bin/env bash
# Deploy the Patient-Directed AI Record Starter Kit (kit/) to its own Cloudflare Pages
# project, separate from caihl.org. Only kit/ goes live. Never deploy the repo root.
# First-time setup (once, in the Cloudflare dashboard or with wrangler):
#   npx wrangler pages project create caihl-kit --production-branch main
#   then attach the custom domain kit.caihl.org under the project's Custom domains.
set -euo pipefail
cd "$(dirname "$0")/.."
test -f kit/index.html && test -f kit/starter-folder.zip && test -f kit/quick-start.pdf && test -f kit/_headers
npx wrangler pages deploy kit --project-name caihl-kit --commit-dirty=true
