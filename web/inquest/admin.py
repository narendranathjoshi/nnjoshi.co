from django.contrib import admin


# Register your models here.
from inquest.models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "os", "sdk", "device", "model",
                    "is_active", "last_ping")
    list_filter = ("os", "sdk", "device", "model", "is_active")


admin.site.register(UserInfo, UserInfoAdmin)
