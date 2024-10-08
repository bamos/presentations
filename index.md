---
layout: singlePage
title: "Presentations"
---

These are the slides behind my major
presentations and posters.
They are all released with a
[CC-BY](http://creativecommons.org/licenses/by/4.0/)
license.
You can subscribe to these posts as an RSS feed [here](https://bamos.github.io/presentations/feed.xml).
The source code for this website is available in
[this repo](https://github.com/bamos/presentations).
It uses Jekyll to take the list of presentations and statically generate
this page along with individual linkable pages for them.
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
