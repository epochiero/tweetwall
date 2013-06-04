# -*- coding: utf-8 *-*
from django.conf import settings
from twython import Twython
import logging

logger = logging.getLogger(__name__)

'''
This class handles Twitter requests

'''

class Twitter():
    def __init__(self, oauth_token=None, oauth_token_secret=None, callback_url=None):
        self.twython = Twython(app_key=settings.CONSUMER_KEY,
                               app_secret=settings.CONSUMER_SECRET, oauth_token=oauth_token,
                               oauth_token_secret=oauth_token_secret, callback_url=callback_url)

    def get_authentication_tokens(self):
        return self.twython.get_authentication_tokens()

    def get_authorized_tokens(self, oauth_verifier):
        return self.twython.get_authorized_tokens(oauth_verifier)

    def get_home_timeline(self):
        tweets = self.twython.request('statuses/home_timeline', params={'include_entities': '1'})
        logger.debug('tweets: ' + str(tweets))
        processed_tweets = [Tweet(tweet) for tweet in tweets]
        return processed_tweets


'''
This class handles processing of media urls

'''

class Tweet():

    def __init__(self, tweet):
        self.text = tweet['text']
        self.name = tweet['user']['name']
        self.profile_image =  tweet['user']['profile_image_url']
        self.youtube_links = []
        #self.process_links(tweet['entities']['urls'])

    def process_links(self, urls):
        if not urls:
            return
        for url in urls:
            for regex in self.REGEXES:
                if regex.match(url['expanded_url']):
                    link_url = url['expanded_url']
                    if 'youtube.com' in link_url:
                        self.youtube_links.append(link_url.split("v=")[1])
    




 