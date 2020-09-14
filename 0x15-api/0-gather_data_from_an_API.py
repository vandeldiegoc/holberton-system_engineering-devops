#!/usr/bin/python3
"""create scrip"""
import requests
from sys import argv


if __name__ == "__main__":
    """coment module"""

    n = requests.get('https://jsonplaceholder.typicode.com/users/' + argv[1])
    name = n.json().get("name")
    link_todos = 'https://jsonplaceholder.typicode.com/todos'
    task = requests.get(link_todos, params={'userId': argv[1]})
    tasks = task.json()
    count = 0
    total = 0
    list_all = []

    for x in tasks:
        if x['completed'] is True:
            list_all.append(x['title'])
            count = count + 1
        total += 1
    print("Employee {} is done with tasks({}/{}):".format(name, count, total))
    for y in list_all:
        print("\t {}".format(y))
