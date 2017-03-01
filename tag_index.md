---
layout : default
title  : tags
---
<div class="tag-cloud">
  {% for tag in site.tags %}
    <a href="#posts-tag"
      id="{{ forloop.index }}" class="__tag" style="margin: 5px">{{tag[0]}}
    </a>
    <ul id="list_{{ forloop.index }}" style="display:none;">
      {% for post in tag[1] %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
  {% endfor %}
</div>
