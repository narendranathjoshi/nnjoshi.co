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
                {% if blog_entry %}
                <div class="col-md-10">
                    {{ render_blog_entry(blog_entry)|safe }}
                </div>
            </div>
            <div class="row">
                <div class="col-md-10">
                    <div id="disqus_thread"></div>
                    <script>
                        var disqus_config = function () {
                            this.page.url = "http://nnjoshi.co/blog/post/{{ blog_entry.slug }}";
                            this.page.identifier = {{ blog_entry.id }};
                            this.page.title = "{{ blog_entry.title }}";
                        };
                        (function() {  // DON'T EDIT BELOW THIS LINE
                            var d = document, s = d.createElement('script');

                            s.src = '//nnjoshico.disqus.com/embed.js';

                            s.setAttribute('data-timestamp', +new Date());
                            (d.head || d.body).appendChild(s);
                        })();
                    </script>
                    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
                    {% else %}
                    <div class="col-md-10 text-center">
                        <h3>
                            Oops! You seemed to have landed in the nether regions of the universe!
                            <br><br>
                            Let's take you back to <a href="/blog/">the surface!</a>
                        </h3>
                    </div>
                    {% endif %}
                    <div class="col-md-2"></div>
                </div>
            </div>
        </div>
        <div class="col-md-2"></div>
    </div>
</div>

<script id="dsq-count-scr" src="//nnjoshico.disqus.com/count.js" async></script>
{% endblock %}