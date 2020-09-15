#!/usr/bin/python3
"""
request api
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    script
    """


    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(argv[1]))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1]))
    dict_users = users.json()
    dict_todos = todos.json()
    total = 0
    tasks = 0

    for i in dict_todos:
        if i.get('completed') is True:
            tasks += 1
        else:
            total += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(dict_users['name'], tasks, total + tasks))
    for i in dict_todos:
        if i.get('completed') is True:
            print('\t {}'.format(i.get('title')))
