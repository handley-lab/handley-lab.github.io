---
layout: page
title: Skills Marketplace
permalink: /skills/
---
The marketplace is where reusable research capabilities live. We encode durable know-how as skills and expose actions as MCP tools.

<p>
  Core repository:
  <a href="https://github.com/fundamental-physics/marketplace" target="_blank" rel="noopener noreferrer">
    github.com/fundamental-physics/marketplace
  </a>
</p>

<section class="feature-list">
  {% for skill in site.data.skills %}
    <article class="feature-card">
      <p class="feature-card-meta">{{ skill.category }} · {{ skill.maturity }}</p>
      <h2>{{ skill.name }}</h2>
      <p>{{ skill.description }}</p>
      <div class="feature-links">
        <a href="{{ skill.url }}" target="_blank" rel="noopener noreferrer">Open</a>
      </div>
    </article>
  {% endfor %}
</section>
