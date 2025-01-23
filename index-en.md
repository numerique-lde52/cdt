---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
lang: en
permalink: /en
---
{%- assign cats = site.data.categories.categories -%}

{%- for cat in cats -%}
{%- assign pages = site.pages | where:"categorie", cat.fr | where:"lang", page.lang | sort: "ordre" -%}
{%- assign pages-size = pages | size -%}

{% if pages-size > 0 %}
<h3>{{ cat[page.lang] }}</h3>
<ul>
{%- for p in pages -%}
<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>{%- endfor -%}
</ul>
{% endif %}
{%- endfor -%}