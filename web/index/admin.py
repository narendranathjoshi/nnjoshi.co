from django.contrib import admin

# Register your models here.
from index.models import BlogEntry, Tag


class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_published", "created"]
    search_fields = ["title", "tags"]
    list_filter = ["tags", "created", "is_published"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created"]
    search_fields = ["title"]
    list_filter = ["created"]

admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(Tag, TagAdmin)
