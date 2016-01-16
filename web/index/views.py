import logging
from django.http import HttpResponse
from django.shortcuts import render

from django.template.loader import get_template
from django.views.generic import View
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from index.models import Tag
from index.serializers import BlogEntrySerializer

logger = logging.getLogger(__name__)


def get_local_log(msg):
    """
    use this like `logger.warning(get_local_log("test log"))`
    :param msg:
    :return:
    """
    return "(LOCAL DEV): %s" % msg


def render_blog_entry(data):
    data["tags"] = [Tag.objects.get(id=tag_id) for tag_id in data["tags"]]
    return get_template("entry_template.html.j").render(data)


def render_blog_peek(data):
    data["tags"] = [Tag.objects.get(id=tag_id) for tag_id in data["tags"]]
    data["peek"] = data["entry"][:600]
    return get_template("peek_template.html.j").render(data)


def render_nav_page(page_type):
    return get_template("nav.html.j").render({
        "page": page_type
    })


def handle_uploaded_file(f, file_save_path):
    with open(file_save_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# Views from here
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
        tags = Tag.objects.all()
        return render(request, "write.html.j", {
            "tags": tags,
            "render_blog_peek": render_blog_peek,
            "render_blog_entry": render_blog_entry,
        })


# API Views
class PreviewAPIView(ListAPIView):
    queryset = []
    serializer_class = BlogEntrySerializer

    def post(self, request, *args, **kwargs):
        return Response({
            "peek": render_blog_peek(request.data),
            "entry": render_blog_entry(request.data)
        })
