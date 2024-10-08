---
layout: singlePage
title: "Presentations"
---

These are the slides behind [my](http://bamos.github.io) major
presentations and posters.
They are all released with a
[CC-BY](http://creativecommons.org/licenses/by/4.0/)
license.
[Here](https://github.com/bamos/presentations)
is the source code that generates this page.
<hr>

{% for post in site.posts %}
{% unless post.draft %}
<h1><a href="{{ site.baseurl }}/{{ post.url }}">{{ post.title }}</a></h1>
<em>{{ post.date | date: "%Y" }}</em>
{%- if post.powerpoint -%}
&nbsp;| <a href="{{ site.baseurl }}/{{ post.powerpoint }}">Powerpoint</a>
{%- endif -%}
{%- if post.keynote -%}
&nbsp;| <a href="{{ site.baseurl }}/{{ post.keynote }}">Keynote</a>
{%- endif -%}
{%- if post.pdf -%}
&nbsp;| <a href="{{ site.baseurl }}/{{ post.pdf }}">PDF</a>
{%- endif -%}
{%- if post.paper -%}
&nbsp;| <a href="{{ post.paper }}">Paper</a>
{%- endif -%}
<br>
<md-block>
{{ post.abstract }}
</md-block>
<embed src="{{ site.baseurl }}/{{ post.pdf }}" width="100%" height="1000px">
<hr>
{% endunless %}
{% endfor %}
