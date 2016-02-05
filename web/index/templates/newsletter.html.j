{% extends "base.html.j" %}

{% block title %}Newsletter - nnjoshi.co{% endblock %}

{% block content %}
<div class="container">
    <div class="row" style="margin-top:4%">
        <div class="col-md-2"></div>
        <div class="col-md-8">
            <div class="row">
                {{ render_blog_peek(blog_entry, True)|safe }}
            </div>
        </div>
        <div class="col-md-2"></div>
    </div>
</div>

{% endblock %}