#!/usr/bin/python3
"""Takes an id as argument and fetch infromation about a user
from https://jsonplaceholder.typicode.com/"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/users/"
    user_id = argv[1] if len(argv) > 1 else None
    if user_id:
        user_url = url + user_id
        todos_url = user_url + "/todos"

        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()

        if user:
            name = user.get("name")
            total = 0
            completed = 0
            titles = []
            for todo in todos:
                total += 1
                if todo.get("completed"):
                    completed += 1
                    titles.append(todo.get("title"))

            print(f"Employee {name} is done with tasks({completed}/{total}):")
            for title in titles:
                print(f"\t {title}")
