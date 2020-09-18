#!/usr/bin/pythvon3
"""querie script"""
import requests


def number_of_subscribers(subreddit):
    """funtion"""
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "vandel"})
    json_request = response.json()
    subscribers = json_request.get('data', {}).get('subscribers', 0)
    return subscribers
