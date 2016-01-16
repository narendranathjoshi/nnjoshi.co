<div class="row">
    <div class="col-md-8">
        <h2>{{ title }}</h2>
    </div>
    <div class="col-md-4 text-right">
        <h4>
            <small>Tags</small>
            {% for tag in tags %}
            <a class="btn btn-default" href="/blog/tagged/{{ tag.slug }}">{{ tag.title }}</a>
            {% endfor %}
        </h4>
    </div>
</div>
<br>
<div class="row">
    <div class="col-sm-12 text-justify">
        <div style="float:left;width:50%;" class="text-center">
            <img src="{{ image }}" style="width:90%;float:left; margin:3%"/>
            <br>
            <h5>{{ image_caption }}</h5>
        </div>
        <p>
            {{ peek }}
        </p>
    </div>
</div>

<hr>