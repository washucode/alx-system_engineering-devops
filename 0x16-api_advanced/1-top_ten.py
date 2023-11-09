#!/usr/bin/python3
"""This module makes a query to Reddit API"""


def top_ten(subreddit):
    """This function returns the number of subscribers"""
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for i in range(10):
            print(response.json()['data']['children'][i]['data']['title'])
    else:
        print('None')
