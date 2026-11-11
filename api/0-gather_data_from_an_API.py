#!/usr/bin/python3
"""Fetches and displays an employee's TODO list progress from a REST API."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    emp_id = sys.argv[1]
    base_url = "https://typicode.com"

    user_res = requests.get("{}/users/{}".format(base_url, emp_id)).json()
    todos_res = requests.get(
        "{}/todos".format(base_url), params={"userId": emp_id}
    ).json()

    employee_name = user_res.get("name")
    done_tasks = [task for task in todos_res if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos_res)
    ))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))

