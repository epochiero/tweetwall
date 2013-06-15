# -*- coding: utf-8 *-*
from django.conf import settings
from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from .twitter import Twitter


def index(request):
    if is_authenticated(request):
        return redirect(reverse('tweetwall.views.wall'))
    return render_to_response('index.html', {'settings': settings}, context_instance=RequestContext(request))


def signin(request):
    twitter = Twitter(callback_url=request.build_absolute_uri(reverse('tweetwall.views.oauth_callback')))
    auth_tokens = twitter.get_authentication_tokens()
    _save_tokens(request, auth_tokens)

    return redirect(auth_tokens['auth_url'])


def oauth_callback(request):
    twitter = Twitter(oauth_token=request.session.get('oauth_token'),
                      oauth_token_secret=request.session.get('oauth_token_secret'))
    oauth_verifier = request.GET.get("oauth_verifier")
    auth_tokens = twitter.get_authorized_tokens(oauth_verifier)
    _save_tokens(request, auth_tokens)

    return redirect(reverse('tweetwall.views.wall'))


def wall(request):
    twitter = Twitter(oauth_token=request.session.get('oauth_token'),
                      oauth_token_secret=request.session.get('oauth_token_secret'))

    tweets = twitter.get_home_timeline()
    return render_to_response('wall.html', {'tweets': tweets,
                                            'settings': settings}, context_instance=RequestContext(request))


def _save_tokens(request, auth_tokens):
    request.session['oauth_token'] = auth_tokens['oauth_token']
    request.session['oauth_token_secret'] = auth_tokens['oauth_token_secret']


def is_authenticated(request):
    return request.session.get('oauth_token')