#!/usr/bin/python3

"""This module makes request to an API"""


import csv
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

    filename = employee_id + ".csv"
    data = [
                '"{}","{}","{}","{}"\n'.format(
                    employee_id, employee_data["username"],
                    todo["completed"], todo["title"]
                )
                for todo in employee_todos
            ]

    with open(filename, "w+") as fd:
        for line in data:
            fd.write(line)


if __name__ == "__main__":
    main()
