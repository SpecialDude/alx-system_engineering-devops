#!/usr/bin/python3

"""This module makes request to an API"""


import json
import requests
import sys


baseurl = "https://jsonplaceholder.typicode.com/"


def fetch_employee_todos(employee_id, employee_username):
    """ Fetches all the todos for the specified employee """

    response = requests.get(baseurl + "todos/?userId=" + employee_id)

    employee_todos = json.loads(response.text)

    # Outputs
    todos = [
                {
                    "username": employee_username,
                    "task": todo["title"],
                    "completed": todo["completed"],
                }
                for todo in employee_todos
            ]

    return todos


def main():
    """ Program Entry point """

    response = requests.get(baseurl + "users")

    all_employee = json.loads(response.text)

    data = {
            employee["id"]: fetch_employee_todos(
                    str(employee["id"]), employee["username"]
                )
            for employee in all_employee
        }

    with open("todo_all_employees.json", "w+") as fd:
        json.dump(data, fd)


if __name__ == "__main__":
    main()
