from taskflow.manager import TaskManager
from pytest import raises


def test_add_task():
    tm = TaskManager()
    task = tm.add_task("Write onboarding doc", priority=" High ")
    with raises(ValueError):
        task1 = tm.add_task("THIS IS AN URGENT TASK", priority="hiught")
    assert len(tm.get_pending_tasks()) == 1
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
    tm.add_task("Low priority", priority=" Low")
    tm.add_task("High priority", priority="high ")
    high_tasks = tm.get_tasks_by_priority("HiGh")
    assert len(high_tasks) == 1
    assert high_tasks[0].title == "High priority"

def test_delete_task():
    tm = TaskManager()
    task = tm.add_task("I want ice cream")
    task1 = tm.add_task("Task 1")
    task2 = tm.add_task("Task 2")
    task_id = task.id
    result = tm.delete_task(task.id)
    result1 = tm.delete_task(task_id)
    result2 = tm.delete_task(0)
    assert result is True
    assert result1 is False
    assert result2 is False
    assert len([t for t in tm.get_pending_tasks() if t.id == task_id]) == 0
    assert len([t for t in tm.get_tasks_by_priority("medium") if t.id == task_id]) == 0
    assert len(tm.get_pending_tasks()) == 2