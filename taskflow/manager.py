from typing import *
from .models import Task
from datetime import datetime


class TaskManager:
    """In-memory manager for creating, completing, and querying tasks."""

    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add_task(self, title:str, priority:str="medium", due_at:datetime|None=None) -> Task:
        if (not isinstance(title, str)) or (not isinstance(priority, str)) or \
                    (not isinstance(due_at, (datetime, type(None)))):
            raise TypeError("add_task: title and priority: str, due_at: datetime|None")
        
        task = Task(id=self._next_id, title=title, priority=priority, due_at=due_at)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def complete_task(self, task_id) -> bool:
        """Mark a task as completed. Returns True if a task was found and updated."""
        if task_id in self._tasks.keys():
            self._tasks[task_id].completed = True
            return True
        return False

    def get_pending_tasks(self) -> List[Task]:
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

    def update_task(self, task_id:int, title:str=None, priority:str=None, due_at:datetime=None) -> bool:
        """update a task using task_id, if None is given for a argument, the parameter is not changed.  
        Returns False if task_id not found, and True if update was succesfful."""
        if (not isinstance(title, (str, type(None)))) or (not isinstance(priority, (str, type(None)))) or \
                (not isinstance(task_id, int)) or (not isinstance(due_at, (datetime, type(None)))):
            raise TypeError("update_task: task_id: int, title and priority:str|None, due_at: datetime|None")
        if task_id not in self._tasks.keys():
            return False
        task = self._tasks[task_id]
        pre_title, pre_due_at, pre_priority = task.title, task.due_at, task.priority
        if title is not None: task.title = title
        if due_at is not None: task.due_at = due_at
        if priority is not None: task.priority = priority
        try:
            task.check_values()
        except ValueError as e:
            task.title, task.due_at, task.priority = pre_title, pre_due_at, pre_priority
            raise ValueError(e)
        return True