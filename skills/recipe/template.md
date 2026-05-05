---
id: TODO-id
title: "TODO: a title that doesn't undersell the work and doesn't read like a press release"
category: "TODO: e.g. Rapid Development, Adversarial Review, Legacy Code Navigation, Context Engineering"
timebox: "TODO: e.g. 4.7 hours active computation, 8 hours, Multi-session"
status: "Draft"
summary: "TODO: 1–2 sentences. What was built/changed, against what reference, with what verification. Avoid productivity-boast framing."
outcome: "TODO: the concrete deliverable. Required, must be non-empty."
evidence: "TODO: how a sceptic could verify the claim — links, repos, test counts, review counts. Required, must be non-empty."
demo_url:
repo_url: "TODO: optional link to the artefact"
author: "TODO: full name + affiliation"
date: TODO-YYYY-MM-DD
---

<!--
  Long-form recipe template for _recipes/<id>.md.

  WARNING: collection-page frontmatter (above) is NOT automatically
  synced with _data/recipes.yml. The card and the long-form
  page have parallel schemas; you must keep id / title / summary /
  outcome / evidence in sync manually (or via the website skill's
  publish step).

  See ../website/SKILL.md for the publish workflow.
  See ../../_recipes/jaxwavelets.md for a worked example.

  Replace every TODO marker before publishing.
  Do NOT write a leading body H1 — the layout renders {{ page.title }}.
-->

## Abstract

TODO: 4–6 sentences. Lead with the intellectual hook (the *idea* the case study is making), not the numbers. Reference the embodied-intelligence pattern, the adversarial-review pattern, or the project's own equivalent. Include the strongest single number with one explanatory phrase ("effectively machine precision for these comparisons"). End with the implicit claim the case study is making — what would a sceptic learn?

## 1. Motivation

TODO: Why does this case study exist? What was the underlying scientific or software problem? If you're porting/extending a mature library, this is where the *embodied intelligence* idea goes — what decades of accumulated decisions are being preserved, and why faithful translation is the right framing.

If the project is novel rather than a port, name a different intellectual hook here — and don't pretend it was a port if it wasn't.

## 2. Principles

TODO: name 2–4 principles that emerged from this session. For each, write a section explaining what the principle means *for this project specifically*. Don't import the jaxwavelets principles wholesale unless they actually apply.

Examples (replace, don't reuse):

### 2.1 [Principle 1 name]

TODO

### 2.2 [Principle 2 name]

TODO

### 2.3 [Principle 3 name]

TODO

## 3. What Required Human Intervention

TODO: the credibility check. List 3–6 decisions where the AI's first answer was wrong, or where no test could validate the call. Be specific. Quote the prompt the human used to push back, if memorable. This list inoculates against scepticism — don't shorten it.

- **TODO**: …
- **TODO**: …
- **TODO**: …

## 4. The Workflow

TODO: the reproducible recipe. Numbered steps. Include the role of `CLAUDE.md` (or equivalent philosophy doc), the role of external review, and the human's role in step ordering and scope.

## 5. What Happened

TODO: a compact session overview. Origin, wall-clock span, active computation, human attention, key decision points. Keep this short — detail goes in the Methods note. Quote any standout user prompts. Acknowledge any stalls or breaks honestly.

## 6. Reproducibility

TODO: link list. Library/repo, PyPI/release, philosophy doc, key generated artefacts, transcript availability. Use real markdown links, not bare URLs.

- Library: TODO
- Tests: TODO
- Philosophy document: TODO
- Session JSONL: TODO — describe availability. Public mirror? Available on request to a specific contact? Private to the author? Be honest about the access model.

## 7. Limitations

TODO: at least 3 honest limitations. *Maintainability*, *generalisability*, *cost*, and *autonomous operation* are the standard four; replace or extend as appropriate.

**TODO — Maintainability.** ...

**TODO — Generalisability.** ...

**TODO — Cost.** ...

**TODO — Autonomous operation.** ...

## Methods note

TODO: move the timing detail, percentile distribution, tool-call counts, and stall narrative here. Public readers shouldn't need this to understand the case study; auditors and sceptics should be able to find it.

| Category | Time | Count | What it measures |
|----------|------|-------|-----------------|
| Tool execution (assistant(tool_use) → user(tool_result)) | TODO | TODO | Wall-clock time for Bash, reviews, file I/O |
| AI thinking → text (user(tool_result) → assistant(text)) | TODO | TODO | Token generation producing text output after a tool result |
| AI thinking → tool (user(tool_result) → assistant(tool_use)) | TODO | TODO | Token generation producing the next tool call after a tool result |
| **Total active computation** | **TODO** | | |
| AI continuation after human prompt (user(prompt) → assistant(*)) | TODO | TODO | Reported separately; not in active total |
| Human response gap (assistant(text) → user(prompt)) | TODO | TODO | Used for attention estimate; not in active total |

| Percentile | Human-response time |
|-----------|--------------|
| p10 | TODO |
| p25 | TODO |
| p50 | TODO |
| p75 | TODO |
| p90 | TODO |

TODO: tool-call breakdown.

TODO: stall narrative if any. Quote the assistant message before and the next message after; report Δ; explain the likely cause without overclaiming.
