#!/usr/bin/python3
"""get data and put it in a csv file"""
from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/todos",
                            params={"userId": argv[1]})
    response_user = requests.get("https://jsonplaceholder.typicode.com/users/"
                                 + argv[1])

    data = response.json()
    username = response_user.json().get('username')

    formated_data = []

    with open("{}.csv".format(argv[1]), "w") as file:
        for task in data:
            id = task.get("userId")
            completed = task.get("completed")
            title = task.get("title")
            file.write('"{}","{}","{}","{}"\n'
                       .format(id, username, completed, title))
