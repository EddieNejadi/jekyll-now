---
layout: default
title  : tags
---

{% for post in site.posts %}
{{ post.title }}:
{% for tag in post.tags %}
{{ tag }}
{% endfor %}
{% endfor %}