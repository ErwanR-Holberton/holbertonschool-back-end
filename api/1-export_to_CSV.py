#!/usr/bin/python3
"""get data and put it in a csv file"""
import requests
from sys import argv


if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url1, params={"userId": argv[1]})
    response_user = requests.get(url2 + argv[1])

    data = response.json()
    username = response_user.json().get('username')

    formated_data = []

    with open("{}.csv".format(argv[1]), "w") as file:
        for task in data:
            id = task.get("userId")
            completed = task.get("completed")
            title = task.get("title")
            str1 = '"{}","{}"'.format(id, username)
            str2 = ',"{}","{}"\n'.format(completed, title)
            file.write(str1 + str2)
