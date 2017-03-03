---
layout: default
title  : tags
---
<ul>
{% for post in site.posts %} {% for tag in post.tags %}
<li class="tag_list">
{{tag}}
<ul class="archive_list">
          <a class="archive_list_article_link" href='{{post.url}}'>{{post.title}}</a> <time style="color:#666;font-size:11px;" datetime='{{post.date | date: "%Y-%m-%d"}}'>{{post.date | date: "%m/%d/%y"}}</time>
          </ul>
        </li>

{% endfor %} {% endfor %}
</ul>
``` {.bash}
echo test
```

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

``` {.bash}
echo test
```

<ul>
{% assign my_array = "ants, bugs, bees, bugs, ants" | split: ", " %}

{{ my_array | uniq | join: ", " }}

  {% capture tag_list %}
  {% for post in site.posts %}
  {% for tag in post.tags %}
  {{tag}}
  {% endfor %}
  {% endfor %}
  {% endcapture %}
  {% assign uniq_tags = tag_list | split: " " | uniq %}</p>
  <p>split: {{ tag_list | size }}</p>
  <p>split join: {{ tag_list | split: " " | uniq | join: ", " }}</p>
  <p>endcaptur: {{ tag_list | split: ", " | uniq | join: ", " }}</p>

  {% for utag in uniq_tags %}
  {% for post in site.posts %}
  {% for tag in post.tags %}
  {% if tag == utag %}
  <li class="tag_list"> {{utag}}
    <ul class="archive_list">
      <a class="archive_list_article_link" href='{{post.url}}'>{{post.title}}</a> <time style="color:#666;font-size:11px;" datetime='{{post.date | date: "%Y-%m-%d"}}'>{{post.date | date: "%m/%d/%y"}}</time>
    </ul>
  </li>
  {% endif %}
  {% endfor %}
  {% endfor %}
  {% endfor %}
</ul>




