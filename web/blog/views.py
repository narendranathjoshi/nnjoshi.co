from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        return render(request, "home.html.jinja", {})


class PostView(View):
    def get(self, request):
        return render(request, "post.html.jinja", {})
