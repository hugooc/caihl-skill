# PUBLISH.md — Handoff plan for Claude Code

> **Status (as of 2026-06-04):** Launch is complete and the repo is now PUBLIC
> at https://github.com/hugooc/caihl-skill. The site is live at https://caihl.org
> and Vadim's first review has been applied. This document is kept as a
> historical record of the launch-night plan. For ongoing redeploys, the
> relevant command is `wrangler pages deploy . --project-name caihl`.

## Goal
- **Tonight:** private GitHub repo + live static site at **https://caihl.org** (Cloudflare).
- **Later** (after Hugo talks to Vadim and Liz): flip the repo to public.

## What's in this folder
- `index.html` — the landing page (static, self-contained, no external dependencies)
- `critical-ai-health-literacy/SKILL.md` — the skill itself
- `critical-ai-health-literacy.zip` — the downloadable package the page links to
- `README.md`, `LICENSE`

## Decisions already made
- Repo visibility: **PRIVATE for now.**
- Host: **Cloudflare.** Domain **caihl.org** (Hugo owns it, DNS already on Cloudflare).
- Deploy method: **Cloudflare Pages.**

## Credentials you (Hugo) handle yourself — browser logins
- GitHub: `gh auth login`
- Cloudflare: `wrangler login` (or a scoped API token)
- Claude Code will not enter these for you. It will pause and ask you to log in.

---

## Step 1 — Create the private GitHub repo
From this folder:
```bash
gh auth status                                      # confirm you're logged in
gh repo create caihl-skill --private --source=. --push
```
Then grab your username and fix the placeholder in the page:
```bash
gh api user -q .login                               # prints your GitHub handle
```
Replace `<your-username>` in `index.html` (the git clone block) with `<handle>/caihl-skill`.

> **Heads-up:** while the repo is private, the "git clone" install instructions on the live
> site will 404 for the public. The **zip download still works for everyone.** See Step 4.

## Step 2 — Deploy the site to Cloudflare Pages
Fastest path for tonight is a direct Wrangler upload. No Git connection needed, works fine
with a private repo:
```bash
npm i -g wrangler                                   # if not already installed
wrangler login
wrangler pages project create caihl --production-branch main
wrangler pages deploy . --project-name caihl
```
This serves `index.html` at a `*.pages.dev` URL. `.git` is ignored automatically.
Confirm the page loads and the zip downloads from the `.pages.dev` link before wiring the domain.

> **Alternative (nicer long-term):** connect the GitHub repo in the Cloudflare dashboard so it
> auto-deploys on every push. Slower to set up tonight. Your call.

## Step 3 — Point caihl.org at it
caihl.org's DNS is already on Cloudflare, so this is quick:
- Dashboard: **Pages → project "caihl" → Custom domains → Set up a custom domain** → add
  `caihl.org` and `www.caihl.org`. Cloudflare auto-creates the DNS records.
- Or script it with the Cloudflare API if you give Claude Code a scoped token.
Wait for the TLS cert to issue (usually a couple minutes), then load **https://caihl.org**.

## Step 4 — Pre-public cleanup (recommended tonight)
- Comment out or remove the **"Claude Code / git clone"** section in `index.html` so the live
  site doesn't show install steps that 404 while the repo is private.
- Keep the **zip download** as the primary install path for now.
- Redeploy after editing: `wrangler pages deploy . --project-name caihl`

## Step 5 — Verify
- https://caihl.org loads over HTTPS
- The download button delivers `critical-ai-health-literacy.zip`
- Page renders cleanly on mobile

---

## When you're ready to go public (after Vadim + Liz)
```bash
gh repo edit <handle>/caihl-skill --visibility public
```
Then restore the git clone section in `index.html`, set the real repo URL, and redeploy:
```bash
wrangler pages deploy . --project-name caihl
```

---

## Paste this into Claude Code to start
> I'm in the CAIHL skill repo. Do three things:
> 1. Create a **private** GitHub repo called `caihl-skill` from this folder and push it.
> 2. Before deploying, comment out the "Claude Code / git clone" section in `index.html`
>    (the repo is private for now) and replace `<your-username>` with my real handle.
> 3. Deploy this folder as a static site to **Cloudflare Pages** (project name `caihl`) and
>    attach my domain **caihl.org**, which is already on Cloudflare.
>
> Pause and walk me through any GitHub or Cloudflare browser logins. When done, verify
> https://caihl.org loads over HTTPS and the zip download works.
