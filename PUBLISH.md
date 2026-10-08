# Publishing and deployment

## Current state

- Public repository: https://github.com/hugooc/caihl-skill
- Live site: https://caihl.org/
- Host: Cloudflare Pages
- Cloudflare project: `caihl`
- Canonical site sources: `index.html`, `og-image.png`, `critical-ai-health-literacy.zip`, `critical-ai-health-literacy/SKILL.md`, and `site/`
- Generated deployment bundle: `public/`

## Safety rule

**Never run `wrangler pages deploy .` from the repository root.** The repository contains private working material, including ignored files under `references/`. Deploy only the allowlisted bundle produced by `scripts/deploy.sh`.

## Before deploying

1. Review the canonical source files, not the generated copies in `public/`.
2. If `critical-ai-health-literacy/SKILL.md` changed, make sure `critical-ai-health-literacy.zip` contains the current skill.
3. If the social image changed, regenerate or replace `og-image.png` and inspect it.
4. Confirm `site/_headers`, `site/robots.txt`, `site/404.html`, and `site/security.txt` are current.
5. Check `git status` so unrelated or private work is not mistaken for public content.

## Deploy

From the repository root, run:

```bash
./scripts/deploy.sh
```

The script deletes and rebuilds `public/`, copies only the approved public assets, and deploys that folder to the `caihl` Cloudflare Pages project. A Cloudflare login or scoped token may be required.

## Verify after deployment

- https://caihl.org/ loads over HTTPS.
- The page renders cleanly on desktop and mobile.
- The skill download returns `critical-ai-health-literacy.zip`.
- The linked public `SKILL.md` is current.
- `robots.txt`, the custom 404 page, security headers, and `/.well-known/security.txt` are available.
- No README, publishing notes, research references, curriculum sources, or other working files are publicly accessible.

## Historical appendix

The site was launched in June 2026. The repository began as private and was later made public after review. The original launch-night checklist covered repository creation, Cloudflare setup, custom-domain attachment, and the transition to public visibility; those one-time steps are complete.

On June 10, deploying the repository root exposed files that were never intended for the public site, including private reference texts. The deployment workflow was changed to use an explicit allowlist: `scripts/deploy.sh` now rebuilds `public/` and deploys only that bundle. This is why the safety rule above is mandatory.

## Starter kit subdomain (added October 7, 2026)

- Live: https://kit.caihl.org/ (custom domain attached, CNAME `kit` -> `caihl-kit.pages.dev`)
- Cloudflare project: `caihl-kit`, separate from `caihl`. Connected to GitHub `hugooc/caihl-skill`, production branch `main`, no build command, output directory `kit`.
- **A push to `main` deploys the kit automatically.** This is different from caihl.org itself, which is still direct upload via `scripts/deploy.sh`. Nothing outside `kit/` is served by `caihl-kit`.
- Sources: `kit/` (index.html, starter-folder.zip, quick-start.pdf, _headers, robots.txt, 404.html). The working copy and build scripts live in `_Documents WORK/2026-09-29__BUILD__Patient-Directed-AI-Record-Turnkey-Kit/`; `kit/` is the deploy copy.
- `scripts/deploy-kit.sh` is a manual fallback (direct upload to the same project). Normally unnecessary.
- The kit's `_headers` allows one inline script by SHA-256 hash (the text-size control). If `kit/index.html` changes, recompute the hash or the buttons will stop working.
