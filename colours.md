---
layout: page
title: Colour card
permalink: /colours/
---
Every colour on this site comes from the tokens below, defined in `_sass/minima/custom-styles.scss` (neutrals, brand, feature) and `_data/research_areas.yml` (topics). Use the token, never a raw hex value, so pages stay consistent in light and dark mode. Use the theme toggle in the header to see the dark versions.

{% assign neutrals = "canvas:Page background|panel:Panel background|panel-strong:Cards inside panels|ink:Body text and headings|ink-soft:Secondary text, captions|line:Borders and dividers" | split: "|" %}
{% assign brand = "accent:Primary buttons, links|accent-2:Highlights, active states, card edges|accent-3:Small kicker labels|tint:Soft highlight behind chips and tags|header-bg:Header bar" | split: "|" %}
{% assign feature = "feature-bg:Homepage statement block|feature-ink:Text on the feature block|feature-soft:Secondary text on the feature block|feature-edge:Feature block border" | split: "|" %}

## Neutrals

<ul class="swatch-grid">
{%- for item in neutrals -%}
  {%- assign parts = item | split: ":" -%}
  <li><span class="chip" style="background: var(--{{ parts[0] }})"></span><code>--{{ parts[0] }}</code><span class="use">{{ parts[1] }}</span></li>
{%- endfor -%}
</ul>

## Brand

<ul class="swatch-grid">
{%- for item in brand -%}
  {%- assign parts = item | split: ":" -%}
  <li><span class="chip" style="background: var(--{{ parts[0] }})"></span><code>--{{ parts[0] }}</code><span class="use">{{ parts[1] }}</span></li>
{%- endfor -%}
</ul>

## Feature

The same in both themes, so the homepage statement reads as one solid block.

<ul class="swatch-grid">
{%- for item in feature -%}
  {%- assign parts = item | split: ":" -%}
  <li><span class="chip" style="background: var(--{{ parts[0] }})"></span><code>--{{ parts[0] }}</code><span class="use">{{ parts[1] }}</span></li>
{%- endfor -%}
</ul>

## Topics

One colour family per research theme, used by the homepage research diagram, the papers map, the GPU/AI statement lines and recipe accents. `--topic-<key>` is for text, headings and borders; `--topic-<key>-mark` for dots, bars, bubbles and lines.

{% assign ra = site.data.research_areas %}
{% assign topics = ra.fields | unshift: ra.centre %}
<ul class="swatch-grid">
{%- for t in topics -%}
  <li><span class="chip" style="background: var(--topic-{{ t.key }})"></span><code>--topic-{{ t.key }}</code><span class="use">{{ t.label }}: text</span></li>
  <li><span class="chip" style="background: var(--topic-{{ t.key }}-mark)"></span><code>--topic-{{ t.key }}-mark</code><span class="use">{{ t.label }}: marks</span></li>
{%- endfor -%}
</ul>
