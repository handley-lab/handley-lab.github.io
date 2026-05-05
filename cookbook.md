---
layout: page
title: AI Cookbook
permalink: /cookbook/
---
A growing collection of recipes for doing science with AI assistance. Each recipe captures a workflow pattern — aim, approach, result — that another researcher can pick up and adapt. Some recipes are short cards; others have a fuller companion write-up linked from the card.

The recipes here are practical, not promotional. We are interested in *what becomes newly possible* — new ways to think, debate, draft, and verify — not in efficiency boasts. If a recipe has a "Read full recipe" link, that's the deeper write-up; if it doesn't, the card is the recipe.

<section class="feature-list">
  {% for recipe in site.data.recipes %}
    {% include recipe_card.html recipe=recipe variant="archive" %}
  {% endfor %}
</section>
