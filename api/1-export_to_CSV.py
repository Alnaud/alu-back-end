#!/usr/bin/python3
"""Export employee tasks from an API to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    emp_id = sys.argv
    base_url = "https://typicode.com"

    user = requests.get(f"{base_url}/users/{emp_id}").json()
    todos = requests.get(f"{base_url}/todos", params={"userId": emp_id}).json()

    username = user.get("username")
    filename = f"{emp_id}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
