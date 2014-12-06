#!/bin/env python2

import yaml
from twitter import Twitter, OAuth

config = yaml.load(open('config.yml'))


def get_client():
    return Twitter(auth=OAuth(
        config['access_token'],
        config['access_token_secret'],
        config['consumer_key'],
        config['consumer_secret']
    ))


if __name__ == '__main__':
    client = get_client
