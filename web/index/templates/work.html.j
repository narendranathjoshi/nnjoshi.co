{% extends "base.html.j" %}

{% block title %}Home - nnjoshi.co{% endblock %}

{% block content %}
<div class="container">
    {{ render_nav_page("work")|safe }}

    <div class="row" style="margin-top:4%">
        <div class="col-md-1"></div>
        <div class="col-md-9">
            <div class="row">
                <div class="col-md-8 text-justify">
                    <h2>Projects at College</h2>
                    <br>
                    <h3>Core Member, PESIT Entrepreneurship Cell</h3>
                    <h4>
                        Founding and core member of the publications
                        team of PESIT Entrepreneurship Cell and was
                        responsible for the management and reporting events.
                    </h4>

                    <h3>Driver Fatigue Detection System</h3>
                    <h4>Undergraduate final year project where the system used computer vision
                    and machine learning to keep track of the driver’s mouth to detect yawns and eyes to detect blinks.
                    </h4>

                    <h3>Agri Yield Consumption and Mill Data Analytics</h3>
                    <h4>A research project which spanned over fifteen months involving data
                    analysis and prediction. We analysed voluminous agricultural data and studied patterns of sowing and harvesting. Created a set of time series which would
                    help us estimate methods by which to suggest crops to farmers for the next sowing season so as to optimise profits.</h4>

                    <h3>Automatic Mobile Phones Customer Care Bot</h3>
                    <h4>Created a customer care bot for mobile phones using n-gram models and supervised MaxEnt classification using Markov models. The bot could accept and answer English queries ranging from the price of a particular model to feature
                    comparison between two devices.</h4>

                    <h3>Timetable Generator</h3>
                    <h4>Developed a Timetable Generator as a part of the Algorithms course in a team
                    of three. It is an application which generates valid and legitimate timetables for educational institutions depending upon their courses and workload.
                    It was developed in Java.</h4>

                    <h3>Infra – An Android based Remote Control for PC</h3>
                    <h4>Developed an android application as a part of the Mobile Systems and Engineering.
                    It is an application which facilitates the control of a PC or desktop through an Android app interfacing via the internet.</h4>

                    <h3>Engineering Results</h3>
                    <h4>Developed a web-based application as a part of the Software Engineering course
                    which provides a system for handling results of multiple institutions. It was developed in HTML/CSS/JavaScript and PHP/MySQL. I was the
                    coordinator and team leader in the project.</h4>

                    <h3>WTP for Typing Party</h3>
                    <h4>Developed a JavaScript-based typing game as a part of the Web
                    Technologies course in a team of two. It is a game which tests and improves the typing speed of a user with different modes of gameplay. It was developed in HTML/CSS/JavaScript and PHP/ MySQL.
                    </h4>
                </div>
                <div class="col-md-4">
                    <h2>Work</h2>
                    <br>
                    <h3>Product Engineer, Sensara <br><small>(August 2015 - present)</small></h3>
                    <h4>
                        A pivotal role in the creation of
                        <a href="http://adbreaks.in/">http://adbreaks.in/</a>,
                        an open, real-time semantic search engine of
                        television advertisements in Indian channels.
                    </h4>
                    <h3>Co-op Intern, Intuit <br><small>(January 2015 - July 2015)</small></h3>
                    <h4>
                        Worked as a part of the
                        <a href="http://www.mint.com/">mint.com</a>
                        platform team.
                    </h4>

                    <hr>

                    <h3>Get my CV <a href="{{ static('files/cv.pdf') }}">here</a></h3>
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