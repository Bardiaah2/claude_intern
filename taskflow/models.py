from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Task:
    """A single task tracked by TaskManager.  
    Priorities: low, medium, high"""
    _PRIORITIES = {"low", "medium", "high"}
    id: int
    title: str
    priority: str = "medium"
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    due_at: datetime | None = None
    

    def __post_init__(self):
        self.check_values()

    def check_values(self):
        # add more checks as this dataclass evolves, post_init and this may need different actions
        self.priority = self.priority.lower().strip()
        if self.priority not in self._PRIORITIES:
            raise ValueError("Task can only take low, medium and high as priorities.")