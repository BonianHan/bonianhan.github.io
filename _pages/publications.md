---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <p class="publications-intro">A complete publication record is available on my <a href="{{ site.author.googlescholar }}">Google Scholar profile</a>.</p>
{% endif %}

{% include base_path %}

<div class="publications-list">
  {% for post in site.publications reversed %}
    {% include archive-single-publication.html %}
  {% endfor %}
</div>
