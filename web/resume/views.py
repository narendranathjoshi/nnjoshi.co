from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from resume.models import *
from resume.serializers import *


class HomeView(View):
    def get(self, request):
        info = {
            "email": BasicInfo.objects.get(key="email").value,
            "phone": BasicInfo.objects.get(key="phone").value,
            "head_bar": BasicInfo.objects.get(key="head_bar").value,
            "skills": Skill.objects.all(),
            "achievements": Achievement.objects.all(),
            "projects": Project.objects.all().order_by("-year"),
            "educations": Education.objects.all().order_by("-start_date"),
            "experiences": Experience.objects.all().order_by("-start_date"),
            "publications": Publication.objects.all().order_by("-year"),
        }

        return render(request, "index.html.jinja", {
            "email": info["email"],
            "phone": info["phone"],
            "skills": info["skills"],
            "head_bar": info["head_bar"],
            "achievements": info["achievements"],
            "projects": info["projects"],
            "educations": info["educations"],
            "experiences": info["experiences"],
            "publications": info["publications"],
        })


class InfoAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        info = {
            "email": BasicInfo.objects.get(key="email").value,
            "phone": BasicInfo.objects.get(key="phone").value,
            "head_bar": BasicInfo.objects.get(key="head_bar").value,
            "skills": SkillSerializer(Skill.objects.all(), many=True).data,
            "achievements": AchievementSerializer(Achievement.objects.all(), many=True).data,
            "projects": ProjectSerializer(Project.objects.all().order_by("-year"), many=True).data,
            "educations": EducationSerializer(Education.objects.all().order_by("-start_date"), many=True).data,
            "experiences": ExperienceSerializer(Experience.objects.all().order_by("-start_date"), many=True).data,
            "publications": PublicationSerializer(Publication.objects.all().order_by("-year"), many=True).data,
        }

        return Response(info, headers={
            "Access-Control-Allow-Origin": "*"
        })


class AppLandingView(View):
    def get(self, request, app):
        return render(request, "%s.html.jinja" % app, {})


class LoaderIOTestingView(View):
    def get(self, request):
        return HttpResponse("loaderio-8072c81ed2865e86699066698e9c40b7")
