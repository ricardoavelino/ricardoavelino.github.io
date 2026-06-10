---
layout: clean
nav: projects
permalink: /projects/
title: "Projects"
---

<h1 class="page-title">Projects</h1>
<p class="lead">Built work and physical prototypes — from professional practice to research pavilions.</p>

{% assign groups = "professional,prototypes" | split: "," %}
{% assign labels = "Professional Practice,Prototypes &amp; Pavilions" | split: "," %}
{% for g in groups %}
  {% assign items = site.data.projects[g] %}
  {% if items and items.size > 0 %}
  <div class="section-head reveal"><h2>{{ labels[forloop.index0] }}</h2><span class="bar"></span></div>
  <section class="grid projects">
    {% for it in items %}
    <article class="card reveal">
      <div class="thumb">{% if it.url %}<a href="{{ it.url }}" target="_blank" rel="noopener">{% endif %}<img src="{{ it.image | relative_url }}" alt="{{ it.title }}">{% if it.url %}</a>{% endif %}</div>
      <div class="body">
        <p class="venue">{{ it.org }}{% if it.year %} &middot; {{ it.year }}{% endif %}</p>
        <h3 class="title">{% if it.url %}<a href="{{ it.url }}" target="_blank" rel="noopener">{{ it.title }}</a>{% else %}{{ it.title }}{% endif %}</h3>
        {% if it.location %}<p class="ploc">{{ it.location }}</p>{% endif %}
        {% if it.description %}<p class="pdesc">{{ it.description }}</p>{% endif %}
      </div>
    </article>
    {% endfor %}
  </section>
  {% endif %}
{% endfor %}
