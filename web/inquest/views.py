from django.utils import timezone
from rest_framework.generics import ListCreateAPIView

# Create your views here.
from rest_framework.response import Response
from inquest.models import UserInfo
from inquest.serializers import UserInfoSerializer
from web.utils import HttpStatusCode


class RegisterUserAPIView(ListCreateAPIView):
    serializer_class = UserInfoSerializer

    def post(self, request, *args, **kwargs):
        params = request.data
        user_info, created = UserInfo.objects.get_or_create(
            username=params["username"])
        if created:
            user_info.os = params["os"]
            user_info.build = params["build"]
            user_info.device = params["device"]
            user_info.sdk = params["sdk"]

        user_info.is_active = True
        user_info.last_ping = timezone.now()
        user_info.save()

        return Response(status=HttpStatusCode.ACCEPTED)
