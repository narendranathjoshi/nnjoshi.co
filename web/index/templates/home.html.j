{% extends "base.html.j" %}

{% block title %}Home - nnjoshi.co{% endblock %}

{% block content %}
<div class="container">
    {{ render_nav_page("home")|safe }}

    <div class="row" style="margin-top:4%">
        <div class="col-md-1"></div>
        <div class="col-md-9">
            <div class="row">
                <h4 class="text-center">
                    Hi! I'm Narendra Nath Joshi.
                </h4>
                <div class="col-md-6 text-right row-eq-height">
                    <h2>Technology Enthusiast.</h2>
                    <h4>I love tech and gadgets!<br>Oh look, there's a new device unveiled, cya!</h4>
                </div>
                <div class="col-md-6 text-left">
                    <img class="home-display-img" src="{{ static('img/tech.png') }}">
                </div>
            </div>
            <br>
            <br>
            <div class="row">
                <div class="col-md-6 text-right">
                    <img class="home-display-img" src="{{ static('img/read.png') }}">
                </div>
                <div class="col-md-6 text-left row-eq-height">
                    <h2>Avid Reader. Potterhead.</h2>
                    <h4>
                        Yes, I'm a Potterhead too! I'm a Gryffindor on
                        <a href="https://www.pottermore.com/">Pottermore.</a>
                        Just waiting for the sword now!
                        <br>
                        A good book is my way of relaxation and abandon.
                    </h4>
                </div>
            </div>
            <br>
            <br>
            <div class="row">
                <div class="col-md-6 text-right row-eq-height">
                    <h2>Regular Writer.</h2>
                    <h4>
                        I write. A lot. Sometimes.
                        <br>
                        Check out my <a href="/blog/">blog</a>
                    </h4>
                </div>
                <div class="col-md-6 text-left">
                    <img class="home-display-img" src="{{ static('img/writer.png') }}">
                </div>
            </div>
            <br>
            <br>
            <div class="row">
                <div class="col-md-6 text-right">
                    <img class="home-display-img" src="{{ static('img/prog_lang.png') }}">
                </div>
                <div class="col-md-6 text-left row-eq-height">
                    <h2>Pythonista. Can Java too.</h2>
                    <h4>
                        Works mainly in Python, HTML/CSS/JavaScript, Java/Android.
                        <br>
                        Check out some work <a href="/work/">here</a>
                    </h4>
                </div>
            </div>
            <br>
            <br>
            <div class="row">
                <div class="col-md-6 text-right row-eq-height">
                    <h2>Product Engineer at <a>Sensara</a>.</h2>
                    <h4>
                        A deep TV search and content startup based in Bangalore, India
                        <br>
                        Check out my work <a href="/work/">here</a>
                    </h4>
                </div>
                <div class="col-md-6 text-left">
                    <img class="home-display-img" src="{{ static('img/sensara.png') }}">
                </div>
            </div>
            <br>
            <br>
            <div class="row">
                <div class="col-md-6 text-right">
                    <img class="home-display-img" src="{{ static('img/data.png') }}">
                </div>
                <div class="col-md-6 text-left row-eq-height">
                    <h2>Interested in Data.</h2>
                    <h4>Fascinated about data mining, search and information retrieval, machine learning and natural processing</h4>
                </div>
            </div>
            <br>
            <br>
            <div class="row">
                <div class="col-md-6 text-right row-eq-height">
                    <h2>Gamer.</h2>
                    <h4>
                        I like to play stuff.
                        <br>
                        (Psst. Don't tell anyone, I prefer a console)
                    </h4>
                </div>
                <div class="col-md-6 text-left">
                    <img class="home-display-img" src="{{ static('img/gamer.png') }}">
                </div>
            </div>
            <br>
            <br>
            <div class="row">
                <div class="col-md-6 text-center">
                    <div class="col-md-5">
                        <a target="_blank" href="https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=narendranathjoshi@gmail.com&body=Hi!">
                            <img src="{{ static('img/gmail.png') }}" />
                        </a>
                        <br>
                        <br>
                        <a href="https://twitter.com/share" class="twitter-share-button"{count} data-url="http://nnjoshi.co" data-via="narendranjoshi" data-size="large">Tweet</a>
                        <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
                        <br>
                        <br>
                    </div>
                    <div class="col-md-7">
                        <!-- Place this tag where you want the button to render. -->
                        <a class="github-button" href="https://github.com/narendranathjoshi" data-style="mega" data-count-href="/narendranathjoshi/followers" data-count-api="/users/narendranathjoshi#followers" data-count-aria-label="# followers on GitHub" aria-label="Follow @narendranathjoshi on GitHub">Follow @narendranathjoshi</a>
                        <br>
                        <br>
                        <script src="//platform.linkedin.com/in.js" type="text/javascript"></script>
                        <script type="IN/MemberProfile" data-id="https://www.linkedin.com/in/narendranathjoshi" data-format="hover" data-related="false" data-text="Narendra Nath Joshi"></script>
                        <br>
                        <br>
                    </div>
                </div>
                <div class="col-md-6 text-left">
                    <h2>
                        Reach me here
                    </h2>
                </div>
            </div>
        </div>
        <div class="col-md-1"></div>
    </div>

    <hr>
</div>

<!-- Place this tag right after the last button or just before your close body tag. -->
<script async defer id="github-bjs" src="https://buttons.github.io/buttons.js"></script>
{% endblock %}