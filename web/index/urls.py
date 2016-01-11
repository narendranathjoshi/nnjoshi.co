from django.conf.urls import url
from django.views.generic.base import RedirectView
from index.views import HomeView, BlogView ,WorkView

urlpatterns = [
    url('', BlogView.as_view()),
    url(r'^about/$', HomeView.as_view()),
    url(r'^work/$', WorkView.as_view())
]
