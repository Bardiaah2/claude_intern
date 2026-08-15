from .models import Task


class TaskManager:
    """In-memory manager for creating, completing, and querying tasks."""

    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add_task(self, title, priority="medium"):
        task = Task(id=self._next_id, title=title, priority=priority)
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
        return [t for t in self._tasks.values() if t.priority == priority]

    def delete_task(self, task_id):
        if task_id in self._tasks.keys():
            self._tasks.pop(task_id)  # of the task exists, pop
            return True
        return False