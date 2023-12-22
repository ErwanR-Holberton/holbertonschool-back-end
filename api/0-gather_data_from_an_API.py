#!/usr/bin/python3
"""get data from an api"""
import requests
from sys import argv


if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url1, params={"userId": argv[1]})
    response_user = requests.get(url2 + argv[1])

    data = response.json()
    data_user = response_user.json()
    name = response_user.json().get('name')
    completed = []

    for task in data:
        if task.get('completed') is True:
            completed.append(task)

    str1 = "Employee {}".format(name)
    str2 = "is done with tasks({}/{}):".format(len(completed), len(data))

    print(str1 + str2)
    for task in completed:
        print("\t " + task.get('title'))
