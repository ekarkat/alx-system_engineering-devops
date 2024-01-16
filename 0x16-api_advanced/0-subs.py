#!/usr/bin/python3
"""
Task 0 Module
"""
import requests


def number_of_subscribers(subreddit):
    """Return returns the number of subscribers"""
    headers = {"User-Agent": "MyCustomUserAgent/1.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        results = response.json().get("data")
        subs = results.get("subscribers")
        return output
    else:
        return 0
