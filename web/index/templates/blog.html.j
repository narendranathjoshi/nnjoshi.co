{% extends "base.html.j" %}

{% block title %}Blog - nnjoshi.co{% endblock %}

{% block content %}
<div class="container">
    {{ render_nav_page("blog")|safe }}

    <div class="row" style="margin-top:4%">
        <div class="col-md-2"></div>
        <div class="col-md-8">
            <div class="row">
                <div class="col-md-2">
                </div>
                <div class="col-md-10">
                {% for blog_entry in blog_entries %}
                    {{ render_blog_peek(blog_entry)|safe }}
                {% endfor %}
                </div>
            </div>
        </div>
        <div class="col-md-2"></div>
    </div>
</div>
{% endblock %}