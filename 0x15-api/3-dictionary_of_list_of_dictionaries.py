#!/usr/bin/python3
"""Takes an id as argument and fetch infromation about a user
from https://jsonplaceholder.typicode.com/"""


if __name__ == "__main__":
    import requests
    import json

    url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(url).json()
    all_todos = {}
    for user in users:
        username = user.get("username")
        ID = str(user.get("id"))
        todos = requests.get(url + ID + "/todos").json()
        all_todos[ID] = []
        for todo in todos:
            new = {}
            new["username"] = username
            new["task"] = todo.get("title")
            new["completed"] = todo.get("completed")
            all_todos[ID].append(new)

    with open("todo_all_employees.json", 'w') as file:
        json.dump(all_todos, file)
