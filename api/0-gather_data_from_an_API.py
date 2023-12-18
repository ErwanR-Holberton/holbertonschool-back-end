#!/usr/bin/python3
import requests
from sys import argv

response = requests.get("https://jsonplaceholder.typicode.com/todos/" + argv[1])

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
