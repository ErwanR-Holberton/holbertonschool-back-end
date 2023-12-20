#!/usr/bin/python3
"""get data and put it in a csv file"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/todos",
                            params={"userId": argv[1]})
    response_user = requests.get("https://jsonplaceholder.typicode.com/users/"
                                 + argv[1])

    if response.status_code == 200 and response_user.status_code == 200:
        data = response.json()
        name = response_user.json()['username']

        formated_data = []

        with open("{}.csv".format(argv[1]), "w") as file:
            for task in data:
                row = [task["userId"], name, task["completed"], task["title"]]
                formated_data.append(row)
                """file.write('"{}","{}","{}","{}"\n'
                           .format(task["userId"], username, task["completed"],
                                   task["title"]))"""
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(formated_data[1:])
    else:
        print(f"Error: {response.status_code}, {response_user.status_code}")
