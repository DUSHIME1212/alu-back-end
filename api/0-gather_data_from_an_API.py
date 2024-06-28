#!/usr/bin/python3
"""
Python script that returns TODO list progress for a given employee ID
"""
import requests
from sys import argv

def get_employee_info(employee_id):
    """
    Get employee information by employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    return response.json()

def get_employee_todos(employee_id):
    """
    Get the TODO list of the employee by employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    return response.json()

def main(employee_id):
    """
    Main function to fetch and display the TODO list progress of the employee
    """
    employee = get_employee_info(employee_id)
    employee_name = employee.get("name")

    emp_todos = get_employee_todos(employee_id)
    total_tasks = len(emp_todos)
    completed_tasks = [todo for todo in emp_todos if todo.get("completed")]
    completed_tasks_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks}):")
    for todo in completed_tasks:
        print(f"\t {todo.get('title')}")

if __name__ == "__main__":
    if len(argv) > 1:
        main(int(argv[1]))
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
