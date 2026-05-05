---
layout: page
title: Case Studies
permalink: /case-studies/
---
These examples show the lab's practical workflow: supervised execution where humans define intent and verify correctness while AI handles implementation overhead.

There are two formats here. **Recipe cards** are short, browseable patterns — aim, approach, result, evidence — that another researcher can copy. **Long-form case studies** are fuller audit trails for substantial software or research workflows, with methods notes and reproducibility links.

## Recipe cards

Short patterns that can be read in a few minutes.

<section class="feature-list case-study-section case-study-section-recipes">
  {% for study in site.data.case_studies %}
    {% if study.format == "recipe" %}
      {% include case_study_card.html study=study variant="archive" %}
    {% endif %}
  {% endfor %}
</section>

## Long-form case studies

Fuller narratives with methods notes, verification details, and reproducibility links.

<section class="feature-list case-study-section case-study-section-long-form">
  {% for study in site.data.case_studies %}
    {% unless study.format == "recipe" %}
      {% include case_study_card.html study=study variant="archive" %}
    {% endunless %}
  {% endfor %}
</section>
