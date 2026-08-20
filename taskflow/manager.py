from .models import Task
from datetime import datetime


class TaskManager:
    """In-memory manager for creating, completing, and querying tasks."""

    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add_task(self, title:str, priority:str="medium", due_at:datetime|None=None):
        if (not isinstance(title, str)) or (not isinstance(priority, str)) or \
                    ((not isinstance(due_at, datetime)) and (due_at != None)):
            raise TypeError("add_task takes title and priority as a str and due_at either None or datetime.")
        
        task = Task(id=self._next_id, title=title, priority=priority, due_at=due_at)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def complete_task(self, task_id):
        """Mark a task as completed. Returns True if a task was found and updated."""
        for task in self._tasks.values():
            if task.id == task_id:
                task.completed = True
                return True
        return False

    def get_pending_tasks(self):
        return [t for t in self._tasks.values() if not t.completed]

    def get_tasks_by_priority(self, priority):
        priority = priority.lower().strip()
        return [t for t in self._tasks.values() if t.priority == priority]

    def delete_task(self, task_id):
        if task_id in self._tasks.keys():
            self._tasks.pop(task_id)
            return True
        return False

    def get_overdue_tasks(self):
        pending = [t for t in self.get_pending_tasks() if t.due_at is not None]
        return [t for t in pending if t.due_at <= datetime.now()]