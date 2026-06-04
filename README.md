# Critical AI Health Literacy (CAIHL) Skill

A Claude Skill that applies the **Critical AI Health Literacy** framework as an analytical lens to any topic where AI and health intersect.

Live site: **https://caihl.org/**

The framework comes from Hugo Campos and Liz Salmi's 2025 National Academy of Medicine commentary, *"Critical AI Health Literacy as Liberation Technology,"* which applies Paulo Freire's theory of critical literacy to health AI.

This is a "way of seeing," not a fixed output format. You control the output. The skill provides the lens.

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
git clone https://github.com/<your-username>/caihl-skill
mkdir -p ~/.claude/skills
cp -r caihl-skill/critical-ai-health-literacy ~/.claude/skills/
```

Then start a fresh session and run `/skills` to confirm it loaded.

## Structure

```text
critical-ai-health-literacy/
  SKILL.md                       # the skill itself
critical-ai-health-literacy.zip  # uploadable package the site links to
index.html                       # caihl.org landing page (static, self-contained)
og-image.png                     # Open Graph / Twitter card image
scripts/
  generate-og-image.py           # regenerates og-image.png
archive/                         # snapshots of prior index.html versions
PUBLISH.md                       # original launch-night handoff plan (historical)
README.md, LICENSE
```

## License

MIT. Attribution to Hugo Campos and Liz Salmi for the underlying framework is appreciated. The four-dimension frame for evaluating patient-facing AI is credited to Vadim Dukhanin et al.
