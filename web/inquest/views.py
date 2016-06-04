from django.utils import timezone
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from inquest.models import UserInfo
from inquest.serializers import UserInfoSerializer
from web.utils import HttpStatusCode


# helper functions
def get_full_mailing_list():
    return [user_info.username for user_info in UserInfo.objects.filter(
        is_email=True
    )]


def get_active_full_mailing_list():
    return [user_info.username for user_info in UserInfo.objects.filter(
        is_email=True, is_active=True
    )]


def get_active_non_pro_mailing_list():
    return [user_info.username for user_info in UserInfo.objects.filter(
        is_email=True, is_pro=False, is_active=True
    )]


def get_active_pro_mailing_list():
    return [user_info.username for user_info in UserInfo.objects.filter(
        is_email=True, is_pro=True, is_active=True
    )]


def get_not_active_mailing_list():
    return [user_info.username for user_info in UserInfo.objects.filter(
        is_email=True, is_active=False
    )]


# Create your views here.
class RegisterUserAPIView(UpdateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            params = request.data
            user_info, created = UserInfo.objects.get_or_create(
                username=params["username"])
            if created:
                user_info.os = params["os"]
                user_info.model = params["model"]
                user_info.device = params["device"]
                user_info.sdk = params["sdk"]

            user_info.is_active = True
            user_info.last_ping = timezone.now()
            user_info.save()

            return Response(status=HttpStatusCode.ACCEPTED)
        except Exception as e:
            return Response(
                {"msg": e.message}, status=HttpStatusCode.BAD_REQUEST)

