#!/usr/bin/python3
"""
Python script that returns TODO list progress for a given employee ID
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
    Request user info by employee ID
    """
    employee_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    user_url = user_url.format(employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    todos_url = todos_url.format(employee_id)

    # Get user info
    user_response = requests.get(user_url)
    user = user_response.json()
    employee_name = user.get("name")

    # Get user's TODO list
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Calculate completed tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
