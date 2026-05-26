# Skills (in-repo)

These skills live inside the website source so anyone who clones the repo can point Claude Code at them. They are **not** published — `_config.yml` excludes the `skills/` directory from the Jekyll build.

> If you're a workshop attendee: clone this repo, then start Claude Code from inside it. The `CLAUDE.md` at the repo root tells Claude where to find these skills. You can also point Claude explicitly via `claude --add-dir skills/` if needed.

## Available skills

| Skill | What it does |
|---|---|
| [`website`](website/SKILL.md) | Build and serve the Jekyll site, edit `_data/*.yml`, add a long-form companion page to the `_recipes/` collection, commit on a feature branch and open a PR. |
| [`recipe`](recipe/SKILL.md) | Two paths: (a) interview-driven short recipe card; (b) forensic long-form recipe — discover a past Claude Code session (no UUID required), analyse its JSONL with a 5-minute-cap pair-timing methodology (see [`methodology.md`](recipe/methodology.md)), and emit a draft matching the [jaxwavelets exemplar](../_recipes/jaxwavelets.md) into a [`template`](recipe/template.md). Hands off to the `website` skill to preview. |
| [`paper`](paper/SKILL.md) | Draft a paper-summary post for `/papers/` from an arXiv ID. Pulls metadata, scaffolds a short post that links prominently to the published paper, leaves space for the lab-author to add the AI-assisted context, and opens a PR for human review. Replaces the auto-publish `script/posts/arxiv.py` workflow. Baseline; iterate on it as it gets used. |
| [`meeting-case-study`](meeting-case-study/SKILL.md) | Sibling of `recipe` but for live-meeting capture rather than Claude Code session forensics. Monitors an Otter transcript (live or post-hoc), synthesises a LaTeX/PDF report via OpenAI, applies a styling preamble (default matplotlib `tab10`, or pulled from email via `tex-style-from-email`), anonymises under Chatham House conventions, creates a private group repo with verbatim transcripts, and emits a `_recipes/<id>.md` case study. Reference run: [thesis-writing-workshop](https://github.com/handley-lab/thesis-writing-workshop). |

## Conventions

- A long-form companion page lives at `_recipes/<id>.md` and is rendered at `/cookbook/<id>/`.
- The matching card is a row in `_data/recipes.yml` whose `id:` field equals `<id>` (and matches the filename).
- The card include (`_includes/recipe_card.html`) finds companion pages by collection `slug`, which Jekyll auto-derives from filename — so the filename, the card `id`, and the collection-page frontmatter `id` must all agree.
- Cards have a strict schema: `id`, `title`, `category`, `timebox`, `status`, `summary`, `outcome`, `evidence`, optional `proposer`, `demo_url`, `repo_url`. **`outcome` and `evidence` must be non-empty** for published cards — they're surfaced as labelled rows in the card UI. For workshop stubs, `Stub: ...` is acceptable.

See repo-root [`CLAUDE.md`](../CLAUDE.md) for site conventions and [the jaxwavelets recipe](../_recipes/jaxwavelets.md) as the reference template.
