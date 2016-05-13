from django.contrib import admin
from blog.models import *


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "is_published")
    list_filter = ("created", "is_published")


admin.site.register(Post, PostAdmin)
