from dataclasses import dataclass, field
from datetime import datetime
# from enum import Enum

# class Priority(Enum):
#     LOW = "low"
#     MEDIUM = "medium"
#     HIGH = "high"


@dataclass
class Task:
    """A single task tracked by TaskManager.  
    Priorities: low, medium, high"""
    __PRIORITIES = {"low", "medium", "high"}
    id: int
    title: str
    priority: str = "medium"
    

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.completed: bool = False
        self.created_at: datetime = field(default_factory=datetime.now)

        self.priority = self.priority.lower().strip()
        # if self.priority in Priority._value2member_map_.keys():
        #     self.priority = Priority._value2member_map_[self.priority]
        if self.priority in self.__PRIORITIES:
            pass
        else:
            raise ValueError("Task can only take low, medium and high as priorit.")