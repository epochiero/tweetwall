from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^tweetwall/$', TemplateView.as_view(template_name="index.html")),
	url(r'^tweetwall/signin$', 'tweetwall.views.signin'),
)

urlpatterns += staticfiles_urlpatterns()
