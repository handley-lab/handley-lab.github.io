---
name: paper
description: Draft a paper-summary post for /papers/ via a pull request. Pulls arXiv metadata, scaffolds a short post that links prominently to the published paper, leaves space for the lab-author to add the AI-assisted context, and opens a PR for human review. Never publishes directly. Iterating from a baseline; expect this skill to evolve.
allowed-tools: []
---

# Paper skill

Use this skill to add a paper-summary post to `/papers/` on `handley-lab.github.io`. The output is a markdown file in `_posts/` accompanied by a PR for human review. **This skill never publishes to `main` directly** — every paper post must be reviewed by a human (ideally not the paper's lead author) before merge.

This skill is a baseline produced during the 5 May 2026 workshop. Treat it as iterating: improve it as part of the PR for the first paper post written through it.

## When to use

- A lab paper has been submitted or published on arXiv and the author wants a `/papers/` post.
- You're demonstrating the new PR-driven paper workflow (rather than the old `script/posts/arxiv.py` auto-publish pipeline).

## What this skill replaces

The repository contains `script/posts/arxiv.py`, an auto-generation pipeline that produced ~88 posts directly to `_posts/` without human review. As of the 5 May 2026 workshop, that approach is being phased out: the auto-generated backlog is being purged and new posts go through this skill (PR + human review). Do not call `script/posts/arxiv.py` from this workflow.

## Inputs

- The arXiv ID (e.g. `2603.26644`).
- Optional: a sentence or two from the lab author about *what was hard, what tool helped, what became possible* — the differentiator that makes a `/papers/` post more than a paper summary.

If the lab author isn't available now, leave the AI-assisted context as a `TODO:` block; the PR review is where it gets filled in.

## Workflow

### Step 1 — Confirm the arXiv ID and check for prior post

```bash
arxiv="<arxiv-id>"
# 1. No existing post?
ls _posts/*${arxiv}* 2>/dev/null && echo "ERROR: existing post for ${arxiv}"
# 2. Paper exists on arXiv?
curl -s "https://export.arxiv.org/api/query?id_list=${arxiv}" | grep -E "<title>|<summary>" | head
```

If the paper is paywalled-but-not-on-arXiv, this skill doesn't apply directly — write the post by hand and open a PR.

### Step 2 — Pull metadata

Use the arxiv MCP if available:

```text
mcp__arxiv__search query=<arxiv-id>
# or
mcp__arxiv__download arxiv_id=<arxiv-id>  # only if the LaTeX source helps
```

Otherwise the arXiv API directly:

```bash
curl -s "https://export.arxiv.org/api/query?id_list=${arxiv}" > /tmp/paper-${arxiv}.atom
```

Capture: `title`, `authors`, `published`, `abstract`, `arxiv_id`, optionally a primary category. Identify which authors are lab members by cross-referencing `assets/group/group.yaml` on surname.

### Step 3 — Branch

```bash
git checkout main
git pull
git checkout -b paper/<arxiv-id>
```

### Step 4 — Scaffold the post

Create `_posts/YYYY-MM-DD-<arxiv-id>.md` (the date is the arXiv submission date, *not* the post date) using this minimal scaffold:

```markdown
---
layout: post
title: "<exact paper title>"
date: YYYY-MM-DD
categories: papers
arxiv: <arxiv-id>
authors: ["<lab member 1>", "<lab member 2>", ...]
---

By <list lab authors with links to their pages> with <co-authors>.

## What the paper does

<2–4 sentences. The scientific result, not a press release. Lead with the question, end with the answer. No "groundbreaking", no "novel".>

## How AI helped (or didn't)

<2–4 sentences from the lab author. What tool, what pattern, what became possible. If the answer is "it didn't, this was done by hand" — say so honestly. This section is the reason for the post; without it the arXiv abstract would suffice.

If a recipe in /cookbook/ matches the workflow used, link it.>

## Read

- [Paper on arXiv](https://arxiv.org/abs/<arxiv-id>)
- [Repository](TODO or omit)
- Related recipe: [<title>](/cookbook/<id>/) (TODO or omit)
```

The `arxiv:` frontmatter field is **load-bearing**: `_layouts/post.html` reads it and renders a clickable arXiv badge near the top, plus auto-includes the first-page screenshot (see Step 5) as a figure. **Do not** repeat the arXiv link in the first body line — the badge handles it.

### Tone constraints

- **Plain descriptive titles** — exactly the paper's. No clever rewrites.
- **No press-release language**. "Groundbreaking", "revolutionary", "exciting new" — out. "We show that …" — in.
- **No AI-generated text in the body**. The post can be drafted with AI assistance but the words shipped to `main` should have been read and chosen by a human. The "How AI helped" section is the only place the AI lives in the post; it lives as a description, not as the writer.
- **Length**: 200–500 words is plenty. The paper itself is the long-form artefact; the post is the human-flavoured pointer to it.

### Step 5 — First-page screenshot (auto-included if present)

The post layout auto-includes `assets/images/papers/<arxiv-id>.png` as a figure if the file exists. Generate it from the paper PDF:

```bash
# Download the PDF (skip if already on disk)
curl -sL "https://arxiv.org/pdf/<arxiv-id>" -o /tmp/<arxiv-id>.pdf
# Or via the arxiv MCP if available:
# mcp__arxiv__download arxiv_id=<arxiv-id> format=pdf output_path=/tmp/<arxiv-id>.pdf

# Render page 1 at 150 DPI; pdftoppm produces firstpage-01.png
pdftoppm -png -f 1 -l 1 -r 150 /tmp/<arxiv-id>.pdf /tmp/firstpage
mv /tmp/firstpage-01.png assets/images/papers/<arxiv-id>.png
```

This is a *screenshot*, not an illustration. Do **not** generate a synthetic "AI illustration" of the paper; the legacy auto-pipeline did that and the room rejected it as slop.

If you want to add a *substantive* internal figure (a key plot, a method diagram), do so in the body markdown with a normal `![alt](/assets/images/papers/<arxiv-id>-figure-<n>.png)`. Keep these to figures that are actually load-bearing for the post; readers can find decorative ones in the paper.

### Step 6 — Build, preview, PR

```bash
script/cibuild
git add _posts/YYYY-MM-DD-<arxiv-id>.md
# add image if any
git commit -m "Add paper post for arXiv:<arxiv-id>"
git push -u origin paper/<arxiv-id>

gh pr create \
  --title "Paper post: arXiv:<arxiv-id>" \
  --body "Refs paper-skill iteration. Reviewer should not be the paper's lead author."
```

### Step 7 — Review

Reviewer responsibilities (must NOT be the paper's lead author, ideally a co-author or an unrelated lab member):

- Title is the paper's exact title.
- The arXiv link is in the first line of the body.
- "What the paper does" is plain English with no marketing language.
- "How AI helped" is honest — including "didn't help" if that's true.
- No AI-generated illustration.
- Word count under ~500.

Approve or request changes. Merge squash; auto-delete branch.

## Files this skill MUST NOT modify

- `_posts/` outside the new file for this paper.
- `assets/images/posts/` (legacy auto-pipeline directory; new posts use `assets/images/papers/`).
- `_data/recipes.yml` and `_recipes/`.
- `_config.yml`, `script/*`, `assets/group/group.yaml`.

## Open questions to resolve via iteration

This skill was written quickly during a workshop. Things that should improve as it gets used:

- Should there be a `_data/papers.yml` for richer indexing on `/papers/` (tags, year, area), or do post frontmatter `categories` + `tags` suffice?
- Should the `/papers/` index get the same card treatment as `/cookbook/` rather than the current `home.html`-driven post listing?
- Should there be cross-linking between papers and the recipes that produced them?
- Should the lab author *always* be invited to write the "How AI helped" section, or is it acceptable for a co-author or the orchestrator to draft it for them to edit?
- Does the existing `script/posts/arxiv.py` get rewritten as a Phase-0 metadata helper for this skill, or deleted entirely?

When iterating: open a PR against this skill, not a parallel skill.
