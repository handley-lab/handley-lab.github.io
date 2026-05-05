---
name: website
description: Work on the handley-lab.github.io Jekyll site — bootstrap, serve, build, edit data files, add a long-form case study to the _case_studies collection, commit on a feature branch and open a PR.
allowed-tools: []
---

# Website skill

Use this skill when working inside `handley-lab.github.io`. It encodes the site conventions from [`CLAUDE.md`](../../CLAUDE.md) and the workflow for adding case studies.

## When to use

- The user wants to add or edit content on the site.
- The user wants to preview their changes locally.
- The user wants to publish a case study (long-form page + card).
- A case-study skill (or other content skill) hands off a draft for preview.

## Bootstrap

Once per machine:

```bash
script/bootstrap            # gem install bundler && bundle install
```

## Local preview

```bash
script/server               # bundle exec jekyll serve, http://127.0.0.1:4000
```

Live-reload picks up edits to `*.md`, `_data/*.yml`, `_layouts/*.html`, `_includes/*.html`, and collection files in `_case_studies/`.

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
test ! -e _site/skills/case-study
test ! -e _site/skills/README.md
# Anything else under _site/skills/ besides index.html and built assets is a leak.
find _site/skills -mindepth 1 ! -name index.html ! -name '*.css' ! -name '*.js' -print
```

The final `find` should print nothing.

```bash
script/cibuild              # builds, asserts _site/index.html exists, then deletes _site
```

If `script/cibuild` exits 0 (printing "It builds!"), the site builds.

## Two formats: recipe cards and long-form case studies

`_data/case_studies.yml` is a single data file with two formats:

- **Recipe cards** (`format: recipe`) — short browseable workflow patterns; card-only, no long-form page.
- **Long-form case studies** (`format: long-form`) — full audit trails; card plus a matching `_case_studies/<id>.md` page.

Missing `format` is rendered as `long-form` for backward compatibility, but new cards should set it explicitly.

`/case-studies/` renders both formats with a visual distinction. Recipe cards appear above long-form cards.

## Adding or editing a recipe card

Recipe cards live only in `_data/case_studies.yml`. They do not require a file in `_case_studies/`.

```yaml
- id: <id>
  format: recipe
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

During the 5 May 2026 workshop and any successor workshop, prefer posting recipe-card YAML to the coordination issue for orchestrator batch-merge rather than opening many competing PRs against `_data/case_studies.yml` — the file is a merge-conflict magnet under parallel edits.

## Adding a long-form case study

A long-form case study has **two halves** that must stay in sync:

1. **Card** — an entry in `_data/case_studies.yml` with `format: long-form`. Renders on `/case-studies/` and the homepage preview block.
2. **Long-form page** — a file at `_case_studies/<id>.md`. Renders at `/case-studies/<id>/`.

The card include (`_includes/case_study_card.html`) discovers a matching long-form page by collection `slug` — Jekyll auto-derives `slug` from the filename. **So `<id>` (the card field, the collection frontmatter field, and the filename) must all agree.** Otherwise the "Read long-form case study" link won't appear.

### Step 1 — Pick `<id>` and check it's unused

- kebab-case (e.g. `jaxwavelets`, `gw-emulator`, `cosmosis-cobaya-port`).
- Unique across all three places it must agree (filename, card `id`, collection frontmatter `id`).

Scripted check (run with your chosen `<id>`):

```bash
id="<id>"
fail=0

# 1. Card id must not exist in _data/case_studies.yml
if grep -nE "^- id: ${id}\$" _data/case_studies.yml; then
  echo "ERROR: _data/case_studies.yml already has id: ${id}"; fail=1
fi

# 2. Collection filename must not exist
if test -e "_case_studies/${id}.md"; then
  echo "ERROR: _case_studies/${id}.md already exists"; fail=1
fi

# 3. Collection frontmatter id must not exist under another filename
if grep -RsnE "^id: ${id}\$" _case_studies; then
  echo "ERROR: another _case_studies/*.md already has id: ${id}"; fail=1
fi

[ "$fail" = 0 ] && echo "OK: ${id} is free"
```

If any check fails, pick a different id. Don't overwrite.

### Step 2 — Create the feature branch

```bash
git checkout -b case-study/<id>
```

Branch first, then write — uncommitted changes carry across, but it's cleaner to bound your edits to the branch from the start. Never push directly to `main`.

### Step 3 — Write `_case_studies/<id>.md`

Frontmatter must include the full card schema (so the page is self-documenting and the layout has the data it needs):

```yaml
---
id: <id>
format: long-form
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

Then the long-form body. **Do not write a leading body H1** — `_layouts/case_study.html` renders `{{ page.title }}` as the H1. Start the body with `## Section`.

Use the [jaxwavelets case study](../../_case_studies/jaxwavelets.md) as the reference template.

### Step 4 — Append a matching card to `_data/case_studies.yml`

```yaml
- id: <id>                              # MUST match _case_studies/<id>.md
  format: long-form
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

Don't ship empty `outcome` or `evidence`. If you can't write them, the case study isn't ready to publish.

### Step 5 — Preview

`script/server` (or refresh the running server). Visit:

- `/case-studies/<id>/` — the long-form page renders with frontmatter title as H1, MathJax loaded if needed.
- `/case-studies/` — the new card appears with a working "Read more" link.
- `/` — homepage preview block reflects the change if `<id>` is in the first three cards.

### Step 6 — Build check + commit

```bash
script/cibuild                          # exits 0 if all good
git add _case_studies/<id>.md _data/case_studies.yml
git commit -m "Add <id> case study"
git push -u origin case-study/<id>
gh pr create                            # or open the PR in the GitHub web UI if gh isn't authenticated
```

## Editing a card without long-form

A card-only entry is the recipe-card format. Set `format: recipe`. No long-form page is required; the "Read long-form case study" link is conditional and will only appear if `_case_studies/<id>.md` exists.

## Files this skill MUST NOT modify without explicit user OK

- `_posts/` — driven by the `script/posts/arxiv.py` Gemini pipeline.
- `assets/group/group.yaml` — managed via `script/calculate`.
- `_config.yml` — site-wide config; needs explicit user OK.
- `script/*` — build scripts; needs explicit user OK.

## Common failure modes

- **"Read more" link missing**: filename slug doesn't match the card's `id`. Verify `_case_studies/<id>.md` exists and the card has `id: <id>`.
- **Duplicate H1 on the page**: the body starts with `# ...`. Strip it; the layout adds the H1 from `{{ page.title }}`.
- **Empty "Outcome:" / "Evidence:" labels**: card fields are `""`. Populate them; the case study isn't ready to publish without them.
- **Build fails after editing `_config.yml`**: collection or default scope syntax error. The current collection is `case_studies` (snake_case to satisfy Jekyll); the URL prefix is `/case-studies/` (kebab-case via `permalink`).
