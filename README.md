# todo_list
This is a simple to-do list application built using Flask, a lightweight web framework for Python. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations and serves as an introductory example of how to create a web application with Flask.

Features
Add Tasks: Users can add new tasks to their to-do list.
Complete Tasks: Users can mark tasks as completed.
Delete Tasks: Users can delete tasks from their to-do list.
In-Memory Storage: Tasks are stored in memory (ideal for learning and demonstration purposes).

Project Structure:
todo_list/
│
├── app.py                # Main application file
├── templates/
│   └── index.html        # HTML template for the to-do list
└── static/
    └── style.css         # CSS file for styling the to-do list

    
Usage:
Add a Task: Enter a task description in the input field and click the "Add" button.
Complete a Task: Click the "Complete" link next to a pending task to mark it as completed.
Delete a Task: Click the "Delete" link next to any task to remove it from the list.
