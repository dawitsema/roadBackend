import json
from datetime import datetime
from task import Task


class TaskManager:
    def __init__(self) -> None:
        pass

    def add_task(self):
        print("\n\tWhat is the short description of your task? : ")
        description = input()
        task = Task(description)

        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            print("File not found. Creating a new file.")
            tasks = {}

        tasks[task.id] = task.to_json()

        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

        print("Task added successfully!")

    def update_task(self, task_id: str):
        print("\n\tWhat is the new description of your task? : ")
        new_desc = input()

        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        
        if task_id in tasks:
            tasks[task_id]["description"] = new_desc
            tasks[task_id]["updated_at"] = datetime.now().isoformat()

            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)

            print("Task updated successfully!")
        else:
            print(f"No task found with ID {task_id}.")

    def delete_task(self, task_id: str):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        if task_id in tasks:
            del tasks[task_id]

            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)

            print("Task deleted successfully!")
        else:
            print(f"No task found with ID {task_id}.")

    def change_status(self):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        print("Enter the ID number of the task: ")
        task_id = input()

        print("\t 1. Mark as In Progress")
        print("\t 2. Mark as Done")

        print("\n\tSelect from the choices: ")
        choice = int(input())

        if task_id in tasks:
            if choice == 1:
                self.shift_status(task_id, "In Progress")
            elif choice == 2:
                self.shift_status(task_id, "Done")
            else:
                print("Unknown command.")
        else:
            print(f"No task found with ID {task_id}.")

    def shift_status(self, task_id: str, status: str):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        if task_id in tasks:
            tasks[task_id]["status"] = status

            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)

            print(f"Task status updated to {status}.")
        else:
            print(f"No task found with ID {task_id}.")

    def list_specific(self, specific: str):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        print(f"All tasks with status '{specific}':")
        print(f"Id\t\tDescription\t\tCreated At\t\tUpdated At")
        for task_id, task in tasks.items():
            if task["status"] == specific:
                print(
                    f'{task_id}\t\t{task["description"]}\t{task["created_at"]}\t{task.get("updated_at", "N/A")}'
                )

    def list_all(self):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        print("All tasks:")
        print(f"Id\t\tDescription\t\tCreated At\t\tUpdated At\t\tStatus")
        for task_id, task in tasks.items():
            print(
                f'{task_id}\t\t{task["description"]}\t{task["created_at"]}\t{task.get("updated_at", "N/A")}\t\t{task["status"]}'
            )
