#!/usr/bin/python3
"""
100-count
"""


def count_words(subreddit, word_list, after="", word_dict={}):
    """
    count_words
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python3"}
    params = {"limit": 100, "after": after}
    r = requests.get(url, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    data = r.json().get("data")
    after = data.get("after")
    children = data.get("children")
    for child in children:
        title = child.get("data").get("title")
        for word in word_list:
            if word.lower() in title.lower():
                if word.lower() not in word_dict:
                    word_dict[word.lower()] = 1
                else:
                    word_dict[word.lower()] += 1
    if after is None:
        if len(word_dict) == 0:
            return
        for key, value in sorted(word_dict.items(),
                                 key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(key, value))
    else:
        count_words(subreddit, word_list, after, word_dict)
