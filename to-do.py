# Load existing to-do lists
# 1. Create a item
# 2. List items
# 3. Mark item as complete
# 4. save items

import json

file_name = 'to-do.json'


def load_tasks():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)

    except FileNotFoundError:
        return {"tasks": []}


def view_tasks(tasks):
    if len(tasks["tasks"]) >= 1:
        print("\nYour To-Do List tasks are:")
        for idx, task in enumerate(tasks["tasks"]):
            print(
                f"{idx + 1}. {task['description']}: {'COMPLETED' if task['complete'] else 'PENDING...'}")
    else:
        print("\nNo tasks to display. Please add a task")


def add_tasks(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("\nTask added")
    else:
        print("\nTask NOT added. Please enter a description")


def save_tasks(tasks):
    try:
        with open(file_name, 'w') as file:
            json.dump(tasks, file)
    except:
        print("Failed to save")


def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_to_complete = int(input(
            "Enter the task number to mark as complete: ").strip())

        if 1 <= task_to_complete <= len(tasks["tasks"]):
            tasks['tasks'][task_to_complete - 1]["complete"] = True
            save_tasks(tasks)
            print("\nTask marked as complete")

        else:
            print("\nInvalid Task Number")
    except:
        print("\nWrong Input! Enter a valid number.")


def main():

    tasks = load_tasks()

    while True:
        print("\n To-Do List Manager")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. Complete task")
        print("4. Exit")
        print()

        choice = input("What would you like to do (1/2/3/4): ").strip()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            print('\nGoodbye, come back next time')
            break
        else:
            print('\nInvalid input! Try again')


main()
