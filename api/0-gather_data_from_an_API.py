#!/usr/bin/python3
"""Exports all employees' TODO list data to a JSON file."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://typicode.com"
    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    all_data = {}
    for user in users:
        uid = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == uid
        ]
        all_data[str(uid)] = user_tasks

    with open("todo_all_employees.json", mode="w", encoding="utf-8") as f:
        json.dump(all_data, f)

