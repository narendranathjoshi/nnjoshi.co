from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from index.views import HomeView, BlogView, WorkView, BlogWriteView, \
    PreviewAPIView, AutoSaveAPIView, BlogEntryView, TaggedView, BlogEditView

urlpatterns = [
    url(r'^about/?$', HomeView.as_view()),
    url(r'^$', RedirectView.as_view(url='/blog', permanent=True)),
    url(r'^blog/?$', BlogView.as_view()),
    url(r'^blog/post/([a-z0-9-]+)/?$', BlogEntryView.as_view()),
    url(r'^blog/tagged/([a-z0-9-]+)/?$', TaggedView.as_view()),
    url(r'^blog/write/?$', login_required(
        BlogWriteView.as_view(), login_url='/admin/login')),
    url(r'^blog/edit/([a-z0-9-]+)/?$', login_required(
        BlogEditView.as_view(), login_url='/admin/login')),
    url(r'^work/?$', WorkView.as_view()),

    # API views
    url(r'^api/v1/preview/?$', PreviewAPIView.as_view()),
    url(r'^api/v1/save/?$', AutoSaveAPIView.as_view()),
]
