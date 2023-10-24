#!/usr/bin/python3
"""Export data in the CSV format"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    """Export data in the CSV format"""
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = argv[1]
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    employee_name = employee.get("name")
    employee_username = employee.get("username")
    employee_todos = requests.get(url + "todos",
                                  params={"userId": employee_id}).json()
    with open("{}.csv".format(employee_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in employee_todos:
            writer.writerow([employee_id, employee_username,
                             task.get("completed"), task.get("title")])
