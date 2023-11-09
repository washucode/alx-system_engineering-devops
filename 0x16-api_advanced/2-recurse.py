#!/usr/bin/python3
"""This module makes a query to Reddit API"""


def recurse(subreddit, hot_list=[], after=None):
    """This function returns the number of subscribers"""
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params={'after': after})
    if response.status_code == 200:
        for i in range(len(response.json()['data']['children'])):
            hot_list.append(response.json()['data']['children'][i]['data']
                            ['title'])
        after = response.json()['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
