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
        json_report = {}
        list_report = []
        for task in employee_todos:
            user_report = {}
            user_report["task"] = task.get("title")
            user_report["completed"] = task.get("completed")
            user_report["username"] = employee_username
            list_report.append(user_report)
            print(list_report)
        json_report[employee_id] = list_report
        json.dump(json_report, jsonfile)
