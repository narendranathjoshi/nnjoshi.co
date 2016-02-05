<div class="row">
    <div class="col-md-8">
        <h2>{{ blog_entry.title }}</h2>
        <h5>{{ to_date(blog_entry.created) }}</h5>
    </div>
    <div class="col-md-4 text-right">
        <h4>
            <small>Tags</small>
            {% for tag in blog_entry.tags.all() %}
            <a class="tag-btn btn btn-success" href="/blog/tagged/{{ tag.slug }}">{{ tag.title }}</a>
            {% endfor %}
        </h4>
    </div>
</div>
<br>
<div class="row">
    <div class="col-sm-12 text-justify">
        <div style="float:left;width:50%;" class="text-center">
            <img src="{{ blog_entry.image }}" style="width:90%;float:left; margin:3%; border-radius: 20px;"/>
            <br>
            <h5>{{ blog_entry.image_caption }}</h5>
        </div>
        <p class="post">
            {{ blog_entry.entry|safe }}
        </p>
    </div>
</div>
<div class="row">
    <div class="col-sm-12 text-right">
        <a href="https://twitter.com/share" class="twitter-share-button"{count} data-via="narendranjoshi">Tweet</a>
        <br>
        <div class="fb-share-button" data-href="/blog/post/{{ blog_entry.slug }}" data-layout="button_count"></div>
    </div>
</div>

<hr>