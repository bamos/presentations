---
layout: singlePage
title: "Presentations"
---

These are the slides behind my major
presentations and posters.
They are all released with a
[CC-BY](http://creativecommons.org/licenses/by/4.0/)
license.
The source code for this website
<span style='color: gray;'>(built with Jekyll)</span>
is available in
[this repo](https://github.com/bamos/presentations).
<div style="margin: 1.5rem 0; height: 2px; border-radius: 999px; background-color: rgba(90, 90, 90, 0.8);"></div>

{% assign presentations = site.presentations | sort: "date" | reverse %}
<ol>
{% for presentation in presentations %}
{% unless presentation.draft %}
<li>
<span class='cvdate'>{{ presentation.date | date: "%Y" }}</span>
<a href="{{ site.baseurl }}{{ presentation.url }}" target='_blank'>{{ presentation.title }}</a>
</li>
{% endunless %}
{% endfor %}
</ol>

<div style="margin: 1.5rem 0; height: 2px; border-radius: 999px; background-color: rgba(90, 90, 90, 0.8);"></div>