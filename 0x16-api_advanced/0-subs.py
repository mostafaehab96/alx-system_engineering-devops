#!/usr/bin/python3

"""Get the number of subscribers for subreddit using reddit api"""
import requests


def number_of_subscribers(subreddit):
    with open('mytoken', 'r') as file:
        mytoken = file.read().strip('\n')

    headers = {
                'User-Agent': 'alxAPI/0.0.1',
                'Authorization': 'bearer {}'.format(mytoken)
              }

    res = requests.get('https://oauth.reddit.com/r/{}/about'.format(subreddit),
                       headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return (res.json()['data']['subscribers'])
    else:
        return 0
