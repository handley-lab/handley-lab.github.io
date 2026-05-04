---
layout: page
title: Case Studies
permalink: /case-studies/
---
These examples show the lab's practical workflow: supervised execution where humans define intent and verify correctness while AI handles implementation overhead.

<section class="feature-list">
  {% for study in site.data.case_studies %}
    {% include case_study_card.html study=study variant="archive" %}
  {% endfor %}
</section>
