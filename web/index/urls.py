from django.conf.urls import url
from django.views.generic import RedirectView
from index.views import HomeView
from index.views import HomeView, BlogView ,WorkView

urlpatterns = [
    url('', HomeView.as_view())
    url(r'^work/$', WorkView.as_view())
]
