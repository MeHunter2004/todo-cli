from typing import List, Optional
from models import Task
from storage import load_tasks, save_tasks


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = load_tasks()

    def _generate_id(self) -> int:
        return max((t.id for t in self.tasks), default=0) + 1

    def add_task(self, description: str) -> Task:
        task = Task(id=self._generate_id(), description=description)
        self.tasks.append(task)
        save_tasks(self.tasks)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def mark_completed(self, task_id: int) -> bool:
        for t in self.tasks:
            if t.id == task_id:
                t.completed = True
                save_tasks(self.tasks)
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        if len(self.tasks) != before:
            save_tasks(self.tasks)
            return True
        return False
