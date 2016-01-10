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
                    <h3>Hold tight! Coming soon!</h3>
                </div>
            </div>
        </div>
        <div class="col-md-2"></div>
    </div>
</div>
{% endblock %}