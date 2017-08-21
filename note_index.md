---
layout: default
title  : notes
---

<ul>

  {% capture tag_list %}
  {% for note in site.notes %}
  {% for tag in note.tags %}
  {{tag}}
  {% endfor %}
  {% endfor %}
  {% endcapture %}

  {% assign uniq_tags = tag_list | split: " " | uniq %}

  {% for utag in uniq_tags %}
  <li class="tag_list" href='#{{utag}}'>
  {{utag}}
  {% for note in site.notes %}
  {% for tag in note.tags %}
  {% if tag == utag %}
    <ul class="archive_list">
      <a class="archive_list_article_link" href='{{note.url}}'>{{note.title}}</a> <time style="color:#666;font-size:11px;" datetime='{{note.date | date: "%Y-%m-%d"}}'>{{note.date | date: "%m/%d/%y"}}</time>
    </ul>
  {% endif %}
  {% endfor %}
  {% endfor %}
  </li>
  {% endfor %}
</ul>
