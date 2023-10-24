#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv


if __name__ == "__main__":
    """Gather data from an API"""
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = argv[1]
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    employee_name = employee.get("name")
    employee_username = employee.get("username")
    employee_todos = requests.get(url + "todos",
                                  params={"userId": employee_id}).json()
    e_tasks = [task for task in employee_todos
               if task.get("completed") is True]
    output = "Employee {} is done with tasks({}/{}):".format(
        employee_name, len(e_tasks), len(employee_todos))
    for task in e_tasks:
        output += "\n\t {}".format(task.get("title"))
    print(output)
