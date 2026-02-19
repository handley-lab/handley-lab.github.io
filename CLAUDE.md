# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Handley Research Group website — a Jekyll (4.4, minima theme) GitHub Pages site for the University of Cambridge research group. Content (blog posts, homepage, images) is generated using Google Gemini API. Group member data is managed as structured YAML.

**Domain:** handley-lab.co.uk | **Deploy:** push to `main` triggers GitHub Pages rebuild.

## Essential Commands

```bash
script/bootstrap          # Install Ruby dependencies (bundler + gems)
script/server             # Start local dev server (bundle exec jekyll serve)
script/build              # Build site to _site/
script/cibuild            # Build + validate _site/index.html exists
script/calculate          # Regenerate group timeline.py + html_table.py
```

### Content Generation (requires `GEMINI_API_KEY`)

```bash
python script/posts/arxiv.py <arxiv_id>   # Generate blog post from arXiv paper
python script/index.py                      # Regenerate homepage content
python script/background.py                 # Regenerate landing page background image
```

## Architecture

### Content Generation Pipeline

`script/posts/arxiv.py` is the primary content pipeline:
1. Fetches paper metadata from arXiv API (feedparser) and LaTeX source from arxiv.org/src/
2. Cross-references authors against `assets/group/group.yaml` using surname matching
3. Calls Gemini (`gemini-2.5-pro`) to generate blog post narrative
4. Calls Imagen (`imagen-4.0-generate-001`) to generate accompanying image
5. Outputs: post in `_posts/YYYY-MM-DD-<arxiv_id>.md`, image in `assets/images/posts/`, prompts saved to `prompts/content/` and `prompts/images/` for reproducibility

Posts are generated on demand (not automated) and require human review before committing.

### Group Data System

**Single source of truth:** `assets/group/group.yaml`

```yaml
Person Name:
  role_type:                    # pi, coi, postdoc, phd, mphil, partiii, summer
    start: YYYY-MM-DD
    end: YYYY-MM-DD            # null = current member
    supervisors: [list]
    thesis: "Title"
  image: path/to/image.jpg
  links:
    Description: URL
  destination:
    YYYY-MM-DD: Position       # Post-group career tracking
```

**Processing pipeline:**
- `assets/group/group.py` — Python classes (`Student`, `Level`) that load YAML, sort by seniority then date, and re-serialize. Seniority: PI/Co-I (-1) > PostDoc (0) > PhD (1) > MPhil (2) > PartIII (3) > Summer (4)
- `assets/group/html_table.py` — Generates `assets/group/group.html` (responsive grid via yattag), separating current vs past members
- `assets/group/timeline.py` — Generates `assets/group/group.png` (matplotlib Gantt chart)

**Workflow to add a member:** edit `group.yaml` → add photo to `assets/group/images/originals/` → run `script/calculate`

### Jekyll Layouts

| Layout | Purpose |
|--------|---------|
| `base.html` | Root HTML shell (all others inherit from this) |
| `landing.html` | Homepage — hero section + panel grid, reads from `_data/*.yml` |
| `home.html` | Blog listing with pagination |
| `post.html` | Individual post with MathJax support |
| `group.html` | Embeds generated `assets/group/group.html` via `include_relative` |
| `page.html` | Generic page |

### Data Files (`_data/`)

- `science.yml` — Research themes displayed on science page and landing panels
- `case_studies.yml` — Case studies with evidence links and status
- `skills.yml` — Skills marketplace entries

### Styling

Customized minima theme (classic skin). Key overrides in `_sass/minima/custom-styles.scss`:
- Fonts: EB Garamond (headings), Crimson Pro (body), IBM Plex Mono (code) — loaded in `_includes/custom-head.html`
- Color palette: dark teal accent (`#133844`), cyan highlight (`#00bdb6`), off-white panels
- Sticky nav with backdrop blur, animated panel cards, responsive 3→2→1 column grid

### Key Excluded Files

`_config.yml` excludes from build: `CLAUDE.md`, `script/`, `venv/`, `requirements.txt`, `README.md`
