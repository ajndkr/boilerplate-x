"""
A simple todo app in Python.

This app allows users to add, view, and delete tasks from a todo list.

Usage:
    python todo.py [command] [task]

Commands:
    add     Add a new task to the todo list
    view    View all tasks in the todo list
    delete  Delete a task from the todo list

Examples:
    python todo.py add "Buy groceries"
    python todo.py view
    python todo.py delete 1

"""

import sys

# Define the todo list
todo_list = []

# Define the add function
def add_task(task):
    todo_list.append(task)
    print("Task added successfully!")

# Define the view function
def view_tasks():
    if len(todo_list) == 0:
        print("No tasks found.")
    else:
        for i, task in enumerate(todo_list):
            print(f"{i+1}. {task}")

# Define the delete function
def delete_task(index):
    try:
        task = todo_list.pop(index-1)
        print(f"Task '{task}' deleted successfully!")
    except IndexError:
        print("Invalid task index.")

# Parse the command line arguments
if len(sys.argv) < 2:
    print("Usage: python todo.py [command] [task]")
    sys.exit()

command = sys.argv[1]

if command == "add":
    if len(sys.argv) < 3:
        print("Usage: python todo.py add [task]")
        sys.exit()
    task = " ".join(sys.argv[2:])
    add_task(task)

elif command == "view":
    view_tasks()

elif command == "delete":
    if len(sys.argv) < 3:
        print("Usage: python todo.py delete [index]")
        sys.exit()
    index = int(sys.argv[2])
    delete_task(index)

else:
    print("Invalid command.")
    sys.exit()
"""
