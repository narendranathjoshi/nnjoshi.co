from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from resume.models import *
from web.rediscache import resume_cache


class HomeView(View):
    def get(self, request):
        info_cache_key = "info_v2"
        info = resume_cache.pickled_get(info_cache_key)

        if not info:
            info = {
                "email": BasicInfo.objects.get(key="email"),
                "phone": BasicInfo.objects.get(key="phone"),
                "head_bar": BasicInfo.objects.get(key="head_bar"),
                "skills": Skill.objects.all(),
                "achievements": Achievement.objects.all(),
                "projects": Project.objects.all().order_by("-year"),
                "educations": Education.objects.all().order_by("-start_date"),
                "experiences": Experience.objects.all().order_by("-start_date")
            }

            resume_cache.pickled_set(info_cache_key, info, 24 * 60 * 60 * 1000)

        return render(request, "index.html.jinja", {
            "email": info["email"],
            "phone": info["phone"],
            "skills": info["skills"],
            "head_bar": info["head_bar"],
            "achievements": info["achievements"],
            "projects": info["projects"],
            "educations": info["educations"],
            "experiences": info["experiences"],
        })


class AppLandingView(View):
    def get(self, request, app):
        return render(request, "%s.html.jinja" % app, {})


class LoaderIOTestingView(View):
    def get(self, request):
        return HttpResponse("loaderio-8072c81ed2865e86699066698e9c40b7")