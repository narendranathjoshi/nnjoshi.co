from django.conf.urls import url
from django.views.generic import RedirectView
from index.views import HomeView

urlpatterns = [
    url('', HomeView.as_view())
]
