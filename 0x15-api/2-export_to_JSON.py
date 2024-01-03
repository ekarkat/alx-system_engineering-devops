import json
import requests
from sys import argv


if __name__ == "__main__":
    # task 0 function
    id = 2
    params_todo = {"userId": id}
    params_user = {"id": id}
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users"

    response_todo = requests.get(url_todo, params=params_todo)
    data_todo = response_todo.json()
    response_user = requests.get(url_user, params=params_user)
    data_user = response_user.json()

    username = data_user[0].get("username")
    list_todo = []

    for dic in data_todo:
        task = dic.get("title")
        completed = dic.get("completed")
        td = {"task": task, "completed": completed, "username": username}
        list_todo.append(td)

    output = {id: list_todo}

    # Specify the file path
    file_path = '{}.json'.format(id)

    # Open the file in write mode ('w')
    # If the file doesn't exist, it will be created
    # If the file already exists, its content will be truncated
    with open(file_path, 'w') as json_file:
        # Use json.dump() to write the data to the file
        json.dump(output, json_file, indent=2)  # indent for pretty formatting
