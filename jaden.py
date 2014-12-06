#!/bin/env python2

import yaml
from twitter import Twitter, OAuth
from random import randint

config = yaml.load(open('config.yml'))


def get_client():
    return Twitter(auth=OAuth(
        config['access_token'],
        config['access_token_secret'],
        config['consumer_key'],
        config['consumer_secret']
    ))


def get_tweets(screen_name):
    return twitter.statuses.user_timeline(
        screen_name=screen_name,
        count=200,
        exclude_replies=True,
        include_rts=False
    )


if __name__ == '__main__':
    twitter = get_client()
    tweets = get_tweets('officialjaden')

    pick = randint(0, len(tweets) - 1)
    print tweets[pick]['text']
