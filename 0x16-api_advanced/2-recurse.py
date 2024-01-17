#!/usr/bin/python3
"""Tasl 2 model"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """task 2"""
    headers = {"User-Agent": "MyCustomUserAgent/1.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data")
    after = data.get("after")
    for post in data.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
