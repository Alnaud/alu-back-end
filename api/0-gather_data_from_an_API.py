#!/usr/bin/python3
"""Gather data from an API for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{emp_id}").json()
    todos = requests.get(f"{base_url}/todos", params={"userId": emp_id}).json()

    emp_name = user.get("name")
    done_tasks = [
        task.get("title") for task in todos if task.get("completed")
    ]

    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, len(done_tasks), len(todos)))

    for title in done_tasks:
        print("\t {}".format(title))
