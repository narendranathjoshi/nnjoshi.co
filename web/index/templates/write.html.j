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
                    <div class="row">
                        <div class="col-sm-6">
                            <input type="text" id="title" name="title" class="form-control" placeholder="Enter post title here"/>
                            <br>
                            <input type="text" class="form-control" name="new_tag" id="new_tag" placeholder="Add a new tag here.."/>
                        </div>
                        <div class="col-sm-6">
                            <select id="tags" name="tags" class="form-control" multiple>
                                {% for tag in tags %}
                                    <option value="{{ tag.id }}">{{ tag.title }}</option>
                                {% endfor %}
                            </select>
                        </div>
                    </div>
                    <br>
                    <textarea style="width:100%" rows="20" name="entry" id="entry" placeholder="Enter post content here"></textarea>
                    <br>
                    <div class="row">
                        <div class="col-sm-6">
                            <input type="url" class="form-control" name="image_url" id="image_url" placeholder="Enter image URL here">
                        </div>
                        <div class="col-sm-6">
                            <input type="text" class="form-control" name="image_caption" id="image_caption" placeholder="Enter image caption here">
                        </div>
                    </div>
                    <br>
                    <input type="button" value="Preview" class="btn btn-primary pull-right" onclick="preview()"/>
                    <input type="submit" value="Submit" class="btn btn-success"/>
                </form>
            </div>
            <hr>
            <div class="row" id="peek-preview-pane">
                {{ render_blog_peek()|safe }}
            </div>
            <div class="row" id="entry-preview-pane">
                {{ render_blog_entry()|safe }}
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