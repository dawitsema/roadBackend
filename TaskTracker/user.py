
from task_manager import TaskManager

taskManager = TaskManager()
print("\n\tWelcome to your own Task Tracker\n")
commands = {
    1 : "Add, Update, and Delete tasks",
    2 : "Mark a task as in progress or done",
    3 : "List all tasks",
    4 : "List all tasks that are done",
    5 : "List all tasks that are not done",
    6 : "List all tasks that are in progress"
}
while True:
    for key in commands:
        print(key, commands[key])
        
    print('What do you want to do?\n')
    print("your choice : ")
    order = int(input())

    if order == 1:
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task\n")
        print("Okay, choose further action: ")
        choose = int(input())
        if choose == 1:
            taskManager.add_task()
        elif choose == 2:
            taskManager.list_all()
            print("\n\nGive me an id of task to be updated: ")
            id = input()
            taskManager.update_task(id)
        elif choose == 3:
            taskManager.list_all()
            print("\n\nGive me an id of task to be deleted: ")
            id = input()
            taskManager.delete_task(id)
        else:
            print("Unknown command")
        
    elif order == 2:
        taskManager.list_all()
        taskManager.change_status()
        
        pass
    elif order == 3:
        taskManager.list_all()
    elif order == 4:
        taskManager.list_specific("Done")
    elif order == 5:
        taskManager.list_specific("To Do")
    elif order == 6:
        taskManager.list_specific("In Progress")
        
    
    print("Do you want to continue y/n? ")
    action = input()
    if action.lower() == 'n':
        break
