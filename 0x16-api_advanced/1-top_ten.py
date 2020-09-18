#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """ funtion """
    if subreddit is None:
        return 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "dsdsad"}
    limit = {"limit": 10}
    response = requests.get(url, headers=headers, params=limit)
    json_request = response.json()
    l_json = json_request.get('data', {}).get('children', None)
    if l_json:
        for item in l_json:
            print(item.get('data').get('title'))
    else:
        print(None)
