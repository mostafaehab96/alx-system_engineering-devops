#!/usr/bin/python3

"""Prints a sorted count of given keywords in each hot title from subreddit."""
import requests


def count_words(subreddit, word_list, params=None, word_count={}):
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
        for post in posts:
            title = post.get('data').get('title').lower()
            for word in word_list:
                word_l = word.lower()
                count = title.count(word_l)
                if count:
                    word_count[word_l] = count + word_count.get(word_l, 0)
        after = res.json().get('data').get('after')
        if after:
            params = {'after': after}
            count_words(subreddit, word_list, params, word_count)
        else:
            sorted_count = dict(sorted(word_count.items(),
                                key=lambda i: i[1],
                                reverse=True))
            for k, v in sorted_count.items():
                print('{}: {}'.format(k, v))
