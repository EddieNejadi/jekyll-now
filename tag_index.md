---
layout: default
title  : tags
---

{% for post in site.posts %}
#### {{ post.title }}: 
{% for tag in post.tags %}
* {{ tag }}
{% endfor %}
{% endfor %}

~~~bash
echo test
~~~

<ul>
  {% for post in site.posts %}
  {% for tag in post.tags %}
  <li class="tag_list"> {{tag}}
    <ul class="archive_list">
      <a class="archive_list_article_link" href='{{post.url}}'>{{post.title}}</a> <time style="color:#666;font-size:11px;" datetime='{{post.date | date: "%Y-%m-%d"}}'>{{post.date | date: "%m/%d/%y"}}</time>
    </ul>
  </li>
  {% endfor %}
  {% endfor %}
</ul>