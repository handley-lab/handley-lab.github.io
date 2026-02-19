---
layout: page
title: The New Scientific Method
permalink: /method/
---
Code is cheap. Truth is expensive. When implementation and exposition can be produced at negligible marginal cost, the limiting resource in research is no longer keystrokes but judgement: what to build, what to trust, and what to discard. This page makes explicit how we organise our research practice under that constraint.

## Two Revolutions

The first revolution is hardware. The GPU ecosystem, built to service machine learning, now accelerates classical scientific computation by factors of 100–1000× when algorithms can be vectorised and kept on-device. In our area this changes the practical scope of Bayesian inference: nested sampling, marginalisation over large numbers of nuisance parameters, and systematic model comparison become routine rather than exceptional.

The second revolution is procedural. Large language models reduce the fixed costs of software development and the surrounding overhead: building interfaces, writing tests, translating between languages, navigating legacy codebases, and producing documentation. The analogy we find useful is the CCD transition: digitisation did not change astrophysics, but it changed the economics of data acquisition. LLMs change the economics of code and text production, and thereby shift the equilibrium of research methods.

## Three Approaches to AI in Science

Current uses of AI in research fall into three categories. First, foundation models trained as general scientific surrogates. Second, autonomous agents that attempt end-to-end generation of research artefacts. Third, supervised execution, where human intent and verification remain central and AI executes the implementation steps.

We work in the third regime. The pragmatic reason is the 80/20 structure of academic labour: most time is consumed by tasks that are necessary but not intrinsically scientific, while the minority is spent on selection and interpretation. LLMs are effective at generation — proposing code, drafts, and alternatives — but weak at selection, in the sense of defending truth claims under adversarial scrutiny. Our workflow therefore emphasises generation followed by deliberate selection, rather than granting autonomy and hoping that selection emerges.

## Six Principles

1. **Capture content.** Systematically transcribe, photograph, and archive to build a knowledge base that extends the effective context of our tools.
2. **Engineer context.** The model is only as good as what it can see. We organise knowledge — skills, conventions, physics — rather than perfecting prompt syntax.
3. **Specify physics, not code.** State the physical intent and mathematical requirements explicitly. Treat generated code as a product to be tested, not a script to be written.
4. **Verify rigorously.** Require verification as a first-class deliverable, not an afterthought. Floating-point regression tests, simulation-based calibration, independent checks.
5. **Use multiple models.** One system implements, another critiques. We do not rely on a single channel of generation.
6. **Stay the scientist.** Define the questions, choose the methods, and take responsibility for the answers.

## Verification as Method

If AI makes it easier to produce plausible code, it also makes it easier to produce subtle errors. The intellectual core of our methodology is therefore verification — understood not as a final sanity check but as the primary means by which we buy trust.

We rely on three complementary strategies. First, **reference outputs**: when porting a likelihood, simulator, or template model, we demand floating-point agreement against a known-good implementation, because downstream inference amplifies small discrepancies. Second, **simulation-based calibration**: for inference pipelines, we validate that posterior quantiles behave correctly under repeated simulation, forcing us to test the full pipeline rather than favoured examples. Third, **adversarial review**: independent implementations or reviewers with incentives aligned towards finding failure modes.

A useful example from our own work: during a GPU rewrite of the SNANA supernova simulation pipeline, point-by-point comparison against the legacy C code revealed a subtle bug in the original dust law implementation. The bug was found *because* the rewrite forced a level of scrutiny that years of manual development had not. The relevant skill is no longer typing speed or syntax recall, but the ability to design tests that fail when something is wrong.

### A typical supervised-execution loop

1. **Specify intent:** state the physical requirement, invariants, and reference behaviour.
2. **Generate:** allow the model to propose code and tests.
3. **Critique independently:** run an adversarial review (a different model or reviewer) focused on failure modes.
4. **Test for parity:** demand quantitative agreement against a reference implementation.
5. **Escalate checks:** simulation-based calibration, analytic limits, dimensional analysis, as appropriate.
6. **Document decisions:** record what was changed and why.

## The Debate

The methodological tension has been stated sharply in recent work. Trotta argues that widespread code generation risks breaking the "trust loop" between scientist and computational object ([arXiv:2602.10165](https://arxiv.org/abs/2602.10165)). Hogg counters that the bottleneck moves from writing to verifying, and that verification is itself a scientific skill that can be formalised and improved ([arXiv:2602.10181](https://arxiv.org/abs/2602.10181)).

Both positions describe real failure modes and real opportunities. Unverified generation creates brittle science; lowered implementation cost allows higher standards of validation. A workable equilibrium is to treat verification as the method: we permit cheap generation, but we make selection expensive, deliberate, and documented.

## The Challenge

If producing code and text were virtually free, what would you do differently as a scientist?
