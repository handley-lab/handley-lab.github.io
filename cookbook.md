---
layout: cookbook
title: AI Cookbook
permalink: /cookbook/
---
{% include katex.html %}
A growing collection of recipes for doing science with AI assistance. Each recipe captures a workflow pattern — aim, approach, result — that another researcher can pick up and adapt. Some recipes are short cards; others have a fuller companion write-up linked from the card.

The recipes here are practical, not promotional. We are interested in *what becomes newly possible* — new ways to think, debate, draft, and verify — not in efficiency boasts. If a recipe has a "Read full recipe" link, that's the deeper write-up; if it doesn't, the card is the recipe.

{% assign finished = site.data.recipes | where: "status", "Complete" %}
{% assign developing = site.data.recipes | where_exp: "r", "r.status != 'Complete'" %}

  <div class="cookbook-main">
    <p class="cookbook-count" aria-live="polite"></p>
    <section class="feature-list recipe-list">
      {%- comment -%} Finished recipes first; Stub / Draft / In progress follow, dimmed and labelled. {%- endcomment -%}
      {% for recipe in finished %}
        {% include recipe_card.html recipe=recipe variant="archive" %}
      {% endfor %}
      {% for recipe in developing %}
        {% include recipe_card.html recipe=recipe variant="archive" %}
      {% endfor %}
    </section>
    <p class="cookbook-empty" hidden>No recipes match these filters.</p>
  </div>

<script>
(function () {
  var root = document.querySelector('.cookbook-page');
  if (!root) return;
  var cards = root.querySelectorAll('.recipe-card');
  var stateChips = root.querySelectorAll('.cookbook-chip[data-state]');
  var tagChips = root.querySelectorAll('.cookbook-chip[data-tag]');
  var clear = root.querySelector('.cookbook-clear');
  var count = root.querySelector('.cookbook-count');
  var empty = root.querySelector('.cookbook-empty');
  var state = 'all';
  var tags = new Set();

  function apply() {
    var shown = 0;
    cards.forEach(function (card) {
      var ok = (state === 'all' || card.dataset.state === state) &&
               (tags.size === 0 || tags.has(card.dataset.tag));
      card.hidden = !ok;
      if (ok) shown++;
    });
    stateChips.forEach(function (c) { c.setAttribute('aria-pressed', c.dataset.state === state); });
    tagChips.forEach(function (c) { c.setAttribute('aria-pressed', tags.has(c.dataset.tag)); });
    clear.hidden = state === 'all' && tags.size === 0;
    empty.hidden = shown > 0;
    count.textContent = 'Showing ' + shown + ' of ' + cards.length + ' recipes';
  }

  stateChips.forEach(function (c) {
    c.addEventListener('click', function () { state = c.dataset.state; apply(); });
  });
  tagChips.forEach(function (c) {
    c.addEventListener('click', function () {
      var t = c.dataset.tag;
      tags.has(t) ? tags.delete(t) : tags.add(t);
      apply();
    });
  });
  clear.addEventListener('click', function () { state = 'all'; tags.clear(); apply(); });
  apply();
})();
</script>
