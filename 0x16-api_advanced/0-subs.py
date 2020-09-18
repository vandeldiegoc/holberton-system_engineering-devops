#!/usr/bin/python3
"""querie script"""
import requests


def number_of_subscribers(subreddit):
    """funtion"""
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "vandel"}
    response = requests.get(url, headers=headers)
    json_request = response.json()
    subscribers = json_request.get('data', {}).get('subscribers', 0)
    return subscribers
