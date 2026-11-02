#!/usr/bin/python3
"""
Gathers data from a REST API and exports it into a CSV file.
"""
import csv
import requests
import sys


def export_to_csv():
    """Fetches user TODO tasks and saves them into a CSV file."""
    if len(sys.argv) < 2:
        return

    user_id = sys.argv[1]
    url = "https://typicode.com"

    # Fetch user details to get the correct username
    user_res = requests.get(f"{url}users/{user_id}")
    if user_res.status_code != 200:
        return
    username = user_res.json().get("username")

    # Fetch all tasks assigned to the user
    todos_res = requests.get(f"{url}todos?userId={user_id}")
    if todos_res.status_code != 200:
        return
    todos = todos_res.json()

    # Write records directly to a file named USER_ID.csv
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])


if __name__ == "__main__":
    export_to_csv()
