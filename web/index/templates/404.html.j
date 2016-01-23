{% extends "base.html.j" %}

{% block title %}
    Not found - nnjoshi.co
{% endblock %}

{% block content %}
<div class="container">
    {{ render_nav_page("blog")|safe }}

    <div class="row" style="margin-top:4%">
        <div class="col-md-2"></div>
        <div class="col-md-8">
            <div class="row">
                <div class="col-md-10 text-center">
                    <h3>
                        Oops! You seemed to have landed in the nether regions of the universe!
                        <br><br>
                        Let's take you back to <a href="/blog/">the surface!</a>
                    </h3>
                </div>
                <div class="col-md-2"></div>
            </div>
        </div>
        <div class="col-md-2"></div>
    </div>
</div>

{% endblock %}