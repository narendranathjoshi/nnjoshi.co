from django.contrib import admin


# Register your models here.
from inquest.models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "os", "sdk", "device", "build",
                    "is_active", "last_ping")
    list_filter = ("os", "sdk", "device", "build", "is_active")


admin.site.register(UserInfo, UserInfoAdmin)
