from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView, TemplateView
from index.views import HomeView, BlogView, WorkView, BlogWriteView, \
    PreviewAPIView, AutoSaveAPIView, BlogEntryView, TaggedView, BlogEditView, \
    HttpError404View, NewsletterSubscribeAPIView

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
    url(r'^api/v1/newsletters/subscribe$',
        NewsletterSubscribeAPIView.as_view()),

    # robots.txt and favicon
    url(r'^robots\.txt/$', TemplateView.as_view(
        template_name='robots.txt', content_type='text/plain')),
    url(r'^favicon\.ico/$', RedirectView.as_view(
        url='/static/favicon/favicon.ico', permanent=True)),

    # mobile redirects
    url(r'^m/?$', RedirectView.as_view(url='/blog', permanent=True)),
    url(r'^mobile/?$', RedirectView.as_view(url='/blog', permanent=True)),

    # other and misc pages
    url(r'^valentine/?$', login_required(TemplateView.as_view(
        template_name='vd.html', content_type='text/html'),
        login_url='/admin/login')),

    # error pages
    # url(r'^([a-zA-Z0-9-/]+)/?$', HttpError404View.as_view()),

]
