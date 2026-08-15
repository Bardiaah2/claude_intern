from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    """A single task tracked by TaskManager."""
    id: int
    title: str
    priority: str = "medium"  # one of: low, medium, high
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
