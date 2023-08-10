#!/usr/bin/python3

"""Gets top 10 most host posts of a subreddit using reddit api."""
import requests


def recurse(subreddit, hot_list=[], params=None):

    headers = {'User-Agent': 'alxAPI'}

    res = requests.get('https://www.reddit.com/r/{}/hot.json'
                       .format(subreddit),
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
