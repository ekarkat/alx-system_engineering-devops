#!/usr/bin/python3
""" TAsk0 model """

import requests
from sys import argv


if __name__ == "__main__":
    # task 0 function
    id = argv[1]
    params_todo = {"userId": id}
    params_user = {"id": id}
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users"

    response_todo = requests.get(url_todo, params=params_todo)
    data_todo = response_todo.json()

    response_user = requests.get(url_user, params=params_user)
    data_user = response_user.json()

    username = data_user[0].get("username")

    # Open a file in write mode ('w')
    # If the file doesn't exist, it will be created
    # If the file already exists, its content will be truncated
    with open('{}.csv'.format(id), 'w') as file:
        # Write content to the file
        for i in range(len(data_todo)):
            completed = data_todo[i].get("completed")
            title = data_todo[i].get("title")
            output = f'"{id}","{username}","{completed}","{title}"'
            file.write(output)
            if i != len(data_todo) - 1:
                file.write("\n")
