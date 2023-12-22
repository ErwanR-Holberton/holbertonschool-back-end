#!/usr/bin/python3
"""export to json"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/todos",
                            params={"userId": argv[1]})
    response_user = requests.get("https://jsonplaceholder.typicode.com/users/"
                                 + argv[1])

    if response.status_code == 200 and response_user.status_code == 200:
        data = response.json()
        data_user = response_user.json()
        username = response_user.json()['username']

        all_tasks = {}
        list_of_tasks = []
        for task in data:
            task_dict = {}
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_dict["username"] = username

            list_of_tasks.append(task_dict)

        all_tasks["{}".format(argv[1])] = list_of_tasks

        with open("{}.json".format(argv[1]), "w+") as file:
            json.dump(all_tasks, file)
    else:
        print(f"Error: {response.status_code}, {response_user.status_code}")
