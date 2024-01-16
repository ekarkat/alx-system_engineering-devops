#!/usr/bin/python3
""" Task 0 Module """
import requests


def top_ten(subreddit):
    """Return returns the hot list of a sub"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALX 0x16.api_advanced"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data").get("children")
        i = 0
        for title in results:
            if i < 10:
                print(title.get("data").get("title"))
            i = i + 1
    else:
        print(None)
