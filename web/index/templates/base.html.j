<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}nnjoshi.co{% endblock %}</title>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0-alpha1/jquery.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css">

        <!--local CSS-->
        <link rel="stylesheet" href="/static/css/local.css">
    </head>
    <body>
    {% block content %}{% endblock %}
    </body>
</html>