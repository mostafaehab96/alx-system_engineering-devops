#!/usr/bin/python3

"""Gets top 10 most host posts of a subreddit using reddit api."""
import requests


def top_ten(subreddit):

    headers = {'User-Agent': 'alxAPI'}

    res = requests.get('https://www.reddit.com/r/{}/hot.json'
                       .format(subreddit),
                       headers=headers, allow_redirects=False)

    if res.status_code == 200:
        posts = res.json().get('data').get('children')
        for post in posts[0: 10]:
            print(post.get('data').get('title'))
    else:
        print(None)
