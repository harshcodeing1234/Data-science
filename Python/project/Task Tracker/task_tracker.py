import sys
import os
import json
from datetime import datetime

json_file = "task.json"

def load_tasks():
    if not os.path.exists(json_file):
        return []
    try:
        with open(json_file, 'r') as f:
                return json.load(f)
    except json.JSONDecodeError:
            return []

def save_tasks(tasks):
      with open(json_file, 'w') as f:
            json.dump(tasks, f, indent=4)

def add_task(title, description):
    tasks = load_tasks()

    task_id = len(tasks) + 1
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = {
        "id"    : task_id,
        "title": title,
        "description": description,
        "status": "Todo",
        "created_at": current_time,
        "updated_at": current_time
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def update_task(task_id, title=None, description=None, status=None):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if status:
                task["status"] = status
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print("Task updated successfully.")
            return
    print("Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully.")

def change_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print("Task status changed successfully.")
            return
    print("Task not found.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command> [<args>]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 4:
            print("Usage: python task_tracker.py add <title> <description>")
            return
        title = sys.argv[2]
        description = sys.argv[3]
        add_task(title, description)

    elif command == "update":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py update <task_id> [<title>] [<description>] [<status>]")
            return
        task_id = int(sys.argv[2])
        title = sys.argv[3] if len(sys.argv) > 3 else None
        description = sys.argv[4] if len(sys.argv) > 4 else None
        status = sys.argv[5] if len(sys.argv) > 5 else None
        update_task(task_id, title, description, status)

    elif command == "delete":
        if len(sys.argv) != 3:
            print("Usage: python task_tracker.py delete <task_id>")
            return
        task_id = int(sys.argv[2])
        delete_task(task_id)

    elif command == "change_status":
        if len(sys.argv) != 4:
            print("Usage: python task_tracker.py change_status <task_id> <status>")
            return
        task_id = int(sys.argv[2])
        status = sys.argv[3]
        change_status(task_id, status)

    elif command == "list":
        list_tasks()

    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()

'''
cli-command examples:
1. python task_tracker.py add "Buy groceries" "Buy milk, bread, and eggs"
2. python task_tracker.py update 1 "Buy groceries" "Buy milk, bread, eggs, and cheese"
3. python task_tracker.py delete 1
4. python task_tracker.py change_status 2 "completed"
5. python task_tracker.py list
'''
