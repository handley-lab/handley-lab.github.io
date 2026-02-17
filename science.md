---
layout: page
title: Group Science
permalink: /science/
---
We develop statistical and computational methods for cosmology, gravitational waves, and time-domain astrophysics, with a focus on Bayesian inference, scalable GPU workflows, and robust scientific software.

## Research Summary
Our work spans the primordial Universe, inflation, dark energy, dark matter, 21-cm cosmology, CMB inference, and gravitational-wave astrophysics. Methodologically, we build high-impact tools for nested sampling, simulation-based inference, and practical research infrastructure.

## Current Highlights
<section class="feature-list">
  {% for item in site.data.science %}
    <article class="feature-card">
      <p class="feature-card-meta">{{ item.theme }}</p>
      <h2>{{ item.title }}</h2>
      <p>{{ item.summary }}</p>
      <p><strong>Examples:</strong> {{ item.examples }}</p>
      <div class="feature-links">
        {% if item.link %}
          <a href="{{ item.link }}" target="_blank" rel="noopener noreferrer">Representative reference</a>
        {% endif %}
      </div>
    </article>
  {% endfor %}
</section>

## Scientific Software
- [PolyChord](https://arxiv.org/abs/1506.00171)
- [anesthetic](https://arxiv.org/abs/1905.04768)
- [GLOBALEMU](https://arxiv.org/abs/2104.04336)
- [maxsmooth](https://arxiv.org/abs/2007.14970)
- [margarine](https://arxiv.org/abs/2205.12841)
- [fgivenx](https://arxiv.org/abs/1908.01711)
- [nestcheck](https://arxiv.org/abs/1804.06406)

## Source Talks
- [Imperial Jan 2026: Two Revolutions](https://github.com/williamjameshandley/talks/tree/imperial_2026)
- [GAMBIT LLMBit Dec 2025: AI/ML Tools for Research](https://github.com/williamjameshandley/talks/tree/gambit_llmbit_2025)
- [Internal Lab Talk Jan 2026: Prompt to Context Engineering](https://github.com/handley-lab/internal-talks/tree/2026_new_year)
- [KICC AI Tools Jul 2025](https://github.com/williamjameshandley/talks/tree/kicc_ai_tools_2025)
