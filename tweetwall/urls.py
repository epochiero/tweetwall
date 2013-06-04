from django.conf import settings
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
                       url(r'^$', 'tweetwall.views.index'),
                       url(r'^signin$', 'tweetwall.views.signin'),
                       url(r'^oauth_callback$', 'tweetwall.views.oauth_callback'),
                       url(r'^wall$', 'tweetwall.views.wall'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
