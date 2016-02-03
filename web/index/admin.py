from django.contrib import admin

# Register your models here.
from index.models import BlogEntry, Tag, Subscriber


def publish(modeladmin, request, queryset):
    queryset.update(status='p')
publish.short_description = "Publish selected blog posts"


class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_published", "created"]
    search_fields = ["title", "tags"]
    list_filter = ["tags", "created", "is_published"]
    actions = [publish]


class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created"]
    search_fields = ["title"]
    list_filter = ["created"]


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "created"]
    search_fields = ["email"]
    list_filter = ["created"]

admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
