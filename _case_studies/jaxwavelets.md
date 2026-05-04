---
id: jaxwavelets
title: "Vibe Coding a Scientific Library: Building jaxwavelets in a Single Session"
category: "Rapid Development"
timebox: "4.7 hours active computation"
status: "Complete"
summary: "JAX-native wavelet transform library with full PyWavelets feature parity, built in a single Claude Code session — 4.7 hours of active computation, ~25 minutes of human attention, 100% test coverage, matching PyWavelets to atol=1e-14."
outcome: "Production-quality library with PyPI release, 1,177 parametrised tests, 100% coverage, and floating-point parity with the C reference implementation."
evidence: "Complete session JSONL (4,221 entries, 95 prompts); 65 external LLM reviews (60% rejection rate); test suite verifying numerical parity to atol=1e-14; published at github.com/handley-lab/jaxwavelets."
demo_url:
repo_url: "https://github.com/handley-lab/jaxwavelets"
author: "Will Handley, Institute of Astronomy, University of Cambridge"
date: 2026-04-16
---


## Abstract

This case study documents the creation of [jaxwavelets](https://github.com/handley-lab/jaxwavelets), a JAX-native wavelet transform library with full [PyWavelets](https://pywavelets.readthedocs.io/) feature parity, built in 4.7 hours of active computation across a single Claude Code session, requiring approximately 20–30 minutes of human attention. The library comprises ~3,000 lines of library code (plus 4,200 lines of auto-generated filter coefficients), ~950 lines of tests (1,177 parametrised test cases), achieves 100% test coverage, and matches PyWavelets to `atol=1e-14` on direct comparisons. The session transcript — 4,221 JSONL entries across 95 human prompts — provides a complete record of how an academic scientist can effectively direct an AI coding agent to produce production-quality scientific software. Three key principles emerged: *embodied intelligence extraction*, *adversarial iterative review*, and *scientist-as-architect*.

## 1. Motivation: Embodied Intelligence

A mature scientific library like PyWavelets represents what I call **embodied intelligence** — analogous to embodied carbon in construction. PyWavelets has been tested, debugged, and battle-tested across thousands of real-world scientific applications over two decades. Its C convolution routines encode subtle numerical decisions (boundary handling, filter alignment, periodization conventions) that were arrived at through years of evolutionary pressure from real users discovering real bugs.

This embodied intelligence should not be discarded. But PyWavelets is written in C/Cython and cannot participate in JAX's transformation ecosystem: no automatic differentiation, no JIT compilation, no GPU acceleration, no `jax.vmap` composability. The task of *transferring* this embodied intelligence to JAX — preserving numerical correctness while gaining differentiability and composability — is ideally suited to AI-assisted "vibe coding."

The key insight is that reimplementing a well-tested library is fundamentally different from writing novel code. The specification already exists in the form of the reference implementation. Every numerical decision can be validated to machine precision. The AI doesn't need domain creativity — it needs faithful translation and the discipline to match floating-point behaviour exactly.

The term "vibe coding" — directing an AI agent with natural-language prompts rather than writing code — has entered popular usage primarily in the context of rapid prototyping and disposable scripts. This case study argues that the approach can produce production-quality scientific software, given the right conditions: a well-tested reference implementation, adversarial review, and a domain expert maintaining architectural control.

## 2. Session Overview

### 2.1 Origin

The session began during a live supervision meeting with PhD student Chris Lovell, who was using PyWavelets for wavelet decomposition of cosmological fields. The question "how jaxable is pywt?" led to discovering that existing JAX wavelet libraries were unmaintained (jax-wavelet-toolbox, last updated 2023). Within 20 minutes, we decided to build a fresh implementation.

### 2.2 Timeline

| Phase | Time | Commits | Tests | What happened |
|-------|------|---------|-------|---------------|
| Meeting + exploration | 15:29–16:09 | 0 | 0 | Live meeting, explored pywt, searched for JAX alternatives |
| Plan + initial implementation | 16:09–17:24 | 1 | 719 | 8 plan review iterations with OpenAI, then DWT/IDWT/nD implemented |
| Review + philosophy | 17:24–22:37 | 6 | 719 | Custom pytree, CLAUDE.md philosophy, periodization, composability |
| Overnight: remaining transforms | 22:37–04:18 | 12 | 1,142 | SWT, FSWT, MRA in evening; plan then 5h stall; CWT + packets burst at 4am |
| Refinement + precision | 05:08–07:01 | 4 | 1,142 | Tightened tolerances, removed complex arithmetic, JIT-compatible CWT |
| Packaging + CI | 07:01–10:25 | 18 | 1,177 | README, PyPI, CI, badges, coverage, branch protection |
| Final review | 12:17–14:29 | 4 | 1,177 | Anti-scientific code review, threshold simplification |

Wall-clock span: ~46 hours (Tuesday afternoon to Thursday afternoon).
Active computation time: **4.7 hours** (284 minutes, methodology below).
Human time: **~20–30 minutes** (95 prompts, median response time 23 seconds, most spent on other screens between prompts).
Commits: 57 (across the full history, including PR merges).

The 4.7-hour figure is computed by summing all adjacent message pairs in the JSONL transcript, excluding any pair with a gap exceeding 5 minutes. The conversation consists of interleaved assistant and user messages. Each adjacent pair falls into one of several categories:

| Category | Time | Count | What it measures |
|----------|------|-------|-----------------|
| Tool execution (assistant→tool result) | 140 min | 1,111 | Wall-clock time for Bash, reviews, file I/O |
| AI thinking → text response | 72 min | 580 | Token generation producing text output |
| AI thinking → tool call | 72 min | 529 | Token generation producing next action |
| **Total computation** | **284 min** | | |

An additional 65 minutes of human response time (assistant text → next human prompt) and 37 minutes of AI continuation time (multi-step reasoning within a single turn) account for the remaining gap to the 418-minute block total. The 65 minutes of human response time is an upper bound; capping each prompt at 30 seconds gives ~22 minutes (see below).

The session JSONL records timestamps on every message, allowing precise reconstruction. The human time estimate deserves scrutiny. Measured naively as the gap between the AI's last message and the next human prompt (excluding breaks >5 minutes), the upper bound is 60 minutes. But the gap distribution tells a different story:

| Percentile | Response time |
|-----------|--------------|
| p10 | 1 second |
| p25 | 12 seconds |
| p50 (median) | 23 seconds |
| p75 | 47 seconds |
| p90 | 3 minutes 38 seconds |

The p90 outliers are not deep reading — they are the human on another screen. Capping each prompt at 30 seconds (generous for "yes", "commit", "push", "continue") gives 22 minutes total. The realistic human engagement was **20–30 minutes of attention spread across 95 prompts over two days.**

The 4.7 hours of active computation were spread across 20 work blocks (with idle time between and within blocks):

| Block | Time | Duration | Mode | Activity |
|-------|------|----------|------|----------|
| Tue afternoon | 15:29–16:50 | ~1h | Interactive (13 prompts) | Meeting, exploration, decision to build |
| Tue evening | 20:38–22:39 | ~40m | Interactive (12 prompts) | Review, philosophy, periodization, composability |
| Tue night | 22:30–22:39 | 9m | Interactive (1 prompt) | Plan extension for CWT + packets |
| **Stall** | **22:39–04:01** | **5h 22m** | **Dead time** | **AI wrote one file then stalled** |
| Wed 4am | 04:01–04:18 | 18m | Autonomous | CWT + wavelet packets burst |
| Wed midday | 12:48–14:00 | ~30m | Interactive (5 prompts) | Missing features review, nD SWT, thresholding |
| Thu morning | 05:07–09:41 | ~2.5h | Mixed (32 prompts + 5 autonomous blocks) | Precision, complex arithmetic, CWT JIT, packaging, CI |
| Thu afternoon | 12:17–13:29 | ~23m | Interactive (11 prompts) | Final anti-scientific review, threshold simplification |

The overnight block reveals a limitation of autonomous operation. After the human's prompt "why would you stop. I want you to complete this overnight whilst I sleep. Please don't stop again" (22:16), the AI spent 9 minutes extending the plan with CWT and wavelet packet details, wrote a single file (`_cwt.py`), and then **stalled for 5 hours 22 minutes**. The most likely cause is a Claude Code idle timeout or session suspension — the agent had no pending tool call to keep it active and no human prompt to respond to, so the session was suspended by the harness and later resumed, possibly triggered by a keepalive or reconnection. At 04:01 it resumed with an intense 18-minute autonomous burst: implementing CWT tests, debugging Gaussian wavelet normalization, implementing wavelet packets, debugging nD mode defaults against PyWavelets' C source, running all 1,142 tests, and pushing. The SWT, FSWT, and MRA had already been implemented earlier in the evening session before the human went to sleep.

Thursday morning shows a different pattern: the human was actively steering (32 prompts in 2.5 hours) but interspersed with 5 autonomous CI-fixing blocks (2–10 minutes each) where the AI diagnosed and fixed platform-specific issues independently while the human was elsewhere.

### 2.3 Session Statistics

| Metric | Count |
|--------|-------|
| Human prompts | 95 |
| Tool calls (total) | ~1,100 |
| — Bash commands | 528 |
| — File edits | 181 |
| — File reads | 130 |
| — File writes | 113 |
| — External LLM reviews | 65 |
| — Web searches | 12 |
| — Subagent launches | 8 |
| Final library code | ~2,936 lines (excl. filters) |
| Auto-generated filters | 4,239 lines |
| Test code | 947 lines → 1,177 parametrised tests |
| Test coverage | 100% |
| Estimated API cost | ~$100 (Claude Code session + 65 OpenAI review calls) |

## 3. The Three Principles

### 3.1 Embodied Intelligence Extraction

PyWavelets' C code contains hundreds of subtle numerical decisions. Rather than reimplementing wavelet transforms from textbook definitions alone, the approach was to use PyWavelets as a *numerical oracle*: implement from the mathematical definition, but validate every computation against PyWavelets to machine precision.

This surfaced real issues that textbook implementations would miss:

- **Filter alignment in SWT**: The stationary wavelet transform dilates filters by powers of 2. The naive "dilate, pad, convolve" approach works for Haar but fails for longer filters (db2, db4, db8). Three separate review rounds with OpenAI were needed to identify the correct cycle-spinning alignment matching PyWavelets' C code (prompts 31–33, reviews 21–23).

- **Periodization boundary handling**: The periodization mode requires promoting odd-length signals to even, wrap-padding, and careful index alignment. This was deferred initially because the first implementation produced errors ~1.0, then fixed after studying the C source directly (prompts 37–38, reviews 16–18).

- **sinc precision in frequency B-spline wavelets**: The `fbsp` wavelet showed 1.5e-14 error vs PyWavelets while all others matched at ~1e-16. Investigation traced this to the difference between `jnp.sinc` and a manual `sin(πz)/(πz)` implementation. The decision to use `jnp.sinc` (which may be GPU-optimised in future) and accept 1.5e-14 was a deliberate scientific judgment (prompt 38, review 39).

- **Complex arithmetic removal**: PyWavelets' C code computes real and imaginary parts of complex wavelets (Morlet, complex Gaussian, etc.) separately. When the question arose of whether JAX should use native complex arithmetic instead, the initial AI recommendation was "complex numbers are fine on GPU." The human overrode this based on student experience with GPU performance, insisting on matching the C code's approach (prompts 40–42, reviews 40–42). This led to removing all complex arithmetic from the CWT pipeline.

The test suite embodies this extraction: 1,177 tests compare every function against PyWavelets across multiple wavelet families, signal lengths, decomposition levels, and boundary modes, at tolerances of `1e-14` (direct) and `1e-11` (roundtrip).

### 3.2 Adversarial Iterative Review

The session used 65 external LLM review calls (GPT-5.4 via `mcp__llm__review`), of which **39 returned "FIXES REQUIRED"** and 26 returned "APPROVED." This 60% rejection rate reflects genuinely adversarial review, not rubber-stamping.

The reviews operated at multiple levels:

1. **Plan review** (reviews 1–8): 8 iterations to get the implementation plan approved. Issues caught included incorrect boundary-mode mappings, confusion between `vmap` semantics and structural axis operations, and incorrect convolution conventions.

2. **Implementation review** (reviews 9–48): Each phase of implementation was reviewed against both correctness and the codebase philosophy (CLAUDE.md). The philosophy demanded: no defensive programming, no overengineering, no input validation, let-it-crash semantics. Reviews caught violations like:
   - `if not coeffs.details: return coeffs.approx` — a defensive guard
   - `_PAD_MODES` dictionary — unnecessary indirection
   - String-dispatch `threshold(data, value, mode='soft')` — anti-scientific abstraction

3. **Targeted debugging** (reviews 17–18, 25–26, 30–33, 47): When implementations produced wrong values, OpenAI was used as a *consultant* to debug specific numerical issues. The SWT alignment problem required three rounds of increasingly specific questions, ultimately solved by reading PyWavelets' C source directly.

4. **Philosophy enforcement** (reviews 14–15, 48, 64–65): Dedicated review passes specifically targeting anti-scientific programming patterns. The final "aggressive review" (prompt 83) caught zero-division guards in thresholding and a string-dispatch pattern, both removed in the final PRs.

The review pattern was not linear — it was genuinely iterative. The human directed *when* to review, *what* to focus on, and critically, *when the reviewer was wrong*. At prompt 33 ("is it niche, or are you backwards justifying that?"), the human challenged whether the AI was rationalising a gap rather than honestly assessing it. The AI consulted OpenAI and revised its assessment.

### 3.3 Scientist-as-Architect

The human's role was architectural, not editorial. Of the 95 prompts, the distribution was roughly:

| Role | Count | Examples |
|------|-------|---------|
| Strategic direction | ~25 | "how much effort to migrate pywt to jax", "can we review what functionality we're missing" |
| Review triggers | ~20 | "get an iterative review", "can we get an aggressive review for anti-scientific programming" |
| Design decisions | ~15 | "I disagree — match the C code", "jaxwavelets — goes with pywavelets" |
| Quality challenges | ~10 | "are you _sure_?", "why 1e-11 and not lower?", "is it niche or backwards justifying?" |
| Operational | ~15 | "commit", "push", "monitor CI" |
| Continuation | ~10 | "continue", "yes", "please don't stop again" |

The human never wrote a line of code. But the human made every decision that required scientific judgment:

- **Tolerance decisions**: Pushing `atol` from 1e-11 to 1e-14, identifying that the fbsp tolerance discrepancy was acceptable
- **API design**: "jaxwavelets — goes with pywavelets", "import jaxwavelets as wt"
- **Complex arithmetic**: Overriding the AI's GPU advice based on student experience
- **Philosophy enforcement**: "no defensive programming, let it crash — this is scientific code"
- **Scope control**: "no, let's leave that for now" (on admissible basis reconstruction)
- **Tone**: "The README is too adversarial. Phrase it as 'extending' pywavelets. We wouldn't have been able to do this without them"

This last point is worth emphasising. The AI's initial README positioned jaxwavelets competitively against PyWavelets. The human recognised that the library *depends on* PyWavelets' embodied intelligence and insisted the framing reflect gratitude rather than competition.

## 4. What the AI Did Well

- **Faithful numerical implementation**: Matching PyWavelets to 1e-14 across all transforms, wavelets, and modes
- **Autonomous burst implementation**: Implementing CWT + wavelet packets in an 18-minute autonomous burst at 4am, including debugging nD mode defaults against PyWavelets' C source
- **Responsive to philosophy**: After CLAUDE.md was established, the AI consistently caught its own defensive-programming tendencies during review
- **PyPI packaging and CI**: Complete packaging infrastructure in ~3 hours, including trusted publishing, codecov, and branch protection

## 5. What Required Human Intervention

- **Complex arithmetic decision**: The AI defaulted to "complex numbers are fine" — the human's anecdotal evidence from students was the deciding factor
- **Tolerance investigation**: The AI had set `atol=1e-11` "empirically" without investigating. The human's "why not lower?" forced proper investigation, tightening to 1e-14
- **Philosophy enforcement**: Required explicit CLAUDE.md and dedicated review passes. Left to itself, the AI drifted toward defensive programming
- **Naming and framing**: "jaxwavelets" (matching pywavelets), the collaborative rather than competitive README tone
- **Scope control**: Knowing when to stop adding features

## 6. The Vibe Coding Workflow

The workflow that emerged can be summarised as:

```
1. Identify a well-tested reference implementation (embodied intelligence)
2. Write a philosophy document (CLAUDE.md) codifying code style and constraints
3. Plan with adversarial review (iterate until the external reviewer approves)
4. Implement phase-by-phase, with:
   a. Implementation
   b. Test against reference to machine precision
   c. External review against philosophy
   d. Human judgment on design decisions and scope
5. Package, test, publish
6. Final adversarial review pass for philosophy violations
```

The key enabler is that step 4b provides an *objective* quality signal. Unlike novel code where "correct" is ambiguous, reimplementation has a clear numerical target. This makes vibe coding particularly effective: the AI handles the translation, the reference implementation provides the specification, and the human provides judgment.

## 7. Reproducibility

The complete session transcript is available as a JSONL file:

```
16ab9ff4-25f6-4f0d-acbe-43338ac4cc82.jsonl
```

This file contains every human prompt, every AI response, every tool call and its result, and every external review. It is a complete, reproducible record of how the library was built.

The library itself: [github.com/handley-lab/jaxwavelets](https://github.com/handley-lab/jaxwavelets) | [pypi.org/project/jaxwavelets](https://pypi.org/project/jaxwavelets/)

## 8. Conclusion

The jaxwavelets case study demonstrates that vibe coding is not just for prototyping. When the task is *transferring embodied intelligence* from a battle-tested library to a new framework, AI coding agents can produce production-quality scientific software — provided a domain expert maintains architectural control and enforces scientific standards through adversarial review.

The 60% review rejection rate is not a failure metric — it is the mechanism by which quality is achieved. Each rejection caught a genuine issue: an incorrect boundary condition, a defensive guard that violated the library philosophy, a tolerance that was too loose. The AI is the engine; the reviews are the brakes; the scientist is the driver.

Three lessons for academics considering vibe coding:

1. **Respect embodied intelligence.** A mature library's numerical decisions were hard-won. Match them to machine precision before claiming your reimplementation works.

2. **Use adversarial review, not rubber-stamping.** External LLM review at 60% rejection rate is quality assurance. At 5% rejection rate, it's theatre.

3. **Stay in the architect's seat.** The most consequential decisions in this session — tolerance standards, complex arithmetic, API naming, README tone — were all human judgments. The AI wrote 7,000 lines of code in 4.7 hours of computation; the human wrote 0 lines in ~25 minutes of attention. But the human shaped every line.

## 9. Limitations

**Maintainability.** The library was generated in a single session by an AI agent. While the code is clean, well-tested, and follows a consistent philosophy, the question of long-term maintainability is open. If a bug is discovered in six months, can a graduate student — or the original author — debug AI-generated code they never wrote? The 100% test coverage and machine-precision validation against PyWavelets provide strong regression protection, but the *understanding* of the code resides in the session transcript, not in a human's head. This is mitigated by the library's small size (~3,000 lines excluding filters) and the CLAUDE.md philosophy document, which constrains future modifications to the same style.

**Generalisability.** The conditions that made this case study successful — a well-tested reference implementation, an objective numerical validation target, and a pure-functional target framework — are not universal. Reimplementing a library with no reference oracle, or building novel scientific software where "correct" is ambiguous, would require a fundamentally different workflow. The embodied intelligence extraction pattern applies specifically to the transfer of mature software between frameworks.

**Cost.** The estimated API cost of ~$100 is modest for a complete library, but would be prohibitive if the approach required multiple failed attempts. The session succeeded on the first try, which may not be representative.

**Autonomous operation.** The overnight stall (Section 2.2) demonstrates that current AI agents cannot reliably sustain multi-hour autonomous work. The productive overnight output was an 18-minute burst, not a sustained 7-hour effort. Autonomous operation remains most effective in short blocks (CI fixing, single-phase implementation) rather than extended campaigns.
