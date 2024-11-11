import json
from task import Task
import datetime

class TaskManager:
    def __init__(self) -> None:
        with open('tasks.json', 'w') as file:
            file.write("{}")
            
    def add_task(self):
        print('\n\twhat is the short description of your task? : ')
        description = input()
        task = Task(description=description)
        
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            
        tasks[task.id] = {
            "id" : task.id,
            "description" : task.description,
            "status" : task.status,
            "created_at" : task.created_at,
            "updated_at" : task.updated_at
        }
        
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)
            
    def update_task(self, id: id):
        print("\n\twhat is the new description of your task? : ")
        new_desc = input()
        
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            
        for task in tasks:
            if task == id:
                task['description'] = new_desc
                task['updated_at'] = datetime.now()
                
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)
            
            
    def delete_task(self, id: id):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            
        for task in tasks:
            if task == id:
                del tasks[id]
                
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)