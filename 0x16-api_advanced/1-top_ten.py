#!/usr/bin/python3
""" Task 0 Module """
import requests
import json

def top_ten(subreddit):
    """Return returns the hot list of a sub"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALX 0x16.api_advanced"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        return results
    else:
        return 0


file_path = "output.json"

# Write the dictionary to the JSON file
with open(file_path, 'w') as json_file:
    json.dump(top_ten("Morocco"), json_file, indent=2)  
