#!/usr/bin/python3
"""
request api
"""
import csv
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
    list_all = []
    list_status = []
    for x in tasks:
        list_all.append(x['title'])
        list_status.append(x['completed'])
    with open("{}.csv".format(argv[1]), "w") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for y in range(len(list_status)):
                writer.writerow([argv[1], username, list_status[y],
                                list_all[y]])
