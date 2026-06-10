---
layout: clean
nav: outreach
permalink: /outreach/
title: "Outreach"
---

<h1 class="page-title">Outreach</h1>
<p class="lead">Teaching, talks, media and service to the structural design and computational design community. </p>

<div class="marquee photostrip reveal">
  <div class="marquee-track">
    {% for half in (1..2) %}{% for rep in (1..2) %}{% for p in site.data.highlights %}
    <figure class="pitem"{% if half == 2 %} aria-hidden="true"{% endif %}>
      <img src="{{ p.image | relative_url }}" alt="{{ p.caption }}" loading="lazy">
      {% if p.caption %}<figcaption>{{ p.caption }}</figcaption>{% endif %}
    </figure>
    {% endfor %}{% endfor %}{% endfor %}
  </div>
</div>

<div class="section-head reveal"><h2>Teaching &amp; Supervision</h2><span class="bar"></span></div>

<section class="rows">
  {% assign items = site.teaching | sort: "date" | reverse %}
  {% for t in items %}
  <div class="prow text-only reveal">
    <div class="rbody">
      <p class="rmeta">{{ t.type }}{% if t.date %} &middot; {{ t.date | date: "%Y" }}{% endif %}</p>
      <h3 class="rtitle">{{ t.title }}</h3>
      <p class="rauth">{{ t.venue }}{% if t.location %} &middot; {{ t.location }}{% endif %}</p>
    </div>
  </div>
  {% endfor %}
</section>

<div class="section-head reveal"><h2>Talks &amp; Presentations</h2><span class="bar"></span></div>
<section class="rows">
  {% assign talks = site.talks | sort: "date" | reverse %}
  {% for t in talks %}
  <div class="prow text-only reveal">
    <div class="rbody">
      <p class="rmeta">{{ t.type }}{% if t.date %} &middot; {{ t.date | date: "%Y" }}{% endif %}</p>
      <h3 class="rtitle">{% if t.paperurl %}<a href="{{ t.paperurl }}" target="_blank" rel="noopener">{{ t.title }}</a>{% else %}{{ t.title }}{% endif %}</h3>
      <p class="rauth">{{ t.venue }}{% if t.location %} &middot; {{ t.location }}{% endif %}</p>
    </div>
  </div>
  {% endfor %}
</section>

<div class="section-head reveal"><h2>Organisation &amp; Service</h2><span class="bar"></span></div>
<section class="rows">
  <div class="prow text-only reveal"><div class="rbody">
    <p class="rmeta">Conference Organiser &middot; 2026</p>
    <h3 class="rtitle">Future of Construction 2026</h3>
    <p class="rauth">Organising team &middot; Zurich, 350+ attendees</p>
  </div></div>
  <div class="prow text-only reveal"><div class="rbody">
    <p class="rmeta">Co-organiser &middot; since 2021</p>
    <h3 class="rtitle">International Summer School on Historic Masonry Structures (HIMASS)</h3>
    <p class="rauth">Annual two-week summer school &middot; Anagni, Italy</p>
  </div></div>
  <div class="prow text-only reveal"><div class="rbody">
    <p class="rmeta">Founding Member &middot; since 2023</p>
    <h3 class="rtitle">COMPAS Association</h3>
    <p class="rauth">Open-source computational framework for the AEC community</p>
  </div></div>
  <div class="prow text-only reveal"><div class="rbody">
    <p class="rmeta">Reviewer</p>
    <h3 class="rtitle">Journals &amp; Conferences</h3>
    <p class="rauth">Engineering Structures &middot; Automation in Construction &middot; Structures &middot; Int. J. Solids and Structures &middot; ACM TOG &middot; Advances in Architectural Geometry (AAG)</p>
  </div></div>
  <div class="prow text-only reveal"><div class="rbody">
    <p class="rmeta">Affiliations</p>
    <h3 class="rtitle">Research communities</h3>
    <p class="rauth">Design++ Research Affiliate &middot; ETH AI Center Research Affiliate &middot; IASS Member</p>
  </div></div>
</section>

{% assign groups = "press,projects" | split: "," %}
{% assign labels = "In the press,Projects &amp; initiatives" | split: "," %}
{% for g in groups %}
  {% assign mitems = site.data.media[g] %}
  {% if mitems and mitems.size > 0 %}
  <div class="section-head reveal"><h2>{{ labels[forloop.index0] }}</h2><span class="bar"></span></div>
  <div class="marquee reveal" data-dir="right">
    <div class="marquee-track">
      {% for rep in (1..2) %}{% for m in mitems %}
      <a class="media-item" href="{{ m.url }}" target="_blank" rel="noopener"{% if rep == 2 %} aria-hidden="true" tabindex="-1"{% endif %} title="{{ m.title }}">
        <div class="media-logo{% unless m.logo %} noimg{% endunless %}">
          {% if m.logo %}<img src="{{ m.logo | relative_url }}" alt="{{ m.name }}">
          {% else %}<span class="media-name">{{ m.name }}</span>{% endif %}
        </div>
        <span class="media-cap">{{ m.title }}{% if m.year %} &middot; {{ m.year }}{% endif %}</span>
      </a>
      {% endfor %}{% endfor %}
    </div>
  </div>
  {% endif %}
{% endfor %}
