"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.views.generic import RedirectView

from resume.views import *


urlpatterns = [
    url(r'^$', HomeView.as_view()),

    # url(r'^apps/$', AppsHomeView.as_view()),
    # url(r'^other/$', OtherThingsView.as_view()),
    url(r'^resume/$', RedirectView.as_view(
        url=settings.STATIC_URL + 'files/NarendraNathJoshi.pdf',
        permanent=True)),
    url(r'^apps/$', RedirectView.as_view(url='/apps/inquest', permanent=True)),
    url(r'^other/$', RedirectView.as_view(url='/blog', permanent=True)),

    url(r'^apps/([a-z0-9]+)/$', AppLandingView.as_view()),
]
