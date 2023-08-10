#!/usr/bin/python3

"""Get the number of subscribers for subreddit using reddit api"""
import requests


def number_of_subscribers(subreddit):

    headers = {'User-Agent': 'alxAPI'}
    res = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit),
                       headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return (res.json()['data']['subscribers'])
    else:
        return 0
