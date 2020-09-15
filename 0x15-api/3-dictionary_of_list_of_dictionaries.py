#!/usr/bin/python3
"""
request api
"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    """
    script
    """

    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    final_dict = {}
    for user in users:
        id_use = user.get("id")
        all_user = requests.get("{}/{}/todos".format(url, id_use)).json()
        result = []
        for task in all_user:
            result.append({'task': task.get('title'), 'completed': task.get
                           ('completed'), 'username': user.get('username')})
        final_dict[id_use] = result
        with open("todo_all_employees.json", "w") as file_json:
            json.dump(final_dict, file_json)
