---
name: website
description: Work on the handley-lab.github.io Jekyll site — bootstrap, serve, build, edit data files, add an AI Cookbook recipe (card and optional companion page), commit on a feature branch and open a PR.
allowed-tools: []
---

# Website skill

Use this skill when working inside `handley-lab.github.io`. It encodes the site conventions from [`CLAUDE.md`](../../CLAUDE.md) and the workflow for adding cookbook recipes and other content.

## When to use

- The user wants to add or edit content on the site.
- The user wants to preview their changes locally.
- The user wants to publish a recipe (card and optional long-form companion page).
- A `recipe` skill (or other content skill) hands off a draft for preview.

## Bootstrap

Once per machine:

```bash
script/bootstrap            # gem install bundler && bundle install
```

## Local preview

```bash
script/server               # bundle exec jekyll serve, http://127.0.0.1:4000
```

Live-reload picks up edits to `*.md`, `_data/*.yml`, `_layouts/*.html`, `_includes/*.html`, and collection files in `_recipes/`.

## Build check

Before committing:

```bash
script/build                # bundle exec jekyll build → _site/
```

If you've touched anything that could expose `skills/`, also run the leak checks. The repo intentionally has both a public `skills.md` page (which publishes to `/skills/`) and a private `skills/` source directory (excluded from build). The combination is subtle — these checks make the distinction explicit:

```bash
# Public marketplace page must exist.
test -f _site/skills/index.html
# Raw skill files must NOT leak.
test ! -e _site/skills/website
test ! -e _site/skills/recipe
test ! -e _site/skills/README.md
# Anything else under _site/skills/ besides index.html and built assets is a leak.
find _site/skills -mindepth 1 ! -name index.html ! -name '*.css' ! -name '*.js' -print
```

The final `find` should print nothing.

```bash
script/cibuild              # builds, asserts _site/index.html exists, then deletes _site
```

If `script/cibuild` exits 0 (printing "It builds!"), the site builds.

## The AI Cookbook content model

Two surfaces:

- **`_data/recipes.yml`** — the list of recipe cards displayed at `/cookbook/`. Every recipe has a card here.
- **`_recipes/<id>.md`** — optional companion page rendered at `/cookbook/<id>/`. Adds a "Read full recipe" link to the card.

Card-only entries are valid. Length is a property of the recipe; some recipes are 3–4 minute reads with no companion page, others have a longer write-up worth linking out to.

## Adding or editing a recipe card

Recipe cards live only in `_data/recipes.yml`. They do not require a file in `_recipes/`.

```yaml
- id: <id>
  title: "..."                           # plain descriptive — say what it is, not how clever it is
  category: "..."                        # e.g. Context Engineering, Research Communication
  timebox: "..."                         # e.g. 10 minutes, one afternoon, multi-session
  status: "Draft"                        # Stub | Draft | In progress | Complete
  proposer: "..."                        # optional; useful for workshop attribution
  summary: "..."                         # 1–2 sentences. Lead with what became possible, not what was efficient.
  outcome: "..."                         # required, must be non-empty (Stub: ... is acceptable)
  evidence: "..."                        # required, must be non-empty (Stub: ... is acceptable)
  demo_url:
  repo_url: "..."
```

During the 5 May 2026 workshop and any successor workshop, prefer posting recipe-card YAML to the coordination issue for orchestrator batch-merge rather than opening many competing PRs against `_data/recipes.yml` — the file is a merge-conflict magnet under parallel edits.

## Adding a long-form companion page for a recipe

A long-form recipe has **two halves** that must stay in sync:

1. **Card** — an entry in `_data/recipes.yml`. Renders on `/cookbook/` and the homepage preview block.
2. **Companion page** — a file at `_recipes/<id>.md`. Renders at `/cookbook/<id>/`.

The card include (`_includes/recipe_card.html`) discovers a matching companion page by collection `slug` — Jekyll auto-derives `slug` from the filename. **So `<id>` (the card field, the companion page's frontmatter `id`, and the filename) must all agree.** Otherwise the "Read full recipe" link won't appear.

### Step 1 — Pick `<id>` and check it's unused

- kebab-case (e.g. `jaxwavelets`, `gw-emulator`, `cosmosis-cobaya-port`).
- Unique across all three places it must agree (filename, card `id`, companion frontmatter `id`).

Scripted check (run with your chosen `<id>`):

```bash
id="<id>"
fail=0

# 1. Card id must not exist in _data/recipes.yml
if grep -nE "^- id: ${id}\$" _data/recipes.yml; then
  echo "ERROR: _data/recipes.yml already has id: ${id}"; fail=1
fi

# 2. Companion filename must not exist
if test -e "_recipes/${id}.md"; then
  echo "ERROR: _recipes/${id}.md already exists"; fail=1
fi

# 3. Companion frontmatter id must not exist under another filename
if grep -RsnE "^id: ${id}\$" _recipes; then
  echo "ERROR: another _recipes/*.md already has id: ${id}"; fail=1
fi

[ "$fail" = 0 ] && echo "OK: ${id} is free"
```

If any check fails, pick a different id. Don't overwrite.

### Step 2 — Create the feature branch

```bash
git checkout -b recipe/<id>
```

Branch first, then write — uncommitted changes carry across, but it's cleaner to bound your edits to the branch from the start. Never push directly to `main`.

### Step 3 — Write `_recipes/<id>.md`

Frontmatter must include the full card schema (so the page is self-documenting and the layout has the data it needs):

```yaml
---
id: <id>
title: "..."
category: "..."
timebox: "..."
status: "Draft"            # Stub | Draft | In progress | Complete
summary: "..."
outcome: "..."
evidence: "..."
demo_url:                  # optional; leave the field with no value or omit entirely
repo_url: "..."            # optional
author: "..."
date: YYYY-MM-DD
---
```

`status` accepts `"Stub"`, `"Draft"`, `"In progress"`, or `"Complete"`. `outcome` and `evidence` must be non-empty (for stubs, lead with `Stub: ...` rather than leaving blank).

Then the long-form body. **Do not write a leading body H1** — `_layouts/recipe.html` renders `{{ page.title }}` as the H1. Start the body with `## Section`.

Use [`_recipes/jaxwavelets.md`](../../_recipes/jaxwavelets.md) as the reference template (with the caveat that its execution was critiqued at the 5 May 2026 workshop as too long and too dense — favour 3–4 minute reads with a Methods note for forensic detail).

### Step 4 — Append a matching card to `_data/recipes.yml`

```yaml
- id: <id>                              # MUST match _recipes/<id>.md
  title: "..."
  category: "..."
  timebox: "..."
  status: "..."
  summary: "..."
  outcome: "..."                        # required, must be non-empty
  evidence: "..."                       # required, must be non-empty
  demo_url:
  repo_url: "..."
```

Don't ship empty `outcome` or `evidence`. If you can't write them, the recipe isn't ready to publish.

### Step 5 — Preview

`script/server` (or refresh the running server). Visit:

- `/cookbook/<id>/` — the companion page renders with frontmatter title as H1, MathJax loaded if needed.
- `/cookbook/` — the new card appears with a working "Read full recipe" link.
- `/` — homepage preview block reflects the change if `<id>` is in the first three cards.

### Step 6 — Build check + commit

```bash
script/cibuild                          # exits 0 if all good
git add _recipes/<id>.md _data/recipes.yml
git commit -m "Add <id> recipe"
git push -u origin recipe/<id>
gh pr create                            # or open the PR in the GitHub web UI if gh isn't authenticated
```

## Files this skill MUST NOT modify without explicit user OK

- `_posts/` — currently being audited; new posts go through PR review (see Papers below).
- `assets/group/group.yaml` — managed via `script/calculate`.
- `_config.yml` — site-wide config; needs explicit user OK.
- `script/*` — build scripts; needs explicit user OK.

## Papers (`_posts/`)

The `_posts/` directory historically held auto-generated arXiv summaries from `script/posts/arxiv.py`. As of 5 May 2026 these are being audited: nothing in `_posts/` should be assumed to be human-reviewed, and the `/papers/` page is being rebuilt to surface only PR-reviewed entries. When in doubt, do not add to `_posts/` directly — open a PR and request human review.

## Common failure modes

- **"Read full recipe" link missing**: filename slug doesn't match the card's `id`. Verify `_recipes/<id>.md` exists and the card has `id: <id>`.
- **Duplicate H1 on the page**: the body starts with `# ...`. Strip it; the layout adds the H1 from `{{ page.title }}`.
- **Empty "Outcome:" / "Evidence:" labels**: card fields are `""`. Populate them; the recipe isn't ready to publish without them.
- **Build fails after editing `_config.yml`**: collection or default scope syntax error. The current collection is `recipes` (lowercase) with `permalink: /cookbook/:path/`.
