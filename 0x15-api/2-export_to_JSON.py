#!/usr/bin/python3
"""
request api
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
    script
    """

    n = requests.get('https://jsonplaceholder.typicode.com/users/' + argv[1])
    username = n.json().get('username')
    link_todos = 'https://jsonplaceholder.typicode.com/todos'
    task = requests.get(link_todos, params={'userId': argv[1]})
    tasks = task.json()
    count = 0
    total = 0
    list_all = []
    dic_all = {}

    for x in tasks:
        dic = {}
        dic["task"] = x['title']
        dic["username"] = username
        dic["completed"] = x['completed']
        list_all.append(dic)
    dic_all = {argv[1]: list_all}
    with open('{}.json'.format(argv[1]), 'w') as json_file:
            json.dump(dic_all, json_file)
