---
id: voice-note-paper-debate
title: "Real-time research dialogue"
category: "Research Workflow"
timebox: "One session"
status: "Complete"
proposer: "Toby Lovick"
summary: "Feed a live-transcribed conversation into Claude sentence-by-sentence for immediate feedback on research discussions. Enables three-way debates between researchers and Claude in real-time, without context-switching or friction."
outcome: "Understand papers and discuss methodology in real-time, generating novel research directions within the flow of conversation."
evidence: "2026-05-01 session: Discussed Park et al. blended light curves paper with Alex in a cafe using Whisper transcription + Claude hooks. Generated novel analysis direction (forward-modeling expected time delays from large-scale structure) during the debate."
demo_url:
repo_url: "https://github.com/tobyLovick/recordCLI"
author: "Toby Lovick"
date: 2026-05-05
---

## The pattern

On Friday mornings, our group meets to do a "breadth-first" search of astro-ph-co, to catch up and discuss any papers of interest to the group (think junior doctors being grilled while doing rounds). Last week we ran into this very interesting paper [2604.27511](https://arxiv.org/abs/2604.27511), which looks at being able to detect strong lensing systems when the lens images are overlapping. After the arxiv scroll Alex and I headed to cafe to work, as we often do, and because he works on strong lensing and I'm interested generally in Bayesian model comparison we got to talking about this paper and about how we would approach the problem.

I recently built a command line app I've called "recordCLI", which hooks up my computers microphone to OpenAI's [Whisper](https://github.com/openai/whisper), so that I can locally transcribe. This was a fairly noisy cafe, we were sat close to another table, and there was music playing in the background, but luckily whisper is really solid, and can very well extract the closest voice from what sounds like a very noisy mp3. So, I set up my recorder in "--live-update" mode, and we started talking.

As we started I loaded up a claude terminal, used an MCP to download and read the source files of the paper, and then took my hands completely off the keyboard. Instead of a two-person debate between people who haven't fully read the paper, you have a three-person conversation where one participant (Claude) has read it perfectly, and the other two bring intuition and domain expertise.

## Setup

1. **Start recording with your `record` CLI app** — this transcribes live speech using Whisper and saves a timestamped transcript file.
2. **Download the paper TeX source** from arXiv (or any reference you want to discuss).
3. **Configure a Claude Code hook** to feed the transcript into your Claude session as it updates. Use markers in your prompt to tell Claude where to read and respond.

The entire setup takes ~20 seconds because the record CLI is low-friction by design. No effort because you were just talking.

## What emerged in practice

In a one-hour session discussing blended light curves in gravitational lensing we:

- **Debated** whether small time delays in lensed supernovae were physical/erroneous/suspicious (noise vs. signal)
- **Questioned** the choice of model-selection metric (DIC) and its false-positive rates
- **Discussed** alternate noise modeling approaches (Gaussian processes for correlated noise)
- **Converged** on a novel analysis direction: forward-modeling the distribution of expected time delays from cosmology + large-scale structure, to set a baseline for "is this time delay anomalous?"

The last idea emerged mid-conversation because Claude could see the debate unfold in real-time and was able to shoot down ideas as they came up. Since neither Alex nor I can touch-type very fast, it wouldn't have been possible to consistently query Claude as we were speaking, nor would it have been possible for us to take notes on the conversation properly. Instead, we produced a live transcript of how we were thinking, how we might apply or change methods from the paper, and all of our reasoning.

I think there are 3 main benefits to what we did.
1- By live transcribing, we could set Claude off to begin working on our approach, searching for the paper's repo, investigating if the code was JAX-native etc. We were already assessing the technical viability of the project while continuing to debate how we might approach the problem
2- Since Claude can access the source from Arxiv, it was able to pull us up on details, we had read the abstract and results of the paper but by having an agent live responding to the conversation, we were able to query implementation details without searching through the paper's appendices with a fine-toothed comb. By engaging with the analysis in a very technical way (but without having to write test code) we were able to get a hands-on learning experience with the paper over the course of two coffees.
3- One can imagine that after building up a collection of these conversations, you would start to get a useful training set (not for LLMs, but for yourself) of your working patterns, and which kind of projects and ideas tend to work and not work.

The buzzword tagline for this would be "Science at the Speed of Conversation"; over the course of an hour we had explored a few avenues of how to approach a new analysis, had a few misunderstandings cleared up, and had created a decent project proposal, of real scientific interest. At the risk of sounding lazy, doing this with practically zero typing meant this didn't feel like working at all; after all we are physics students and we quite like talking about science!

## Limitations

- **Transcription errors**: Whisper occasionally misses domain-specific terms or misparses technical jargon. You may need to re-explain or correct a transcript line. Future transcription software (or if my laptop had a GPU) would allow you to run a larger, more accurate model.
- **Async latency**: Claude can't interrupt the conversation in real-time — you have to decide when to pause and ask for input.
- **Context window**: Very long conversations would hit Claude's context limit. You may need to summarize, pause, or start a fresh session.
- **Privacy**: It is local transcription, however if that's plugged into Claude then your conversation is fed through Claude's API. Maybe use discretion with unpublished work, sensitive discussions, or content you want to keep private.
- **Real-time feedback loop**: This isn't simultaneous conversation — you're speaking, pausing for Claude's response, then continuing. It's fast but not literally real-time.

## Try it yourself

- Clone the `record` CLI repo and configure your transcription hook.
- Pick a paper you've been meaning to discuss with someone.
- Grab a colleague (or rant at a waiter)
- Start recording. Use markers to tell Claude when to read your conversation and respond.

---

## N.B.

My computer has an Intel i7-1370P with 62GB RAM and integrated Iris Xe graphics (no dedicated GPU). With these I can live transcribe using whisper's "small" model (which does well but struggles with proper nouns) with about 5 seconds of delay. Your mileage may vary!

*Transcription powered by OpenAI's Whisper. This recipe emerged from a May 2026 discussion with Alex Drane on gravitational lensing and supernova detection.*
