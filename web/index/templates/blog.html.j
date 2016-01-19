{% extends "base.html.j" %}

{% block title %}Blog - nnjoshi.co{% endblock %}

{% block content %}
<div class="container">
    {{ render_nav_page("blog")|safe }}

    <div class="row" style="margin-top:4%">
        <div class="col-md-2"></div>
        <div class="col-md-8">
            {% if not tag %}
            <div class="row">
                {% for all_tag in all_tags %}
                    <a href="/blog/tagged/{{ all_tag.slug }}" class="btn btn-default">{{ all_tag.title }}</a>
                {% endfor %}
            </div>
            <hr>
            {% endif %}
            <div class="row">
                {% for blog_entry in blog_entries %}
                    {{ render_blog_peek(blog_entry)|safe }}
                {% endfor %}
            </div>
        </div>
        <div class="col-md-2"></div>
    </div>
</div>
{% endblock %}