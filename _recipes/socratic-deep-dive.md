---
id: socratic-deep-dive
title: "Building technical understanding through Socratic AI dialogue"
category: "Context Engineering"
timebox: "One focused session"
status: "Complete"
summary: "Eighteen targeted exchanges with an AI, starting from a high-level question about IMEX Runge-Kutta solvers, built precise connected understanding of a topic scattered across specialist literature — ending in a publishable reference document."
outcome: "A comprehensive 4,000-word technical document on IMEX-Rosenbrock-Wanner methods, covering theory, derivation, and application to CMB Einstein-Boltzmann equations — a document no single reference contains."
evidence: "Full conversation transcript (18 exchanges). Terminal artefact: structured markdown synthesising IMEX-RK foundations, Rosenbrock linearisation, W-methods, coefficient derivation, and CMB application, commissioned directly from the dialogue."
demo_url:
repo_url:
author: "Lawrence Berry, Institute of Astronomy, University of Cambridge"
date: 2026-05-05
---

## Abstract

Numerical methods literature on IMEX Runge-Kutta solvers, Rosenbrock linearisation, and W-methods is scattered across specialist papers, each assuming fluency in the others. A textbook teaches what its author judged important; a Socratic AI dialogue lets you chase exactly the threads *you* find confusing or interesting, at the depth *you* need, connected to *your* domain. Eighteen exchanges — starting from "how do IMEX RK methods work?" — produced precise, connected understanding of a topic that normally requires weeks of literature study, ending in a publishable 4,000-word reference document that no single source contains.

## 1. What a Textbook Cannot Do

A standard treatment of IMEX methods covers the stage equations and order conditions. What it rarely does:

- Walk through the *derivation* of the Rosenbrock stage equation step by step, starting from a standard DIRK method and arriving at the master linear solve via a Taylor expansion.
- Clarify the distinction between the exact implicit state $\mathbf{Y}_i^{\text{exact}}$ and the explicit predictor $\tilde{\mathbf{Y}}_i$, and what it means operationally.
- Connect additive splitting (ARK) to partitioned splitting (PRK) and show when they collapse to the same method.
- Apply the theory directly to the CMB Einstein-Boltzmann equations — a system where the stiffness is a time-varying Thomson scattering term, not a permanently stiff variable.

A Socratic dialogue builds all of this, because the student controls the depth at every step. The AI never tires of going deeper on a specific confusion, and never simplifies a follow-up because the textbook chapter is already overlong.

## 2. Three Principles

### 2.1 Enter at the Boundary of Your Understanding

Start with a question that is neither trivial nor completely foreign. "What is a Runge-Kutta method?" is too basic; "derive the B-series for a third-order IMEX-W method" assumes fluency you haven't built yet. The productive entry is the question you would ask a patient expert over coffee — the thing you know *about* but haven't internalised.

In this session, that question was: *"Please explain how IMEX RK ODE solver methods work and how they are derived."* This is a genuine research-adjacent question, not a homework exercise. The AI produced a complete, technically precise answer, and the rest of the session was driven by drilling into the parts of that answer that were new.

### 2.2 Ask for Elaboration on Specific Parts, Not General Follow-Ups

"Tell me more" is weak. "Please elaborate on section 2" — pointing at the specific part of the previous answer — produces depth rather than breadth. The questions that drove the most learning in this session were surgical:

- *"Elaborate on the step 3 solve for $Y_i$ and generalise your explanation to a vector state $Y_i$"* — forced a full treatment of the Newton-Raphson loop and Jacobian-Free Newton-Krylov.
- *"Please elaborate on how the master equation shown in step 2 is derived"* — produced the four-step derivation from idealized DIRK through Taylor expansion to the linear solve.
- *"Please elaborate how you derive the equation for $Y_i^{\text{exact}}$ in Step 1 from the general $y' = f(y,t) + g(y,t)$"* — unpacked the slope-notation bridge that numerical methods papers often skip.

Each of these produced a section of the final document. The document is, in effect, the conversation's elaboration tree, harvested.

### 2.3 Test Understanding by Proposing Your Own Hypothesis

The most valuable exchanges were not questions but hypotheses. The student proposes a conjecture; the AI confirms, corrects, or refines it. This is faster than asking an open question and more diagnostic — it exposes exactly where the mental model is wrong.

The pivotal exchange in this session:

> *"Which is more appropriate for the first order CMB Einstein-Boltzmann equations? PRK or ARK? My guess is ARK as it is specific coupling forces that cause stiffness, it's not true to say a particular variable is always stiff?"*

The AI confirmed the intuition and extended it: the stiffness comes from a single physical term ($\dot{\tau}$, the Thomson scattering rate), which is time-varying. After recombination $\dot{\tau} \to 0$, and the implicit solver organically degenerates to explicit — no dynamic switching needed. This is not in any textbook treatment of IMEX methods. It emerged because the student proposed a concrete hypothesis from their research domain.

Similarly:

> *"If I use Gershgorin circle theorem to split my linear ODE system into stiff and non-stiff rows, is this equivalent to partitioning my state vector?"*

This produced a proof of equivalence between ARK and PRK for row-split linear systems, and the observation that for a 10,000-variable system where only 50 rows are stiff, the implicit solve reduces from a $10000 \times 10000$ matrix to a $50 \times 50$ matrix. A genuinely useful result that the student derived by connecting two ideas.

## 3. What Required Human Judgment

The AI answered every question. The student had to know which questions to ask.

**Choosing the right entry level.** Starting at IMEX rather than at "what is a Butcher tableau?" required knowing roughly where the conceptual gap was. Starting too early wastes the session on basics already understood.

**Recognising incomplete answers.** The Rosenbrock derivation initially elided the step from the idealized DIRK equation to the slope-notation form. *"Please elaborate how you derive the equation for $Y_i^{\text{exact}}$"* was a correction, not a continuation — the student noticed the gap.

**Connecting to the research domain.** The CMB question required knowing that the Einstein-Boltzmann equations have a stiff scattering term, and that this term is time-varying. Without that domain knowledge, the question cannot be formed.

**Commissioning the synthesis.** The session ended with: *"Refactor this conversation into a more coherent structure... Do not miss any detail from this conversation. Write your resulting coherent explanation into a markdown file."* The document was the explicit goal of the final exchange. Without the commission, the understanding would have remained in the dialogue — present but unharvested.

## 4. The Workflow

1. Identify a technical topic at the edge of your understanding — something you've encountered in the literature but haven't internalised.
2. Open a fresh dialogue with a focused, non-trivial opening question.
3. After each answer, identify the *one part* you most want to go deeper on. Ask for elaboration by pointing at that specific part.
4. When you have a conjecture about something — especially a connection to your research domain — state it as a hypothesis and ask for confirmation or correction.
5. Periodically ask the AI to reformulate the system in a different notation or for a different audience. This surfaces hidden assumptions.
6. At the end, commission a synthesis: *"Rewrite everything we've discussed as a coherent document."* This is the artefact.

The dialogue itself is ephemeral; the synthesis document is durable. Both are worth keeping — the dialogue shows the learning path, the document is the result.

## 5. What Happened

The session covered:

| Exchange | Topic |
|----------|-------|
| 1 | IMEX-RK overview: splitting, stage equations, update rule |
| 2 | Butcher tableaux: structure, explicit vs. implicit, RK4 example |
| 3 | Vectorised Newton-Raphson solve for $\mathbf{Y}_i$ |
| 4 | Rosenbrock methods: linearisation, single linear solve per stage |
| 5 | Rosenbrock derivation: Taylor expansion of stiff term |
| 6 | Rosenbrock-Wanner (W-methods): approximate Jacobians, order conditions |
| 7 | IMEX-Rosenbrock combination: the master equation |
| 8 | Derivation of master equation: four steps from DIRK to linear solve |
| 9 | Whether $\tilde{\mathbf{Y}}_i$ requires tracking two state vectors (it doesn't) |
| 10 | Derivation of $\mathbf{Y}_i^{\text{exact}}$ from the general non-autonomous system |
| 11 | $\tilde{\mathbf{Y}}_i$ for additive RK: explicit predictor construction |
| 12 | Computing the coefficients: order conditions, Butcher trees, free parameters |
| 13 | Partitioned RK: when to split the state vector vs. the forcing terms |
| 14 | Gershgorin circle theorem splitting: equivalence to PRK for row-split linear systems |
| 15 | When ARK and PRK are not equivalent |
| 16 | CMB Einstein-Boltzmann equations: ARK is correct; Thomson scattering as the stiff term |
| 17 | Whether the stiff/non-stiff split must be determined dynamically at runtime (it need not be) |
| 18 | Synthesis: comprehensive structured document commissioned from the dialogue |

The session moved from introductory (exchange 1) to research-adjacent (exchanges 13–17) in under two hours. The terminal document runs to approximately 4,000 words, covering all eighteen topics in a coherent sequence that a textbook chapter on IMEX methods would not replicate.

## 6. Limitations

**The student must already know enough to ask.** The Gershgorin question and the CMB question both required prior domain knowledge. This method accelerates learning inside a field you partly understand; it is less effective for crossing disciplinary boundaries from scratch.

**The AI can be confidently wrong on specialised details.** The derivations in this session are correct, but numerical methods is a domain where subtleties matter — sign conventions, summation limits, the precise meaning of "stage derivative" vs. "stage value". Every derivation should be checked against a primary source before being used in production code or a paper.

**The synthesis document is a summary, not a proof.** The document produced is a coherent exposition, not a verified derivation. It captures the learning; it is not a substitute for reading Hairer, Wanner, and Nørsett.

**Dialogue is ephemeral without the commission step.** Understanding without an artefact dissipates quickly. The synthesis commission at the end of the session is not optional — it is what converts the dialogue into something durable and shareable.
