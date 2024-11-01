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

<ol>
{% for post in site.posts %}
{% unless post.draft %}
<li>
<span class='cvdate'>{{ post.date | date: "%Y" }}</span>
<a href="{{ site.baseurl }}{{ post.url }}" target='_blank'>{{ post.title }}</a>
</li>
{% endunless %}
{% endfor %}
</ol>

<hr>

<!---
{% for post in site.posts %}
{% unless post.draft %}
<h1><a href="{{ site.baseurl }}/{{ post.url }}" target='_blank'>{{ post.title }}</a></h1>
<em>{{ post.date | date: "%Y" }}</em>
{%- if post.powerpoint -%}
&nbsp;| <a href="{{ site.baseurl }}/{{ post.powerpoint }}" target='_blank'>Powerpoint</a>
{%- endif -%}
{%- if post.keynote -%}
&nbsp;| <a href="{{ site.baseurl }}/{{ post.keynote }}" target='_blank'>Keynote</a>
{%- endif -%}
{%- if post.pdf -%}
&nbsp;| <a href="{{ site.baseurl }}/{{ post.pdf }}" target='_blank'>PDF</a>
{%- endif -%}
{%- if post.paper -%}
&nbsp;| <a href="{{ post.paper }}" target='_blank'>Paper</a>
{%- endif -%}
<br>
<md-block>
{{ post.abstract }}
</md-block>
<br>
<object data="{{ site.baseurl }}/{{ post.pdf }}" type='application/pdf' width="100%" height="1000px">
</object>
<hr>
{% endunless %}
{% endfor %}
-->
