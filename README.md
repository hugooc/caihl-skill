# Critical AI Health Literacy (CAIHL)

This repository is the working home for the **Critical AI Health Literacy** framework, its installable AI skill, the public website at **https://caihl.org/**, and related private research and educational materials.

The framework comes from Hugo Campos and Liz Salmi's 2025 National Academy of Medicine commentary, *"Critical AI Health Literacy as Liberation Technology,"* which applies Paulo Freire's theory of critical literacy to health AI. It is a "way of seeing," not a fixed output format: the person using it controls the purpose and output; the framework provides the lens.

## What it does

Use it to analyze news, evaluate products, critique papers, or write content through a critical lens on topics like:

- Institutional vs patient-directed AI
- Algorithmic resistance and patient AI rights
- AI patients and liberation technology in healthcare
- Health AI bias and equity
- Ambient scribes, AI clinical notes, prior authorization AI, clinical decision support

Trigger it with prompts like "from a CAIHL perspective," "through the critical AI health literacy lens," "from a Freirean point of view," or "as an AI patient."

## Install

### Option A: Upload the zip (Claude apps)

1. Download [critical-ai-health-literacy.zip](critical-ai-health-literacy.zip)
2. In Claude, go to **Settings → Skills → Upload zip**
3. Ask something like: "Analyze this article from a CAIHL perspective."

### Option B: Claude Code (or any folder-based agent)

Clone or copy the skill folder into your skills directory:

```bash
git clone https://github.com/hugooc/caihl-skill
mkdir -p ~/.claude/skills
cp -r caihl-skill/critical-ai-health-literacy ~/.claude/skills/
```

Then start a fresh session and run `/skills` to confirm it loaded.

## Project map

```text
critical-ai-health-literacy/
  SKILL.md                       # canonical skill source
critical-ai-health-literacy.zip  # uploadable public skill package
index.html                       # canonical caihl.org landing page
og-image.png                     # canonical social-sharing image
site/                            # source for headers, robots, 404, and security.txt
scripts/
  deploy.sh                      # builds a safe public bundle and deploys it
  generate-og-image.py           # regenerates the social-sharing image
public/                          # generated deployment bundle; do not hand-edit
references/                      # private source texts; excluded from Git and deploys
output/
  curriculum/                    # editable educational materials
  pdf/                           # shareable PDF exports
tmp/                             # temporary render and quality-check files
PUBLISH.md                       # current deployment guide and historical notes
README.md                        # authoritative project orientation
LICENSE                          # MIT license
```

## Working conventions

- Treat `README.md` as the front door and update the project map when a durable folder or workflow is added.
- Edit canonical sources (`index.html`, `critical-ai-health-literacy/SKILL.md`, and `site/`), not generated files in `public/`.
- Keep source materials in `references/` private unless their rights and intended use have been reviewed. That folder is excluded from Git and from the public deployment bundle.
- Put editable teaching or research artifacts in a descriptive `output/` subfolder and their shareable exports in `output/pdf/`.
- Preserve provenance: distinguish framework source material, outside references, working analysis, and public-facing outputs.

## Publishing

Follow [PUBLISH.md](PUBLISH.md). The safe deployment command is:

```bash
./scripts/deploy.sh
```

The script rebuilds `public/` from an explicit allowlist and deploys only that generated bundle. **Never deploy the repository root**, because it contains private working material.

## License

MIT. Attribution to Hugo Campos and Liz Salmi for the underlying framework is appreciated. The four-dimension frame for evaluating patient-facing AI is credited to Vadim Dukhanin et al.
