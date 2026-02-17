---
layout: page
title: Case Studies
permalink: /case-studies/
---
These examples show the lab's practical workflow: supervised execution where humans define intent and verify correctness while AI handles implementation overhead.

<section class="feature-list">
  {% for study in site.data.case_studies %}
    <article class="feature-card">
      <p class="feature-card-meta">{{ study.timebox }} · {{ study.status }}</p>
      <h2>{{ study.title }}</h2>
      <p>{{ study.summary }}</p>
      <p><strong>Outcome:</strong> {{ study.outcome }}</p>
      <p><strong>Evidence:</strong> {{ study.evidence }}</p>
      <div class="feature-links">
        {% if study.demo_url %}
          <a href="{{ study.demo_url }}" target="_blank" rel="noopener noreferrer">Demo</a>
        {% endif %}
        {% if study.repo_url %}
          <a href="{{ study.repo_url }}" target="_blank" rel="noopener noreferrer">Repository</a>
        {% endif %}
      </div>
    </article>
  {% endfor %}
</section>
