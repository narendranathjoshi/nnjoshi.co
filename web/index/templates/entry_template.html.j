<div class="row">
    <div class="col-md-8">
        <h2>{{ blog_entry.title }}</h2>
        <h5>{{ to_date(blog_entry.created) }}</h5>
    </div>
    <div class="col-md-4 text-right">
        <h4>
            <small>Tags</small>
            {% for tag in blog_entry.tags.all() %}
            <a class="btn btn-default" href="/blog/tagged/{{ tag.slug }}">{{ tag.title }}</a>
            {% endfor %}
        </h4>
    </div>
</div>
<br>
<div class="row">
    <div class="col-sm-12 text-justify">
        <div style="float:left;width:50%;" class="text-center">
            <img src="{{ blog_entry.image }}" style="width:90%;float:left; margin:3%"/>
            <br>
            <h5>{{ blog_entry.image_caption }}</h5>
        </div>
        <p>
            {{ blog_entry.entry }}
        </p>
    </div>
</div>

<hr>