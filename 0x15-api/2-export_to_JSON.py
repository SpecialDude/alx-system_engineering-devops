#!/usr/bin/python3

"""This module makes request to an API"""


import json
import requests
import sys


def main():
    """ Program Entry point """

    args = sys.argv[1:]

    if len(args) == 0:
        exit(1)

    employee_id = args[0]

    baseurl = "https://jsonplaceholder.typicode.com/"

    response = requests.get(baseurl + "users/" + employee_id)

    employee_data = json.loads(response.text)

    employee_name = employee_data["name"]

    response = requests.get(baseurl + "todos/?userId=" + employee_id)

    employee_todos = json.loads(response.text)

    completed_todos = [
                todo for todo in employee_todos
                if todo["completed"] is True
            ]

    # Outputs

    filename = employee_id + ".json"
    todos = [
                {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": employee_data["username"]
                }
                for todo in employee_todos
            ]

    data = {employee_id: todos}

    with open(filename, "w+") as fd:
        json.dump(data, fd)


if __name__ == "__main__":
    main()
