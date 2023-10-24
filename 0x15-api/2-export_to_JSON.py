#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    """Export data in the JSON format"""
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = argv[1]
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    employee_username = employee.get("username")
    employee_todos = requests.get(url + "todos",
                                  params={"userId": employee_id}).json()

    with open("{}.json".format(employee_id), "w") as jsonfile:
        for task in employee_todos:
            task["task"] = task.pop("title")
            task["completed"] = task.pop("completed")
            task["username"] = employee_username
            del task["id"]
            json.dump(task, jsonfile)
