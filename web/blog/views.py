from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from blog.models import Post


# helper functions
def get_published_posts():
    if settings.DEBUG:
        return Post.objects.all()

    return Post.objects.filter(is_published=True)


def get_recent_posts(number):
    return get_published_posts().order_by('-created')[:number]


# Create your views here.
class HomeView(View):
    def get(self, request):

        return render(request, "home.html.jinja", {
            "recent_posts": get_recent_posts(4),
            "posts": get_published_posts(),
        })


class PostView(View):
    def get(self, request, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return render(request, "404.html.jinja", {
                "recent_posts": get_recent_posts(4),
            })

        return render(request, "post.html.jinja", {
            "recent_posts": get_recent_posts(4),
            "post": post
        })


class SearchView(View):
    def get(self, request):
        q = request.GET.get("q", None)

        if not q:
            return HttpResponseRedirect("/blog")

        results = get_published_posts().filter(title__icontains=q)

        return render(request, "home.html.jinja", {
            "recent_posts": get_recent_posts(4),
            "posts": results
        })
