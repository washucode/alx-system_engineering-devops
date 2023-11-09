#!/usr/bin/python3
"""This module makes a query to Reddit API"""


def number_of_subscribers(subreddit):
    """This function returns the number of subscribers"""
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
