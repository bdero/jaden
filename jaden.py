#!/bin/env python2

import pyttsx
import yaml

from random import randint
from time import sleep
from twitter import Twitter, OAuth

config = yaml.load(open('config.yml'))


def get_tts():
    return pyttsx.init()


def get_client():
    return Twitter(auth=OAuth(
        config['access_token'],
        config['access_token_secret'],
        config['consumer_key'],
        config['consumer_secret']
    ))


def get_tweets(screen_name):
    raw_tweets = twitter.statuses.user_timeline(
        screen_name=screen_name,
        count=200,
        exclude_replies=True,
        include_rts=False
    )
    print 'Fetched', len(raw_tweets), 'tweets'

    tweets = filter(
        lambda t: t['text'].find('http') == -1,
        raw_tweets
    )
    print 'Filtered', len(raw_tweets) - len(tweets), 'tweets'

    return tweets


def say(tts, message):
    tts.say(message)
    tts.runAndWait()


if __name__ == '__main__':
    twitter = get_client()
    tweets = get_tweets('officialjaden')

    while True:
        pick = randint(0, len(tweets) - 1)
        tweet = tweets[pick]['text']

        print tweet
        tts = get_tts()
        say(tts, tweet)

        sleep(10)
