---
name: case-study
description: Convert a past Claude Code session JSONL into a long-form case study + card for handley-lab.github.io. Includes session discovery (no UUID required), JSONL analysis with the 5-minute-cap pair-timing methodology, and Socratic verification before publishing. Hands off to the website skill for preview.
allowed-tools: []
---

# Case-study skill

Use this skill to turn a past Claude Code session into a publishable case study at `/case-studies/<id>/`. The reference template is [`_case_studies/jaxwavelets.md`](../../_case_studies/jaxwavelets.md), produced by exactly this methodology.

## When to use

- The user wants to write a case study but doesn't know (or remember) which session UUID to use.
- The user has a session in mind and wants to turn it into a long-form post + card.
- A workshop attendee is sitting next to a freshly-cloned `handley-lab.github.io` and wants Claude to produce a draft from one of their past sessions.

## What this skill is and is not

- **It is** documentation that orchestrates a phased workflow with Socratic verification at each step. It instructs Claude to write and run analysis scripts under `/tmp/case-study-<id>/` and to pause for user confirmation between phases.
- **It is not** committed code. Each invocation generates its own analysis scripts in `/tmp` so the user's clone is never mutated during analysis.

## Two companion files

- [`methodology.md`](methodology.md) — the JSONL parsing rules, the 5-minute-cap active-time analysis, the Socratic verification rules. **Read it before running any analysis** — these rules are the hard-won output of the original jaxwavelets case study.
- [`template.md`](template.md) — the section scaffold to fill at Phase 4.

## Phases

The phases are run in order. Each one produces output and **pauses for user confirmation** before proceeding. Do not run end-to-end without the human in the loop — the methodology depends on it.

### Phase 0 — Session discovery (no UUID required)

The publication `<id>` is not chosen yet at Phase 0. Use scratch directory `/tmp/case-study-discovery/` until the user picks an `<id>` (Phase 1 onward); then move scratch into `/tmp/case-study-<id>/`.

Use the cross-platform Python discovery script in [`methodology.md`](methodology.md#session-discovery-cross-platform). Save it to `/tmp/case-study-discovery/discover.py` and run with `python3 /tmp/case-study-discovery/discover.py 30` (the argument is the recency window in days). The script avoids GNU-only flags and Python ≥3.10-only syntax, so it runs on macOS and on Python 3.8+.

The script lists Claude Code session JSONLs across `~/.claude/projects/*/` modified in the configured window, skipping `/subagents/` paths, and prints a numbered table with index, modification date, `cwd`, line count, and a short excerpt of the first and last real user prompts (system reminders stripped).

The user can:

- **pick a number** from the listing. The default run writes `/tmp/case-study-discovery/candidates.json`; resolve the picked index with `python3 /tmp/case-study-discovery/discover.py --index N` which prints the JSONL path.
- **supply a UUID/session id**. Run `python3 /tmp/case-study-discovery/discover.py --uuid <uuid>` — the script first looks for an exact filename match, then scans for `sessionId == <uuid>`.
- **supply an absolute JSONL path** directly.

### Phase 1 — Inventory

Once the user has chosen a session, ask them for an `<id>` (kebab-case, will become the URL slug `/case-studies/<id>/`). Move scratch from `/tmp/case-study-discovery/` to `/tmp/case-study-<id>/`. From here on, all scratch files live under `/tmp/case-study-<id>/`.

Read the chosen JSONL using the parsing rules in `methodology.md`. Save to `/tmp/case-study-<id>/inventory.md`:

- Total messages by top-level `type`.
- Breakdown of assistant content blocks (`text` / `tool_use` / `thinking`).
- Wall-clock span (first → last timestamp).
- Tool-call counts by tool name.
- `mcp__llm__review` verdict counts: `APPROVED` / `FIXES REQUIRED` (literal) plus colloquial-fallback bucket (`not approved`, `not ready`, `rejected`) and an `unknown` bucket. Include a short excerpt from each `unknown` review so the user can adjudicate (see [methodology.md Review verdict extraction](methodology.md#review-verdict-extraction)).
- **Prompt-count audit**: real `user(prompt)` count, plus a breakdown of excluded entries by reason (`[Request interrupted by user]`, `<task-notification>`, `<command-message>`, system-reminder-only, `tool_result`). See [methodology.md Prompt-count audit](methodology.md#prompt-count-audit).

**Pause.** Ask the user to confirm this is the session they meant.

### Phase 2 — Active-time analysis

Apply the 5-minute-cap pair-timing methodology (see `methodology.md`). Headline outputs:

- **Active computation** — sum of three retained-pair categories (≤ 5 min):
  - tool execution (`assistant(tool_use) → user(tool_result)`)
  - AI thinking → text (`user(tool_result) → assistant(text)`)
  - AI thinking → tool (`user(tool_result) → assistant(tool_use)`)
- **Reported alongside, NOT in active total**:
  - AI continuation after human prompt (`user(prompt) → assistant(*)`)
  - human response gap (`assistant(text) → user(prompt)`)
- Wall-clock span and (active / wall-clock) ratio.
- Percentile distribution of human-response gaps; a 30-second-cap "attention" estimate as a separate, lower-bound figure.
- Long-tool-execution exceptions: any `assistant(tool_use) → user(tool_result)` gap > 5 min, with the `tool_use` input and the `tool_result` content. **Watch the subtle case**: an instant-success `tool_result` on a multi-hour gap means the session suspended at the tool boundary — *not* a long tool. See methodology.md.
- Candidate stalls/breaks: any gap > 30 min, with start/end, Δ, and the messages immediately either side. **Quote them verbatim.** Long-gap entries must NOT be labelled with retained-pair category names (e.g. don't call a 5h gap "tool execution"; label it "candidate stall, requires user adjudication").

**Pause for each long gap.** Quote the entry immediately before and the entry immediately after, identify the boundary pair type, and ask the user to classify it (real long-running tool, suspended/stalled session, or human break/sleep). See [`methodology.md`](methodology.md#stall-detection) for the pair-type taxonomy and why this Socratic pause is required, not optional.

Save the analysis script to `/tmp/case-study-<id>/timing.py` and the report to `/tmp/case-study-<id>/timing.md`.

### Phase 3 — Tool & prompt classification

Tool-call counts by name, and human-prompt classification (rough categories: `strategic / review-trigger / design-decision / quality-challenge / operational / continuation`). Heuristic — keyword + length. Output as a frequency table to `/tmp/case-study-<id>/classification.md`. **The user can override classifications.**

### Phase 4 — Narrative scaffold

Copy `template.md` to `/tmp/case-study-<id>/draft.md` and fill it with the computed numbers and lifted excerpts. Save the proposed card YAML separately to `/tmp/case-study-<id>/card.yml`.

**Do not edit `_case_studies/` or `_data/case_studies.yml` until Phase 6.** Phase 4 is non-mutating: all output stays under `/tmp/case-study-<id>/`.

Sections (matching the jaxwavelets exemplar):

1. Abstract
2. Motivation (the *embodied intelligence* idea, or the project-specific intellectual hook)
3. N Principles (project-specific — let the user name them)
4. What Required Human Intervention
5. The Workflow
6. What Happened (compact session overview)
7. Reproducibility (with links — repo, PyPI, philosophy doc, transcript availability)
8. Limitations
9. Methods note (the timing / percentile detail moved out of the main flow)

The principles section is **author-authored** — produce a stub with prompts for the user to fill, not invented content. Same for the abstract: produce a draft, but flag it as a draft and ask the user to challenge or rewrite.

### Phase 5 — External review (optional, opt-in, privacy-aware)

Before sending anything externally:

1. List the artefacts that would be sent: draft markdown, full JSONL, redacted JSONL, draft only.
2. **Warn explicitly** that JSONLs may contain private repo paths, emails, unpublished code, accidentally-pasted credentials, or supervision-private material.
3. Offer four modes:
   - (a) draft only;
   - (b) draft + redacted excerpts (auto-redact emails / token-shaped strings / absolute home paths);
   - (c) draft + full JSONL after user confirms;
   - (d) skip external review.
4. If `mcp__llm__review` is unavailable, fall back to a manual prompt the user can paste into ChatGPT/Gemini.

Default: draft only. Don't escalate without explicit user opt-in.

### Phase 6 — Publish

Hand off to the [`website` skill](../website/SKILL.md). Inputs from Phase 4: `/tmp/case-study-<id>/draft.md` and `/tmp/case-study-<id>/card.yml`.

The website skill is responsible for:

- Running its scripted duplicate-ID check (yml + filename + frontmatter).
- Creating the `case-study/<id>` feature branch.
- Writing `_case_studies/<id>.md` from the Phase 4 draft.
- Appending the card to `_data/case_studies.yml` from the Phase 4 card.yml using the **full schema** (`id`, `title`, `category`, `timebox`, `status`, `summary`, `outcome`, `evidence`, optional `demo_url`, `repo_url`).
- Building, leak-checking, previewing at `/case-studies/<id>/`.
- Committing and opening a PR.

Until Phase 6 is invoked, **nothing under the website's tracked source has been mutated** — the case-study skill alone never edits `_case_studies/` or `_data/case_studies.yml`.

## Edge cases

- **Sessions without timestamps** (older Claude Code versions): fall back to wall-clock-only analysis with a banner. No 5-min cap is possible.
- **Compacted sessions**: the first user message may be a context summary, not the original prompt. Detect `<command-name>` or `Caveat:` markers and warn.
- **Subagent JSONLs**: under `<session>/subagents/agent-*.jsonl`. Excluded from Phase 0 listing.
- **PII / credentials**: see Phase 5. Default opt-out for JSONL escalation.
- **Non-handley-lab sessions**: ask the user whether the case study should still publish to `handley-lab.github.io` or be kept private/local.
- **Long-running tool execution mistaken for stall**: methodology distinguishes `tool_use→tool_result` gaps from text→prompt gaps. Inspect tool input/output before classifying.

## Cautionary tale

The original jaxwavelets case study went through several Socratic corrections before reaching the published numbers. From session `180860e2` (the analysis session that produced [`_case_studies/jaxwavelets.md`](../../_case_studies/jaxwavelets.md)):

- *"When you say 46 hours — there were plenty of pauses there. Is there a way to determine how long it actually took?"* — forced the introduction of the 5-min-cap method. Wall-clock 46h → active 4.7h.
- *"are you _sure_ about the overnight thing? I remember waking up and sighing because all it had done was written a plan."* — corrected an over-confident "productive overnight" narrative to a 5h22m stall + 18m burst.
- *"are you sure about 6.2h?"* — pushed a tighter recomputation that landed on 4.7h.
- *"Take me through how you've come to that?"* — required the methodology be explained, not just the result.

This is the discipline. **All headline numbers are provisional until the user confirms them.** See `methodology.md` for the full rules.
