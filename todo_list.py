from utils import print_task

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})
        print(f"Task '{task}' added!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        for i, task in enumerate(self.tasks):
            print_task(i, task)

    def mark_done(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id]['done'] = True
            print(f"Task {task_id} marked as done.")
        else:
            print("Invalid task ID")
