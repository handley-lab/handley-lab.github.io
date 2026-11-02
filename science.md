---
layout: page
title: Group Science
permalink: /science/
---
We develop statistical and computational methods for cosmology, gravitational waves, and time-domain astrophysics, with a focus on Bayesian inference, scalable GPU workflows, and robust scientific software.

## GPUs for Science

GPU hardware — developed for machine learning — accelerates classical statistical methods by 100–1000× for rigorous astrophysics. These speedups enable systematic Bayesian model comparison at scales that were previously intractable.

<section class="feature-list">
  {% for item in site.data.science %}
    {% if item.area == "GPUs for Science" %}
      {% include science_card.html item=item %}
    {% endif %}
  {% endfor %}
</section>

## Methodology

<section class="feature-list">
  {% for item in site.data.science %}
    {% if item.area == "Methodology" %}
      {% include science_card.html item=item cta="Read more" %}
    {% endif %}
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
- [Imperial Feb 2026: The New Scientific Method](https://github.com/williamjameshandley/talks/tree/imperial_2026)
- [Imperial Jan 2026: Two Revolutions](https://github.com/williamjameshandley/talks/tree/imperial_2026)
- [GAMBIT LLMBit Dec 2025: AI/ML Tools for Research](https://github.com/williamjameshandley/talks/tree/gambit_llmbit_2025)
- [Internal Lab Talk Jan 2026: Prompt to Context Engineering](https://github.com/handley-lab/internal-talks/tree/2026_new_year)
- [KICC AI Tools Jul 2025](https://github.com/williamjameshandley/talks/tree/kicc_ai_tools_2025)
