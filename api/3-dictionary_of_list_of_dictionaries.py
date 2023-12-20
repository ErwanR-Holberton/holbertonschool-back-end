#!/usr/bin/python3
"""format all to dos"""
import json
import requests

if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    response_user = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200 and response_user.status_code == 200:
        to_do = response.json()
        data_user = response_user.json()

        all_tasks = {}

        for user in data_user:
            id = user['id']
            username = user['username']
            list_of_tasks = []
            for task in to_do:
                if task['userId'] == id:
                    task_dict = {}
                    task_dict["username"] = username
                    task_dict["task"] = task["title"]
                    task_dict["completed"] = task["completed"]
                    list_of_tasks.append(task_dict)
            all_tasks["{}".format(id)] = list_of_tasks

        with open("todo_all_employees.json", "w+") as file:
            json.dump(all_tasks, file)
    else:
        print(f"Error: {response.status_code}, {response_user.status_code}")
