{% extends "base.html.j" %}

{% block title %}
    {% if blog_entry %}
        {{blog_entry.title}} - nnjoshi.co
    {% else %}
        Not found - nnjoshi.co
    {% endif %}
{% endblock %}

{% block content %}
<div class="container">
    {{ render_nav_page("blog")|safe }}

    <div class="row" style="margin-top:4%">
        <div class="col-md-2"></div>
        <div class="col-md-8">
            <div class="row">
                <div class="col-md-2">
                </div>
                {% if blog_entry %}
                <div class="col-md-10">
                    {{ render_blog_entry(blog_entry)|safe }}
                </div>
                {% else %}
                <div class="col-md-10 text-center">
                    <h3>
                        Oops! You seemed to have landed in the nether regions of the universe!
                        <br><br>
                        Let's take you back to <a href="/blog/">the surface!</a>
                    </h3>
                </div>
                {% endif %}
            </div>
        </div>
        <div class="col-md-2"></div>
    </div>
</div>
{% endblock %}