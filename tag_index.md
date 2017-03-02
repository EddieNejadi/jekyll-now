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

{% for post in site.posts %}
{% for tag in post.tags %}
{% if tag in post.tags %}
{{ tag }}
{% endif %}
* {{ post.title }}: 
{% endfor %}
{% endfor %}
