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
                    <div class="panel panel-primary">
                        <div class="panel-heading">
                            <h3 class="panel-title">Like What You Read? So, Read What You Like!</h3>
                        </div>
                        <div class="panel-body">
                            <h4>Drop in your email ID and get all updates right in your inbox!</h4>
                            <h5>I solemnly swear that I won't spam you. Ever.</h5>
                            <div class="input-group">
                                <input id="subsc_email" type="email" class="form-control" placeholder="Email ID" required>
                                <span class="input-group-btn">
                                    <button class="btn btn-success" onclick="subscribe()" type="button">Go!</button>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-10">
                    <div class="fb-comments" data-href="http://nnjoshi.co/blog/post/{{ blog_entry.slug }}" data-numposts="10"></div>
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

<script>
    function validateEmail(email){
        var emailReg = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
        var valid = emailReg.test(email);

        if(!valid) {
            return false;
        } else {
            return true;
        }
    }

    function subscribe() {
        var subsc_email = $('#subsc_email').val();
        if (subsc_email == '') showAlert('noemail');
        else if (!validateEmail(subsc_email)) showAlert('invalidemail');
        else {
            $.get("/api/v1/newsletters/subscribe?email=" + subsc_email, function(data) {
                showAlert(data['msg']);
            })
        }

    }

    function showAlert(type) {
        if (type == 'noemail') {
            var noemail_alert = $("<div class='alert alert-danger text-center' role='alert' style='position:fixed; top: 100px; width: 400px; right: 200px;'>Nice Troll! But I need an email ID</div>").appendTo('body');
            setTimeout(function () {
                noemail_alert.fadeOut(500);
            }, 2000);
        } else if (type == 'invalidemail') {
            var noemail_alert = $("<div class='alert alert-danger text-center' role='alert' style='position:fixed; top: 100px; width: 400px; right: 200px;'>Oops! Not a valid email ID</div>").appendTo('body');
            setTimeout(function () {
                noemail_alert.fadeOut(500);
            }, 2000);
        } else if (type == 'success') {
            var noemail_alert = $("<div class='alert alert-success text-center' role='alert' style='position:fixed; top: 100px; width: 400px; right: 200px;'>Nice! You're awesome. Wait for the goodies in your inbox!</div>").appendTo('body');
            setTimeout(function () {
                noemail_alert.fadeOut(500);
            }, 2000);
        } else if (type == 'dupe') {
            var noemail_alert = $("<div class='alert alert-info text-center' role='alert' style='position:fixed; top: 100px; width: 400px; right: 200px;'>Wow! You're already registered for the good stuff!</div>").appendTo('body');
            setTimeout(function () {
                noemail_alert.fadeOut(500);
            }, 2000);
        }
    }
</script>

{% endblock %}