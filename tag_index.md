---
layout: default
title  : tags
---

<h2 class="post_title">{{page.title}}</h2>

{% for post in site.posts %}
{% for tag in post.tags %}
{% if tag == page.tag %}
<a class="archive_list_article_link" href='{{post.url}}'>{{post.title}}</a>
<p class="summary">{{post.summary}}</p>
{% endif %}
{% endfor %}
{% endfor %}

