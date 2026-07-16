---
id: coating-sampler-blackjax
title: "Updating a coating sampler for the current BlackJAX nested-sampling API"
category: "Legacy Code Navigation"
timebox: "15 minutes active computation"
status: "Draft"
summary: "A single supervised Claude Code session updated an optical-coating nested-sampling script for the current BlackJAX API, built a fresh GPU-capable Python environment, smoke-tested the result on CPU, and ran it on an A100 to produce the requested optimisation plot."
outcome: "Working `sampler.py` run against the current `blackjax-ns` interface, with a generated `ar_coating_blackjax_optimization.png` from an interactive GPU job."
evidence: "A private Claude Code transcript records 32 tool calls over a 20-minute wall-clock session; the final run used an interactive GPU job on an A100 and reported an output PNG plus final log-evidence around -42664."
demo_url:
repo_url: "https://github.com/zwei-beiner/Code"
author: "Namu Kroupa"
date: 2026-05-05
---

## Abstract

This case study is small on purpose. A legacy optical-coating sampler needed to be moved onto the current `blackjax-ns` interface, installed in a GPU-capable environment, tested, and run to produce a plot. Instead of treating those as separate setup, API archaeology, debugging, and HPC tasks, the whole repair was expressed as one operational prompt to Claude Code. The session produced a fresh Python 3.13 virtual environment, patched `sampler.py`, smoke-tested it on CPU, and launched an interactive A100 job that generated `ar_coating_blackjax_optimization.png`. The useful pattern is not autonomy over days; it is compression of the glue work around scientific code that sits between a changing library API and a working research artefact.

## 1. Motivation

The underlying project was an optical-coating optimisation workflow: a JAX implementation of code related to the public repository [`zwei-beiner/Code`](https://github.com/zwei-beiner/Code). The local script used BlackJAX nested sampling, but the installed development version of BlackJAX had changed its `blackjax-ns` interfaces since the script was written.

That kind of breakage is common in research code. The scientific idea has not changed, but the route to running it has: imports move, named tuple fields are renamed, state objects are reshaped, and the working cluster environment has its own module and GPU constraints. The case study is about making that interface layer tractable without the researcher manually spelunking through every new API surface.

## 2. Principles

### 2.1 Let the Agent Inspect the Live API

The session did not rely on memory of BlackJAX. After creating the virtual environment and installing `jax[cuda12]`, the agent imported the installed package, listed the relevant namespaces, and used Python introspection on functions and state objects before editing the sampler.

That matters because the failure mode was interface drift. The correct source of truth was the live installed package, not old documentation or guesses about what changed.

### 2.2 Keep the Scientific Shape Intact

The script mixed continuous coating thicknesses with discrete material choices. The patch preserved that shape: covariance adaptation was applied to the continuous thickness parameters, while material choices remained discrete. The repair was therefore not just "make imports stop failing"; it had to respect the structure of the sampler.

### 2.3 Verify Before Spending GPU Time

The agent ran the patched script on CPU first to catch ordinary Python and JAX errors before requesting a GPU allocation. Only after the CPU smoke test completed did it launch the interactive A100 job with `srun`.

That is the transferable workflow: inspect, patch, smoke-test cheaply, then spend scarce accelerator time.

## 3. What Required Human Intervention

The human contribution was concentrated into one prompt, but that prompt carried the project context and the success criterion:

- **Environment target**: create a new virtual environment with the latest available Python on the system.
- **Dependency target**: install JAX with GPU support and the development BlackJAX repository.
- **Repair target**: analyse `sampler.py` and update it for the current `blackjax-ns` API.
- **Execution target**: use an interactive GPU job, not just a local import test.
- **Artefact target**: produce the output PNG.

The transcript does not show adversarial external review, a human design debate, or multiple correction rounds. This is a short operational case, not a claim that the agent independently validated the scientific model.

## 4. The Workflow

1. Inspect the working directory and identify the Python script to repair.
2. Load the available Python module and create a fresh `venv`.
3. Install `jax[cuda12]`, development BlackJAX, and the domain dependencies.
4. Introspect the installed BlackJAX nested-sampling API directly from Python.
5. Patch imports, kernel construction, state access, finalisation, and precision settings in `sampler.py`.
6. Run a CPU smoke test to catch interface and dtype errors.
7. Submit an interactive A100 run with `srun`.
8. Check that `ar_coating_blackjax_optimization.png` was produced.

## 5. What Happened

The session lasted 20.3 minutes wall-clock on 5 May 2026. The transcript contains one substantive human prompt, 53 assistant entries, and 32 tool calls: 22 shell commands, one file read, one tool search, and eight edits.

The main API updates recorded in the final assistant summary were:

- `compute_covariance_from_particles` became `particles_covariance_matrix`.
- The slice-kernel construction moved to a new `build_kernel(slice_fn, max_steps, max_shrinkage)` shape.
- The inner kernel was rewritten around `update_with_mcmc_take_last`.
- Nested-sampling state access moved from fields such as `state.loglikelihood` and `state.logZ` to `state.particles.loglikelihood` and `state.integrator.logZ`.
- Finalisation returned particles through a `StateWithLogLikelihood` object, requiring `.position` and `.loglikelihood` access.
- `jax_enable_x64` was disabled because `tmmax` 1.1.4 hardcoded `complex64` internally.

The final GPU run used an interactive GPU job on an A100, completed sampling at roughly 400 dead points per second, and produced `ar_coating_blackjax_optimization.png` with final log-evidence around `-42664`.

## 6. Reproducibility

- Reference code context: [`zwei-beiner/Code`](https://github.com/zwei-beiner/Code).
- Local artefact: `ar_coating_blackjax_optimization.png`.
- Session JSONL: private Claude Code transcript.
- Public status: the repaired local working tree and output image were not public at the time this recipe was drafted.

## 7. Limitations

**Scientific validation.** The transcript verifies that the script ran and produced the requested plot. It does not prove that the optical model, likelihood, or nested-sampling configuration were scientifically optimal.

**No adversarial review.** Unlike the longer `jaxwavelets` case study, this session did not include external LLM review. The evidence is execution-based rather than review-based.

**Private artefacts.** The patched `sampler.py`, generated PNG, and JSONL transcript are not public, so external readers cannot independently replay the session from this page alone.

**Single prompt.** Because the session had one substantive human prompt, it shows operational compression rather than a rich human-agent design dialogue.

## Methods note

Timing was computed from the line-delimited Claude Code transcript using the 5-minute-cap adjacent-pair method. The headline active-computation total sums three retained pair categories: tool execution, AI thinking to text, and AI thinking to tool call. Human-response gaps and continuation after the human prompt are reported separately rather than folded into the active total.

| Category | Time | Count | What it measures |
|----------|------|-------|-----------------|
| Tool execution (assistant(tool_use) -> user(tool_result)) | 11.72 min | 31 | Wall-clock time for Bash, file I/O, tool search, and edits |
| AI thinking -> text (user(tool_result) -> assistant(text)) | 2.00 min | 18 | Token generation producing text output after a tool result |
| AI thinking -> tool (user(tool_result) -> assistant(tool_use)) | 0.91 min | 13 | Token generation producing the next tool call after a tool result |
| **Total active computation** | **14.64 min** | | |
| AI continuation after human prompt (user(prompt) -> assistant(*)) | 0.05 min | 1 | Reported separately; not in active total |
| Human response gap (assistant(text) -> user(prompt)) | 0.00 min | 0 | No human follow-up prompt occurred during the analysed task |

The wall-clock span was 20.3 minutes, from `2026-05-05T09:07:08Z` to `2026-05-05T09:27:28Z`, giving an active/wall-clock ratio of about 72%. There were no gaps longer than 30 minutes, so no stall or sleep-break adjudication was required.

Prompt-count audit:

| Class | Count |
|-------|-------|
| Real user prompts | 1 |
| Tool results | 32 |
| Command-message injections | 1 |
| System/local-only entries | 2 |
| Request-interrupted entries | 0 |
| Task notifications | 0 |

Tool-call breakdown:

| Tool | Count |
|------|-------|
| Bash | 22 |
| Read | 1 |
| ToolSearch | 1 |
| Edit | 8 |
