# Skills (in-repo)

These skills live inside the website source so anyone who clones the repo can point Claude Code at them. They are **not** published — `_config.yml` excludes the `skills/` directory from the Jekyll build.

> If you're a workshop attendee: clone this repo, then start Claude Code from inside it. The `CLAUDE.md` at the repo root tells Claude where to find these skills. You can also point Claude explicitly via `claude --add-dir skills/` if needed.

## Available skills

| Skill | Status | What it does |
|---|---|---|
| [`website`](website/SKILL.md) | Available | Build and serve the Jekyll site, edit `_data/*.yml`, add a long-form page to the `_case_studies/` collection, commit on a feature branch and open a PR. |
| `case-study` | Coming | Discover one of your past Claude Code sessions (no UUID required), analyse its JSONL with a 5-minute-cap pair-timing methodology, and emit a draft long-form page + card matching the [jaxwavelets exemplar](../_case_studies/jaxwavelets.md). Hands off to the `website` skill to preview. |

## Conventions

- A long-form case study lives at `_case_studies/<id>.md` and is rendered at `/case-studies/<id>/`.
- The matching card is a row in `_data/case_studies.yml` whose `id:` field equals `<id>` (and matches the filename).
- The card include (`_includes/case_study_card.html`) finds long-form pages by collection `slug`, which Jekyll auto-derives from filename — so the filename, the card `id`, and the collection-page frontmatter `id` must all agree.
- Cards have a strict schema: `id`, `title`, `category`, `timebox`, `status`, `summary`, `outcome`, `evidence`, optional `demo_url`, `repo_url`. **`outcome` and `evidence` must be non-empty** for published cards — they're surfaced as labelled rows in the card UI.

See repo-root [`CLAUDE.md`](../CLAUDE.md) for site conventions and [the jaxwavelets case study](../_case_studies/jaxwavelets.md) as the reference template.
