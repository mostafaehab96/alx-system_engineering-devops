#!/usr/bin/python3

"""Gets top 10 most host posts of a subreddit using reddit api."""
import requests


def recurse(subreddit, hot_list=[], params=None):
    with open('mytoken', 'r') as file:
        mytoken = file.read().strip('\n')

    headers = {
                'User-Agent': 'alxAPI/0.0.1',
                'Authorization': 'bearer {}'.format(mytoken)
              }

    res = requests.get('https://oauth.reddit.com/r/{}/hot'.format(subreddit),
                       headers=headers, allow_redirects=False, params=params)

    if res.status_code == 200:
        posts = res.json().get('data').get('children')
        hot_list.extend(posts)
        after = res.json().get('data').get('after')
        if after:
            params = {'after': after}
            return recurse(subreddit, hot_list, params)
        else:
            return hot_list
    else:
        return None
