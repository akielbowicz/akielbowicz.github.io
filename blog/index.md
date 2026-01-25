---
layout: default
title: Blog
---

# Blog

Aquí puedes encontrar mis artículos, en español e inglés.

## Artículos en Español

<ul>
  {% for post in site.posts %}
    {% if post.lang == 'es' %}
      <li>
        <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%B %d, %Y" }}
      </li>
    {% endif %}
  {% endfor %}
</ul>

## Posts in English

<ul>
  {% for post in site.posts %}
    {% if post.lang == 'en' %}
      <li>
        <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%B %d, %Y" }}
      </li>
    {% endif %}
  {% endfor %}
</ul>
