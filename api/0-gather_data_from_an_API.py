#!/usr/bin/python3
"""get data from an api"""
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
        name = response_user.json()['name']
        completed = []

        for task in data:
            if task['completed'] is True:
                completed.append(task)

        print("Employee {} is done with tasks({}/{}):"
              .format(name, len(completed), len(data)))
        for task in completed:
            print("\t " + task.get('title'))
    else:
        print(f"Error: {response.status_code}, {response_user.status_code}")
