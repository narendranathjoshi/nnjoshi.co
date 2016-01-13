import logging
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.views.generic import View
from index.models import Tag

logger = logging.getLogger(__name__)


def get_local_log(msg):
    """
    use this like `logger.warning(get_local_log("test log"))`
    :param msg:
    :return:
    """
    return "(LOCAL DEV): %s" % msg


def render_blog_entry():
    return get_template("entry_template.html.j").render()


def render_blog_peek():
    return get_template("peek_template.html.j").render()


def render_nav_page(page_type):
    return get_template("nav.html.j").render({
        "page": page_type
    })


class HomeView(View):
    def get(self, request):
        return render(request, "home.html.j", {
            "render_nav_page": render_nav_page
        })


class BlogView(View):
    def get(self, request):
        return render(request, "blog.html.j", {
            "render_nav_page": render_nav_page
        })


class WorkView(View):
    def get(self, request):
        return render(request, "work.html.j", {
            "render_nav_page": render_nav_page
        })


class BlogWriteView(View):
    def get(self, request):
        return render(request, "write.html.j")
