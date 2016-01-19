import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.template.loader import get_template
from django.utils.text import slugify
from django.views.generic import View
from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from index.models import Tag, BlogEntry
from index.serializers import BlogEntrySerializer

logger = logging.getLogger(__name__)


def get_local_log(msg):
    """
    use this like `logger.warning(get_local_log("test log"))`
    :param msg:
    :return:
    """
    return "(LOCAL DEV): %s" % msg


def auto_save(data):
    slug = slugify(data["title"])
    if slug and slug != '':
        blog_entry, created = BlogEntry.objects.get_or_create(slug=slug)
        blog_entry.title = data["title"]
        blog_entry.image = data["image"]
        blog_entry.image_caption = data["image_caption"]
        blog_entry.entry = data["entry"]
        blog_entry.peek = data["entry"][:600]
        tags = data["tags"] if "tags" in data.keys() else data["tags[]"]
        for tag_id in tags:
            blog_entry.tags.add(Tag.objects.get(id=tag_id))
        if data["new_tag"] != '':
            new_tag, _ = Tag.objects.get_or_create(
                slug=slugify(data["new_tag"]))
            new_tag.title = data["new_tag"]
            new_tag.save()
            blog_entry.tags.add(new_tag)
        blog_entry.save()

        return blog_entry
    else:
        return None


def render_blog_entry(blog_entry):
    return get_template("entry_template.html.j").render({
        "blog_entry": blog_entry,
        "to_date": to_date
    })


def render_blog_peek(blog_entry):
    return get_template("peek_template.html.j").render({
        "blog_entry": blog_entry,
        "to_date": to_date
    })


def render_nav_page(page_type):
    return get_template("nav.html.j").render({
        "page": page_type
    })


def handle_uploaded_file(f, file_save_path):
    with open(file_save_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def to_date(created_time):
    return created_time.strftime("%Y, %h %d")


def qdict_to_dict(qdict):
    """Convert a Django QueryDict to a Python dict.

    Single-value fields are put in directly, and for multi-value fields, a list
    of all values is stored at the field's key.

    """
    return {k: v[0] if len(v) == 1 else v for k, v in qdict.lists()}


# Views from here
class HomeView(View):
    def get(self, request):
        return render(request, "home.html.j", {
            "render_nav_page": render_nav_page
        })


class BlogView(View):
    def get(self, request):
        blog_entries = BlogEntry.objects.filter(is_published=True).order_by(
            "-created")
        tags = Tag.objects.all()

        return render(request, "blog.html.j", {
            "render_nav_page": render_nav_page,
            "render_blog_peek": render_blog_peek,
            "blog_entries": blog_entries,
            "all_tags": tags
        })


class BlogEntryView(View):
    def get(self, request, slug):
        try:
            blog_entry = BlogEntry.objects.get(slug=slug)
        except BlogEntry.DoesNotExist:
            return render(request, "entry.html.j", {
                "render_nav_page": render_nav_page
            })

        return render(request, "entry.html.j", {
            "render_nav_page": render_nav_page,
            "render_blog_entry": render_blog_entry,
            "blog_entry": blog_entry
        })


class TaggedView(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug=slug)
        blog_entries = BlogEntry.objects.filter(is_published=True,
                                                tags=tag).order_by("-created")

        return render(request, "blog.html.j", {
            "render_nav_page": render_nav_page,
            "render_blog_peek": render_blog_peek,
            "blog_entries": blog_entries,
            "tag": tag
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

    def post(self, request):
        data = qdict_to_dict(request.POST)
        blog_entry = auto_save(data)
        blog_entry.is_published = True
        blog_entry.save()

        return HttpResponseRedirect("/blog/post/%s" % blog_entry.slug)


class BlogEditView(View):
    def get(self, request, id):
        try:
            blog_entry = BlogEntry.objects.get(id=id)
        except BlogEntry.DoesNotExist:
            return HttpResponse("No blog post for the specified ID")
        tags = Tag.objects.all()
        selected_tags = [b.id for b in blog_entry.tags.all()]
        return render(request, "edit.html.j", {
            "tags": tags,
            "render_blog_peek": render_blog_peek,
            "render_blog_entry": render_blog_entry,
            "blog_entry": blog_entry,
            "selected_tags": selected_tags
        })

    def post(self, request):
        data = qdict_to_dict(request.POST)
        blog_entry = auto_save(data)
        blog_entry.is_published = True
        blog_entry.save()

        return HttpResponseRedirect("/blog/post/%s" % blog_entry.slug)


# API Views
class PreviewAPIView(ListAPIView):
    renderer_classes = (TemplateHTMLRenderer,)

    def post(self, request, *args, **kwargs):
        data = qdict_to_dict(request.data)
        blog_entry = auto_save(data)

        if data["content"] == 'peek':
            return HttpResponse(render_blog_peek(blog_entry))
        else:
            return Response({"blog_entry": blog_entry,
                             "to_date": to_date},
                            template_name="entry_template.html.j")


class AutoSaveAPIView(ListAPIView):
    queryset = []
    serializer_class = BlogEntrySerializer

    def post(self, request, *args, **kwargs):
        data = qdict_to_dict(request.data)
        auto_save(data)

        return Response({
            "success": True
        })
