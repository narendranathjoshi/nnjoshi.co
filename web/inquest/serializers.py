from rest_framework import serializers
from inquest.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ("id", "username", "os", "sdk", "device", "build",
                  "is_active", "last_ping")
