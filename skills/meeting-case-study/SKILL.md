---
name: meeting-case-study
description: Turn a live or recent meeting (Otter transcript) into a published case study for the AI Cookbook. Sibling of the `recipe` skill but for meeting capture rather than Claude Code session forensics. Produces (a) a private group repo containing verbatim transcripts and a styled LaTeX/PDF report; (b) a `_recipes/<id>.md` case-study page on the website matching the jaxwavelets exemplar; (c) a card in `_data/recipes.yml`. Use when the user has just attended (or is attending) a meeting they want documented as a worked example of live-meeting capture.
allowed-tools: []
---

# Meeting Case Study skill

Sibling of the [`recipe`](../recipe/SKILL.md) skill. Where `recipe` does forensic analysis of a past Claude Code session, this skill captures a live (or recently concluded) meeting and turns it into:

1. A **private group repository** (under the relevant org) containing the verbatim Otter transcripts and a curated LaTeX/PDF report distilled from them.
2. A **case study page** at `_recipes/<id>.md` on the website, matching the [jaxwavelets exemplar](../../_recipes/jaxwavelets.md).
3. A **card** in `_data/recipes.yml`.

The reference worked example is the [thesis-writing-workshop case study](https://github.com/handley-lab/thesis-writing-workshop/blob/master/CASE_STUDY.md) from the 26 May 2026 thesis workshop.

## When to use

- The user has just attended a workshop, seminar, or group meeting that was being transcribed by Otter and wants it captured before the memory fades.
- The user is *currently in* such a meeting and wants Claude Code to monitor the live transcript and produce a draft document by the time the meeting ends.
- The user explicitly asks for "a case study of this session" or "case study for the website".

If the input is a Claude Code session JSONL rather than an Otter transcript, use the [`recipe`](../recipe/SKILL.md) long-form path instead.

## Phases

### Phase 0 — Identify the meeting

Use `mcp__otter__otter` to find the meeting:

- `action=live` for currently-live meetings
- `action=recent` to list the last ~10 meetings
- `action=search` for a title keyword

A multi-hour workshop usually produces two or more Otter sessions (one per stretch around a break). Get all the `otid`s before proceeding. Also check for any Otter "Note" recordings created in the same window — they are sometimes duplicates and sometimes incidental private conversations that should be excluded.

### Phase 1 — Decide on Chatham House discipline

Ask the user, or infer from context:

- **Anonymise from the start.** Speakers are referred to as "a participant", "a student", "the convenor"; named attribution only in the title-block administrative metadata. This is the default.
- **Attributed.** Speakers are named in the body. Only safe when all speakers have explicitly consented and the document is internal.

Record this decision before writing anything. Switching mid-stream is expensive (it forces a global rewrite).

### Phase 2 — Live or post-hoc?

**Live mode.** The meeting is in progress. The expected user prompt is `check`. On each `check`:
1. Pull new segments via `mcp__otter__otter action=transcript otid=<otid> since_offset_ms=<last seen>`.
2. Summarise inline for situational awareness (short, to the user).
3. At inflection points, fold substantive material into the LaTeX report via `Edit` calls.
4. Recompile with `pdflatex` and report the page count.

Track the last-seen offset per `otid`. Do not re-read earlier segments — they cost context for no gain.

**Post-hoc mode.** The meeting is over. Pull the full transcripts in one go (use `include_formatted_text=true`; output usually exceeds the inline cap, so use the persisted-output file plus `jq -r '.transcript.formatted_text'` to extract). Skip the polling loop.

### Phase 3 — First synthesis

Save each transcript to `/tmp/<id>-transcripts/` as a text file. Hand all transcripts plus a styling brief to OpenAI (`mcp__llm__chat model=openai`, `reasoning_effort=high`, `branch=false`) and request a LaTeX report. Pass the file paths via the `files=` parameter — never inline ~70 KB of transcript text into the prompt.

System prompt should include:
- Output **only** valid LaTeX, no markdown fences, no commentary.
- Preserve the preamble exactly if one is supplied (see Phase 4).
- Compile-clean on `pdflatex`.
- Anonymisation rule from Phase 1.

The output file is written via `output_file=` so the response doesn't enter Claude's context. Strip any markdown fence the model may add despite the instruction (one of the failure modes — verify before compiling).

### Phase 4 — Apply a LaTeX style

If the user names a style (e.g. "in the X style", "like the document I sent to Y"), invoke the [`tex-style-from-email`](../../../../.claude/skills/tex-style-from-email/SKILL.md) skill to extract the preamble from a past email attachment.

If no style is named, use the default Handley-group preamble:
- `lmodern` + `parskip` + `microtype`
- `\usepackage[margin=2.5cm]{geometry}`
- matplotlib `tab10` colours `C0`–`C9` defined via `\definecolor{Cn}{HTML}{...}`, with `\colorlet{accent}{C0}`
- `\titleformat{\section}{\large\bfseries\color{accent}}{}{0em}{}[\vspace{-0.5em}\rule{\textwidth}{0.4pt}]`
- `fancyhdr` page style with the group name on the left and date on the right
- Manual centred title block with metadata `tabular` (Date / Location / Convenor / Organiser / Audience / Status)
- `% ============` banner comments between sections

### Phase 5 — Iterate during/after the meeting

For each `check` (live mode) or each user message (post-hoc mode):

- Pull new transcript segments if live.
- Fold substantive content into the report via `Edit`.
- Recompile, report the page count.
- Note in chat anything explicitly excluded (private side-conversations, AV chatter, coffee-break logistics).

When the meeting ends or a major restructure is needed, do a **second OpenAI synthesis pass**: hand it the full transcripts and the current `.tex`, ask it to fold in named additions, anonymise per Phase 1, and emit a revised file. Strip fences, compile, report.

### Phase 6 — Build the private group repo

```
<org>/<meeting-slug>/
  README.md                 # what's here, how to contribute, Chatham House note
  .gitignore                # LaTeX build artefacts
  report/
    <meeting-slug>.tex
    <meeting-slug>.pdf
  transcripts/
    <YYYY-MM-DD>-session1-<segment>.txt    # Otter formatted_text, verbatim
    <YYYY-MM-DD>-session2-<segment>.txt
  CASE_STUDY.md             # the case-study, matching jaxwavelets style
```

Create via `gh repo create <org>/<meeting-slug> --private --source=. --push`. Then grant write access to the relevant team:

```
gh api -X PUT orgs/<org>/teams/<team>/repos/<org>/<meeting-slug> -f permission=push
```

The default team is the org-wide one (commonly `<org>/all`). Confirm with `gh api orgs/<org>/teams --jq '.[] | {name, slug}'` first.

### Phase 7 — Write CASE_STUDY.md

Match the [jaxwavelets recipe template](../../_recipes/jaxwavelets.md) structure:

- YAML front matter (`id`, `title`, `category`, `timebox`, `status`, `summary`, `outcome`, `evidence`, `date`)
- Abstract
- The Problem
- The Workflow That Emerged (include an ASCII diagram)
- Style choices, anonymisation decisions
- What Required Human Intervention (the credibility check)
- Costs and Timing (OpenAI token spend + human attention estimate)
- What Generalises
- Skills Spun Out
- Limitations
- Reproducibility (links, Otter session IDs, archived LLM call IDs)

The "Costs and Timing" section should report actual cost in dollars from `mcp__llm__chat` `usage.cost` fields.

### Phase 8 — Publish to the website

Hand off to the [`website`](../website/SKILL.md) skill to:

- Copy `CASE_STUDY.md` to `_recipes/<id>.md`.
- Add a card to `_data/recipes.yml` matching the schema.
- Build locally, verify the page renders.
- Commit on a feature branch and open a PR.

The card schema:

```yaml
- id: <id>
  title: "<plain descriptive title>"
  category: "Live-meeting capture"
  timebox: "<e.g. 5-hour meeting, 1 hour human attention>"
  status: "Complete"
  proposer: "<full name>"
  summary: "<1–2 sentences. Lead with what became possible.>"
  outcome: "<the artefacts: private repo, report, case study>"
  evidence: "<repo URL, transcripts kept verbatim, LLM call IDs>"
  demo_url:
  repo_url: "<the private repo URL>"
```

## Costs

The thesis-workshop reference run cost **$0.68** total across two OpenAI synthesis passes (`gpt-5.5`, high reasoning effort, ~42k input + ~16k output tokens). All other work was native Claude Code. Human attention was ~30–60 minutes spread across a 5-hour meeting.

## Gotchas

- Otter routinely mistranscribes domain-specific terms ("viva" → "vibe"/"Bible", "Opus" → "OPS"/"OS"). The synthesis pass usually corrects these silently, but check the final document for survivors.
- Otter sometimes records pre- and post-meeting walking conversations. Identify and exclude these explicitly — they often contain private content unrelated to the meeting.
- `mcp__otter__otter action=transcript` with `include_formatted_text=true` regularly exceeds the inline output cap for long meetings; rely on the persisted-output file and use `jq` to extract.
- `mcp__llm__chat` with `model=openai` and large `files=` payloads may wrap the response in markdown fences despite instructions; always strip before compiling.
- `git -c commit.gpgsign=true` is the safe form for committing; do not silently disable signing.
- `gh repo create --private --source=. --push` fails if the local `git init` was not done first. Initialise the repo with `git init -q && git add -A && git commit -m "Initial commit"` before invoking `gh`.

## Reference run

The 26 May 2026 thesis-writing workshop produced:

- Private repo: `github.com/handley-lab/thesis-writing-workshop`
- Report: 14 pages, 12 sections, ~5,500 words
- Case study: [`CASE_STUDY.md`](https://github.com/handley-lab/thesis-writing-workshop/blob/master/CASE_STUDY.md)
- Total spend: $0.68 OpenAI + native Claude Code

See that case study for a walkthrough of the actual prompts used.
