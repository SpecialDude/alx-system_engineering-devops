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

    print("Employee {} is done with".format(employee_name), end=" ")
    print("tasks({}/{}):".format(len(completed_todos), len(employee_todos)))
    for todo in completed_todos:
        print("\t {}".format(todo["title"]))


if __name__ == "__main__":
    main()
