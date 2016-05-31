from django.contrib import admin
from blog.models import *


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "is_published")
    list_filter = ("created", "is_published")
    actions = (publish_post, )


admin.site.register(Post, PostAdmin)


def publish_post(modeladmin, request, queryset):
    queryset.update(is_published=True)

publish_post.short_description = "Publish post to blog"
