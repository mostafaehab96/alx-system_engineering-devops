#!/usr/bin/python3

"""Gets top 10 most host posts of a subreddit using reddit api."""
import requests


def top_ten(subreddit):
    with open('mytoken', 'r') as file:
        mytoken = file.read().strip('\n')

    headers = {
                'User-Agent': 'alxAPI/0.0.1',
                'Authorization': 'bearer {}'.format(mytoken)
              }

    res = requests.get('https://oauth.reddit.com/r/{}/hot'.format(subreddit),
                       headers=headers, allow_redirects=False)

    if res.status_code == 200:
        posts = res.json().get('data').get('children')
        for post in posts[0: 10]:
            print(post.get('data').get('title'))
    else:
        print(None)

