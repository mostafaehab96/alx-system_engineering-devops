#!/usr/bin/python3
"""Takes an id as argument and fetch infromation about a user
from https://jsonplaceholder.typicode.com/"""


if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    url = "https://jsonplaceholder.typicode.com/users/"
    user_id = argv[1] if len(argv) > 1 else None
    if user_id:
        user_url = url + user_id
        todos_url = user_url + "/todos"

        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()

        username = user.get("username")
        file_name = f"{user_id}.json"
        with open(file_name, mode='w') as file:
            data = {user_id: []}
            for todo in todos:
                task = {}
                status = todo.get("completed")
                title = todo.get("title")
                task["task"] = title
                task["completed"] = status
                task["username"] = username
                data.get(user_id).append(task)
            json.dump(data, file)
