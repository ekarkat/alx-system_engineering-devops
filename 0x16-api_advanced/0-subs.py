#!/usr/bin/python3
""" Task 0 Module """
import requests


def number_of_subscribers(subreddit):
    """Return returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALX 0x16.api_advanced"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")
    else:
        return 0
