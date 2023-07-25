#!/usr/bin/python3
"""Takes an id as argument and fetch infromation about a user
from https://jsonplaceholder.typicode.com/"""


if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    url = "https://jsonplaceholder.typicode.com/users/"
    user_id = argv[1] if len(argv) > 1 else None
    if user_id:
        user_url = url + user_id
        todos_url = user_url + "/todos"

        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()

        username = user.get("username")
        file_name = f"{user_id}.csv"
        with open(file_name, mode='w') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for todo in todos:
                status = todo.get("completed")
                title = todo.get("title")
                writer.writerow([user_id, username, status, title])
