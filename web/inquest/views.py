from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from resume.models import *
from web.rediscache import resume_cache


class HomeView(View):
    def get(self, request):
        return render(request, "inquest.html.jinja", {})
