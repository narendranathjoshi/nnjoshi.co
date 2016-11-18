from django.contrib import admin


# Register your models here.
from inquest.models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "os", "sdk", "device", "model",
                    "is_active", "is_pro", "last_ping")
    list_filter = ("os", "sdk", "device", "model", "is_active", "is_pro")


admin.site.register(UserInfo, UserInfoAdmin)
