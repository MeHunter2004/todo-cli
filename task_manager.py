from models import Task
from storage import load_tasks, save_tasks


class TaskManager:

    def __init__(self):
        self.tasks = load_tasks()

    def _generate_id(self):
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1

    def add_task(self, title):
        task = Task(id=self._generate_id(), title=title)
        self.tasks.append(task.to_dict())
        save_tasks(self.tasks)

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        save_tasks(self.tasks)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
        save_tasks(self.tasks)

    def list_tasks(self):
        return self.tasks
