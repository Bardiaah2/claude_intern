from taskflow.manager import TaskManager


def test_add_task():
    tm = TaskManager()
    task = tm.add_task("Write onboarding doc", priority="high")
    assert task.title == "Write onboarding doc"
    assert task.priority == "high"
    assert not task.completed


def test_complete_task():
    tm = TaskManager()
    task = tm.add_task("Fix login bug")
    result = tm.complete_task(task.id)
    assert result is True
    assert task.completed is True


def test_pending_tasks_excludes_completed():
    tm = TaskManager()
    t1 = tm.add_task("Task 1")
    t2 = tm.add_task("Task 2")
    tm.complete_task(t1.id)
    pending = tm.get_pending_tasks()
    assert t1 not in pending
    assert t2 in pending


def test_get_tasks_by_priority():
    tm = TaskManager()
    tm.add_task("Low priority", priority="low")
    tm.add_task("High priority", priority="high")
    high_tasks = tm.get_tasks_by_priority("high")
    assert len(high_tasks) == 1
    assert high_tasks[0].title == "High priority"
