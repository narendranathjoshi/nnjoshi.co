from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from resume.models import *


class DummyHomeView(View):
    def get(self, request):
        email = BasicInfo.objects.get(key="email")
        phone = BasicInfo.objects.get(key="phone")
        skills = Skill.objects.all()
        achievements = Achievement.objects.all()
        projects = Project.objects.all().order_by("-year")
        educations = Education.objects.all().order_by("-start_date")
        experiences = Experience.objects.all().order_by("-start_date")

        return render(request, "index.html.jinja", {
            "email": email,
            "phone": phone,
            "skills": skills,
            "achievements": achievements,
            "projects": projects,
            "educations": educations,
            "experiences": experiences,
        })
