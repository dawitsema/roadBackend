# Task Tracker CLI

Task Tracker CLI is a command-line application designed to manage tasks efficiently. It allows users to add, update, delete, and list tasks with various statuses ``` todo, in-progress, done ```. Tasks are stored persistently in a JSON file within the current directory.


## Features

- 1. Add Tasks: Create new tasks with a unique ID and a short description.
- 2. Update Tasks: Modify the description of existing tasks.
- 3. Delete Tasks: Remove tasks by their ID.
- 4. Change Status: Mark tasks as ``` in-progress ``` or ```done```.
- 5. List Tasks:
    - List all tasks.
    - Filter tasks by status ```todo, in-progress, done```
- 6. Persistent Storage: Tasks are saved in a JSON file in the current directory.


## Task Properties

- id: A unique identifier for the task.
- description: A short description of the task.
- status: The current status of the task (todo, in-progress, done).
- createdAt: The timestamp when the task was created.
- updatedAt: The timestamp when the task was last updated.

@dawitsema source of motivation: ```https://roadmap.sh/projects/task-tracker```