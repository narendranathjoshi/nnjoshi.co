from django.conf.urls import url
from django.views.generic.base import RedirectView
from index.views import HomeView, BlogView ,WorkView

urlpatterns = [
    url(r'^about/$', HomeView.as_view()),
    url(r'^$', RedirectView.as_view(url='/blog/', permanent=False)),
    url(r'^blog/$', BlogView.as_view()),
    url(r'^work/$', WorkView.as_view())
]
