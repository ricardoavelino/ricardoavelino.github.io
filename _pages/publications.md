---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on my <u><a href="https://scholar.google.com/citations?user=x1FhoYcAAAAJ&hl=fr">Google Scholar</a></u>, or <u><a href="https://www.researchgate.net/profile/Ricardo_Avelino2">ResearchGate</a></u>  profiles.

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
