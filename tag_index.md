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


~~~bash
echo test
~~~

<ul>
  {% for tagpage in site.page.tag %}
  <li class="tag_list"> {{tagpage}}
    {% for post in site.post %}
    {% for tag in post.tags %}
    {% if tag == tagpage %}
    <ul class="archive_list">
      <a class="archive_list_article_link" href='{{post.url}}'>{{post.title}}</a> <time style="color:#666;font-size:11px;" datetime='{{post.date | date: "%Y-%m-%d"}}'>{{post.date | date: "%m/%d/%y"}}</time>
    </ul>
    {% endif %}
    {% endfor %}
    {% endfor %}
  </li>
  {% endfor %}
</ul>
~~~bash
echo test
~~~

<ul>
{% assign my_array = "ants, bugs, bees, bugs, ants" | split: ", " %}

{{ my_array | uniq | join: ", " }}

  {% capture tag_list %}
  {% for post in site.posts %}
  {% for tag in post.tags %}
  {{tag}},
  {% endfor %}
  {% endfor %}
  {% endcapture %}
  <p>endcaptur: {{ tag_list }}</p>

  <p>t_list: {{ t_list }}</p>
  {% for tag_item in tag_list %}
  {% for post in site.posts %}
  <li class="tag_list"> {{tag_item}}
    <ul class="archive_list">
      <a class="archive_list_article_link" href='{{post.url}}'>{{post.title}}</a> <time style="color:#666;font-size:11px;" datetime='{{post.date | date: "%Y-%m-%d"}}'>{{post.date | date: "%m/%d/%y"}}</time>
    </ul>
  </li>
  {% endfor %}
  {% endfor %}
</ul>

