#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    """Export data in the JSON format"""

    url = "https://jsonplaceholder.typicode.com/"
    all_employees = requests.get(url + "users").json()
    employees_dict = {}
    for employee in all_employees:
        employee_dict = {}
        employee_id = employee.get("id")
        employee_username = employee.get("username")
        employee_todos = requests.get(url + "todos",
                                      params={"userId": employee_id}).json()
        list_report = []
        for task in employee_todos:
            user_report = {}
            user_report["username"] = employee_username
            user_report["task"] = task.get("title")
            user_report["completed"] = task.get("completed")
            list_report.append(user_report)
        employee_dict[employee_id] = list_report
        employees_dict.update(employee_dict)

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(employees_dict, jsonfile)
