# Case-study methodology

These rules are imperative, not background. They were derived from the corrections forced during the original jaxwavelets analysis (session `180860e2`). Read them before running any analysis script.

## Behavioural rules

1. **All headline numbers are provisional** until the user confirms them.
2. **Show the formula and the script output** for every number you publish. Don't quote a figure without showing how it was computed.
3. **Keep generated analysis under `/tmp/case-study-discovery/` until an `<id>` is chosen, then under `/tmp/case-study-<id>/`.** Never mutate the user's clone during analysis. The repo is for publish-time output only.
4. **When challenged, rerun.** Do not defend a number; recompute it. Save the new computation alongside the old one in `/tmp/case-study-<id>/revisions.md`.
5. **Maintain a revision log** at `/tmp/case-study-<id>/revisions.md` recording every challenge from the user and the corrected number.
6. **Never infer "overnight productive work" from wall-clock span.** Do not call a long gap productive unless its boundary pair is `assistant(tool_use) → user(tool_result)` and the user confirms it was a real long-running tool. A long gap whose boundary is `assistant(text) → user(prompt)` or `user(*) → assistant(*)` is a stall or break, not autonomous work.
7. **Quote the messages either side of any gap** when reporting it. Don't summarise — paste the actual prompt text and tool outputs.
8. **Adversarial questions to ask the user** before finalising any number:
   - "Could this be idle time rather than autonomous work?"
   - "Does this wall-clock span include sleep, lunch, or a suspended session?"
   - "Which claims would be embarrassing if wrong?"
9. **Cite the cautionary tale.** The original jaxwavelets analysis confidently reported a productive overnight session. The user corrected it: *"I remember waking up and sighing because all it had done was written a plan."* That correction is in the published case study (5h22m stall + 18m autonomous burst at 4am). Don't make the same mistake.

## Session discovery (cross-platform)

The Phase 0 discovery script must run on Linux *and* macOS. Avoid GNU-only flags (`stat -c`, `find -printf`). Avoid Python ≥3.10-only syntax (no `str | None` unions, no `list[str]` lowercase generics) so the script works on Python 3.8+.

Setup:

```bash
mkdir -p /tmp/case-study-discovery
```

Then save the script below as `/tmp/case-study-discovery/discover.py` and run with `python3 /tmp/case-study-discovery/discover.py 30` (the argument is the recency window in days). Once the user has chosen their session and an `<id>` (Phase 1), scratch files move to `/tmp/case-study-<id>/`.

```python
from pathlib import Path
from datetime import datetime, timezone, timedelta
import json
import re
import sys

SYSTEM_REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.DOTALL)
PROJECTS = Path.home() / ".claude/projects"


def real_user_prompt(message_content):
    """Return the user's actual prompt text, or None if the entry is
    purely system-reminder injection / tool result / non-prompt."""
    if isinstance(message_content, str):
        text = SYSTEM_REMINDER.sub("", message_content).strip()
        return text or None
    if isinstance(message_content, list):
        chunks = []
        for block in message_content:
            if isinstance(block, dict) and block.get("type") == "text":
                t = SYSTEM_REMINDER.sub("", block.get("text", "")).strip()
                if t:
                    chunks.append(t)
        return "\n".join(chunks) or None
    return None


def summarise_jsonl(path):
    cwd = None
    line_count = 0
    user_prompts = []
    session_id = None
    with path.open() as f:
        for line in f:
            line_count += 1
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if cwd is None and entry.get("cwd"):
                cwd = entry["cwd"]
            if session_id is None and entry.get("sessionId"):
                session_id = entry["sessionId"]
            if entry.get("type") == "user":
                msg = entry.get("message") or {}
                prompt = real_user_prompt(msg.get("content"))
                if prompt:
                    user_prompts.append(prompt)
    if cwd is None:
        # Fallback: derive from path. ~/.claude/projects/-home-will-foo-bar/<uuid>.jsonl
        # ↔ /home/will/foo/bar
        slug = path.parent.name
        if slug.startswith("-"):
            cwd = "/" + slug[1:].replace("-", "/")
    return {
        "path": path,
        "session_id": session_id,
        "cwd": cwd,
        "lines": line_count,
        "first_prompt": user_prompts[0] if user_prompts else "",
        "last_prompts": user_prompts[-2:],
    }


def discover(days=30):
    since = datetime.now(timezone.utc) - timedelta(days=days)
    candidates = []
    for jsonl in PROJECTS.glob("*/*.jsonl"):
        if "/subagents/" in str(jsonl):
            continue
        mtime = datetime.fromtimestamp(jsonl.stat().st_mtime, tz=timezone.utc)
        if mtime < since:
            continue
        s = summarise_jsonl(jsonl)
        s["mtime"] = mtime
        candidates.append(s)
    candidates.sort(key=lambda c: c["mtime"], reverse=True)
    return candidates


def resolve_uuid(uuid_str):
    """Resolve a UUID/session id to JSONL path(s).

    Strategy:
      1. Exact filename match: ~/.claude/projects/*/<uuid>.jsonl
      2. Otherwise: scan all JSONLs for top-level sessionId == <uuid>.
    Returns a list of candidate Paths.
    """
    matches = list(PROJECTS.glob("*/" + uuid_str + ".jsonl"))
    matches = [m for m in matches if "/subagents/" not in str(m)]
    if matches:
        return matches
    found = []
    for jsonl in PROJECTS.glob("*/*.jsonl"):
        if "/subagents/" in str(jsonl):
            continue
        try:
            with jsonl.open() as f:
                for line in f:
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if entry.get("sessionId") == uuid_str:
                        found.append(jsonl)
                        break
        except OSError:
            continue
    return found


def _candidates_index_path():
    return Path("/tmp/case-study-discovery/candidates.json")


def write_candidates_index(rows):
    out = []
    for i, r in enumerate(rows):
        out.append({
            "index": i,
            "path": str(r["path"]),
            "session_id": r["session_id"],
            "cwd": r["cwd"],
            "lines": r["lines"],
            "mtime": r["mtime"].strftime("%Y-%m-%dT%H:%M:%SZ"),
        })
    p = _candidates_index_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w") as f:
        json.dump(out, f, indent=2)


def lookup_index(idx):
    p = _candidates_index_path()
    if not p.exists():
        return None
    with p.open() as f:
        rows = json.load(f)
    for r in rows:
        if r["index"] == idx:
            return r["path"]
    return None


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--uuid" and len(args) >= 2:
        for p in resolve_uuid(args[1]):
            print(p)
        sys.exit(0)
    if args and args[0] == "--index" and len(args) >= 2:
        path = lookup_index(int(args[1]))
        if path:
            print(path)
            sys.exit(0)
        sys.stderr.write("no candidates index — run discovery first\n")
        sys.exit(1)
    days = int(args[0]) if args else 30
    rows = discover(days)
    write_candidates_index(rows)
    for i, r in enumerate(rows):
        first = r["first_prompt"][:80].replace("\n", " ")
        last = (r["last_prompts"][-1][:80].replace("\n", " ")) if r["last_prompts"] else ""
        print("%3d  %s  %5dL  %s" % (i, r["mtime"].strftime("%Y-%m-%d %H:%M"), r["lines"], r["cwd"]))
        print("      path:  " + str(r["path"]))
        if r["session_id"]:
            print("      session: " + r["session_id"])
        print("      first: " + first)
        print("      last:  " + last)
```

The default run also writes `/tmp/case-study-discovery/candidates.json`, so once the user picks index `N` you can resolve it with:

```bash
python3 /tmp/case-study-discovery/discover.py --index N
```

which prints the JSONL path on stdout.

If the user supplies a UUID/session id, run `python3 /tmp/case-study-discovery/discover.py --uuid <uuid>`:

- One match → use that JSONL path.
- Multiple matches → present numbered candidates and ask the user to choose.
- Zero matches → ask the user for an absolute JSONL path.

If the user supplies an absolute JSONL path directly, just use it (after confirming it exists and is under `~/.claude/projects/`).

## JSONL parsing rules

Claude Code session JSONLs are line-delimited JSON. Open with tolerance — warn on malformed lines, don't crash.

### Top-level fields (per entry)

- `type`: one of `user`, `assistant`, `progress`, `system`, `file-history-snapshot`, `queue-operation`, `custom-title`, `agent-name`, plus a few others. Filter for `user` and `assistant` for most analysis.
- `timestamp`: ISO 8601 with `Z` suffix. **Not present on every entry** — `progress`, `file-history-snapshot`, `queue-operation` often lack one. Skip those for gap analysis but include in inventory totals.
- `message`: object with the actual content (see below).
- `cwd`: the session's working directory (may be missing on early entries — fall back to inferring from JSONL path: `~/.claude/projects/-home-will-foo-bar/<uuid>.jsonl` ↔ `/home/will/foo/bar`).
- `sessionId`, `parentUuid`, `uuid`: useful for cross-referencing.
- `version`, `gitBranch`: Claude Code version + git branch when the message was sent.

### `message.content` parsing

`message.content` is **either a string or a list of blocks** — handle both.

**String form** (typed user prompt): the prompt is `message.content` directly.

**List form**: walk the blocks. Each block has a `type`:

- `text` — assistant or user text. The text is in `block.text`.
- `tool_use` — assistant tool call. Has `name` (e.g. `Bash`, `Edit`, `mcp__llm__review`) and `input`.
- `tool_result` — user-side tool return. Has `tool_use_id`, `content`, optional `is_error`.
- `thinking` — assistant internal reasoning (extended thinking mode); usually safe to skip for content extraction.

### System reminders

User messages can contain `<system-reminder>...</system-reminder>` blocks injected by the runtime (e.g. task list reminders, plan mode notices). These are **not real user prompts** — strip them when classifying user prompts as "real". Use a regex like:

```python
import re
SYSTEM_REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.DOTALL)
real_prompt = SYSTEM_REMINDER.sub("", text).strip()
```

If `real_prompt` is empty or only whitespace, the entry is a pure system-reminder injection — exclude from the prompt count.

### Subagent JSONLs

Subagent transcripts live at `~/.claude/projects/<project>/<session>/subagents/agent-*.jsonl`. **Exclude these from Phase 0 session listing** and from any analysis of the parent session — they're a separate conversation thread, not part of the user-facing session.

## Active-time analysis (the 5-minute-cap pair-timing method)

The headline metric is **active computation**, defined as the sum of adjacent-message timestamp gaps where the gap is ≤ 5 minutes. This excludes breaks, sleep, suspended sessions, and the user being on another screen.

### Procedure

1. Start from top-level `user` and `assistant` entries that have a `timestamp` field. Exclude `progress`, `system`, `file-history-snapshot`, `queue-operation`, `custom-title`, `agent-name`, etc. from gap analysis (keep them in inventory totals).

2. Classify each retained message by its content blocks **before** computing adjacent-pair gaps.

   **Assistant messages**: if the content list contains any `tool_use` block, classify as `assistant(tool_use)`. Otherwise (text-only or thinking-only) classify as `assistant(text)`.

   **User messages**:
   - If `message.content` (string or list) contains any `tool_result` block, classify as `user(tool_result)`.
   - Otherwise strip `<system-reminder>...</system-reminder>` from string/list text.
   - If the remaining text matches a **runtime-injection pattern**, classify as `user(system-only)` — these are not real human turns:
     - `[Request interrupted by user]` (and the `for tool use` variant) — emitted when the user hits Esc, not typed.
     - `<task-notification>...</task-notification>` — background-task system message.
     - Content starting with `<command-message>` — slash-command body injected when a `/foo` skill is invoked.
   - If non-empty real text remains, classify as `user(prompt)`.
   - If only system reminders / injections remain, classify as `user(system-only)`.

3. **Remove `user(system-only)` entries from the timing timeline.** They are runtime injections, not turns. Including them would split or extend gaps incorrectly.

4. Sort the remaining entries chronologically.

5. For each adjacent pair `(m_i, m_{i+1})`, compute `Δt = ts(m_{i+1}) - ts(m_i)`.

6. If `Δt > 5 min`, **exclude from the active-computation total** but log it separately for the user to inspect (see Stall detection below). The long-tool exception applies — see below.

7. For retained pairs, split into **five reported categories** — three count toward the active-computation headline, two are reported alongside but not summed into it:

   **Headline active computation** (sum these for the headline figure):
   - `assistant(tool_use) → user(tool_result)` = **tool execution**
   - `user(tool_result) → assistant(text)` = **AI thinking → text response**
   - `user(tool_result) → assistant(tool_use)` = **AI thinking → tool call**

   **Reported alongside, but NOT in active computation**:
   - `user(prompt) → assistant(text or tool_use)` = **AI continuation after a human prompt**. This is *AI* work, but it's the response to a human turn. Counting it as "active computation" double-counts the AI side of the human–AI exchange. Report it as its own line.
   - `assistant(text) → user(prompt)` = **human response gap**. This is the human side of the same exchange. Use it for the percentile distribution and the 30-second-cap attention estimate (see below).

8. Sum minutes per group. The headline "active computation" figure is the sum of the three computation categories only. The other two are reported as separate lines, not folded into the headline.

This split — three headline categories plus two reported-alongside categories — is what produced the canonical 4.7h figure for the jaxwavelets case study (140 min tool exec + 72 min thinking → text + 72 min thinking → tool = 284 min). The "AI continuation" and "human response" lines accounted for the rest of the retained-pair total.

### Long-tool-execution exception

Some `assistant(tool_use) → user(tool_result)` gaps exceed 5 minutes for legitimate reasons — a long test suite, a slow build, a network-bound operation. Don't blanket-exclude these.

For each such gap > 5 min:

- Inspect the `tool_use` input (what tool, what arguments).
- Inspect the `tool_result` content (success/failure, length, exit code).
- **Ask the user**: "Tool `X` ran from Y to Z (Δ=hh:mm) producing N bytes of output. Real long-running tool, or stalled session?"

Only after the user confirms is it included in the headline number.

**Subtle case: session suspension at the tool boundary.** A `assistant(tool_use) → user(tool_result)` pair can have a multi-hour gap even when the tool itself ran in milliseconds — if the Claude Code session is suspended between the agent emitting the `tool_use` block and the runtime recording the `tool_result` entry. The canonical example is the jaxwavelets overnight stall: a `Write` call for `_cwt.py` whose tool_use timestamp is 22:39:51 and whose tool_result timestamp is 04:00:59 the next morning. The Write itself ran instantly; the 5h22m gap is session suspension. The methodology must **not** report this as productive autonomous work just because the boundary pair type *could* be a long tool. Inspect the tool_result content: if it's an instant success message (e.g. "File created successfully at..."), the gap is a stall, not a long tool.

### Human-response percentile

Compute the distribution of `assistant(text) → user(prompt)` gaps:

| Percentile | What it tells you |
|---|---|
| p10, p25, p50 | The user's actual engagement cadence when they're at the keyboard. |
| p75, p90 | Likely "user is on another screen" outliers. |

Report the percentiles in the timing table. Then compute a **30-second-cap "attention" estimate**: cap each `assistant(text) → user(prompt)` gap at 30 seconds and sum. This is a *lower bound* on human attention. Report it as a separate figure, not a substitute for the un-capped sum.

The original jaxwavelets analysis: median 23s, p90 3m38s, capped sum ~22 min, un-capped ~65 min. The published case study uses ~25 min as a midpoint with the full distribution shown in the Methods note.

## Stall detection

Any gap > 30 minutes is a candidate stall. The gap is between two adjacent JSONL entries — by definition there are no entries inside it. What matters is the **pair type** at the boundary *and* the actual content either side.

For each gap > 30 minutes:

1. **Quote the entries immediately before and after the gap.** Do not paraphrase. The skill must surface verbatim text (or `tool_use` name + truncated input, or `tool_result` summary) so the user can classify the gap with full context.
2. Identify the pair type:
   - `assistant(tool_use) → user(tool_result)` — *possible* long-running tool, but also possibly a session suspension at the tool boundary (see Subtle case above). Inspect both: tool name, tool input length, tool_result content. An instant-success result on a multi-hour gap = stall, not a long tool.
   - `assistant(text) → user(prompt)` — likely human break / sleep / attention gap.
   - `user(prompt or tool_result) → assistant(*)` — possible suspended AI response (idle timeout, network drop). The agent had a turn to take but didn't take it for hours.
   - `user(tool_result) → user(prompt)` — the tool result was recorded, but the assistant did not take the next turn before the human came back. Treat as possible suspended assistant response / idle session; ask the user.
   - any other `user(*) → user(*)` or `assistant(*) → assistant(*)` ordering — unusual; quote both and ask.
3. Report Δ in hours:minutes.
4. **Pause and ask the user** to classify it: "Was this productive autonomous work, a stall, or sleep/break?"

Do not silently classify. Do not label a long unconfirmed gap with the same category name as a retained active-computation pair (e.g., a 5h `assistant(tool_use) → user(tool_result)` gap is not "tool execution" until the user confirms the tool genuinely ran for 5 hours). The original jaxwavelets analysis confidently reported a productive overnight session and was corrected by the user's memory ("I remember waking up sighing"). The Methods note in the published case study now reads:

> *The agent did not work continuously overnight: after I asked it to continue while I slept, it stalled for 5h22m, then completed an 18-minute autonomous burst at 4am.*

That honesty is the case study's credibility. The Socratic correction is the methodology — encode it as a behavioural rule, not as a one-off anecdote.

## Review verdict extraction

`mcp__llm__review` calls don't always end with a literal `APPROVED` or `FIXES REQUIRED` string — early sessions used colloquial verdicts ("not approved yet", "this needs work", "looks good to me"). The skill must:

1. Match against a literal-string allowlist first (`APPROVED`, `FIXES REQUIRED`).
2. Apply a fallback regex set for colloquial language (`not approved`, `required fixes`, `not ready`, `rejected`, etc.).
3. Classify any review whose verdict can't be determined as `unknown` rather than guessing.
4. **Surface the unknowns to the user.** Phase 1 inventory must include the count and a *human-readable, verdict-relevant* excerpt from each unknown verdict — not provider metadata, token counts, timing fields, or raw JSON wrappers. If the review result is JSON-encoded (e.g. `{"content": "...", "usage": {...}, ...}`), parse out the `content` (or equivalent text) field first, then truncate to the closing prose. Phase 4 must ask the user to adjudicate before any "rejection rate" claim is published.

Do not publish a rejection percentage unless every review's verdict is either confirmed by the regex set or hand-classified by the user.

## Prompt-count audit

Once user-message classification has filtered runtime injections, Phase 1 inventory must report:

```
Real prompts (user(prompt)):  N
Excluded by reason:
  [Request interrupted by user]:    n_1
  <task-notification>:               n_2
  <command-message>:                 n_3
  system-reminder-only:              n_4
  tool_result:                       n_5
```

Print every category, including zero-valued ones, so the user sees the full taxonomy.

Then Phase 3 / Phase 4 must ask the user whether any excluded class should be folded back into the published prompt count. (E.g., a workshop attendee may want to count `<command-message>` slash-command invocations as user actions; another may not.)

Do not publish a prompt count without showing the audit and getting the user to confirm the categorisation.

## Revision log format

Save to `/tmp/case-study-<id>/revisions.md`. One entry per correction:

```markdown
## 2026-04-17 06:49 — overnight productive work claim

Initial claim: "the agent worked productively overnight, completing CWT and wavelet packets between 22:30 and 04:18".

User challenge: "are you _sure_ about the overnight thing? I remember waking up and sighing because all it had done was written a plan. Do the autonomous calls have timestamps?"

Recomputation: Inspected timestamps between 22:39 (last assistant message) and 04:01 (next assistant message). Δ = 5h22m. Tool calls during this gap: 0. Conclusion: the session was suspended (likely Claude Code idle timeout), not productive work. Corrected number: 18-minute autonomous burst at 4am.
```

This is what the published case study draws on. Without it, the analysis is just numbers.
