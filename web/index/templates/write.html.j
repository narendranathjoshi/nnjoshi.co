{% extends "base.html.j" %}

{% block title %}Create Post - nnjoshi.co{% endblock %}

{% block content %}
<div class="container">
    <div class="row" style="margin-top:4%">
        <div class="col-md-2"></div>
        <div class="col-md-8">
            <div class="row">
                <h3>Create a Blog Entry</h3>
                <form method="post">
                    {% csrf_token %}
                    <input type="text" id="title" name="title" class="form-control" placeholder="Enter post here"/>
                    <hr>
                    <textarea style="width:100%" rows="20" name="entry" id="entry" placeholder="Enter post content here"></textarea>
                    <hr>
                    <input type="url" class="form-control" placeholder="Enter image URL here">
                    <p class="text-center">OR</p>
                    <input type="file" />
                    <hr>
                    <input type="button" value="Preview" class="btn btn-primary pull-right" onclick="preview()"/>
                    <input type="submit" value="Submit" class="btn btn-success"/>
                </form>
            </div>
            <div class="row" id="preview-pane">

            </div>
        </div>
        <div class="col-md-2"></div>
    </div>
</div>

<script>
    function preview() {
        $.post("/api/v1/preview/", {content:$("#entry"), title:$("#title")}, function(data) {
            $("#preview-pane").html(data)
        })
    }
</script>
{% endblock %}