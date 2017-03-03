---
layout: default
title  : tags
---
  {% capture tag_list %}		
  {% for post in site.posts %}		
  {% for tag in post.tags %}		
  {{tag}}		
  {% endfor %}		
  {% endfor %}		
  {% endcapture %}
  
  {% for utag in uniq_tags %}
  {{utag}}
  {% for post in site.posts %}
  {% for tag in post.tags %}
  {% if tag == utag %}
    <ul class="archive_list">
      <a class="archive_list_article_link" href='{{post.url}}'>{{post.title}}</a> <time style="color:#666;font-size:11px;" datetime='{{post.date | date: "%Y-%m-%d"}}'>{{post.date | date: "%m/%d/%y"}}</time>
    </ul>
  {% endif %}
  {% endfor %}
  {% endfor %}
  {% endfor %}


