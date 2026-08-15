# Closed Tickets

## TF-101: complete_task() silently fails to complete tasks — CLOSED
Root cause: `task.id == str(task_id)` compared int to str, so the match
never succeeded. Fixed to `task.id == task_id`. All tests green.

---

# Open Tickets

## TF-102: Add task deletion support
**Priority:** Medium
**Status:** Unassigned → assigning to new intern

### Description
Product wants users to be able to delete a task outright (not just mark
it complete) — e.g. tasks added by mistake, duplicates, tests, etc. Add
a `delete_task(task_id)` method to `TaskManager`.

### Acceptance criteria
- [x] `delete_task(task_id)` removes the task if it exists
- [x] Returns something sensible to indicate success/failure — be
      consistent with how `complete_task` already signals that
- [x] Deleted tasks no longer show up in `get_pending_tasks()` or
      `get_tasks_by_priority()`
- [x] You write the tests this time — add them to `tests/test_manager.py`

### Notes
This one's loosely spec'd on purpose, closer to how real tickets show up.
Use your judgment on edge cases (e.g. deleting an ID that doesn't exist)
and use `complete_task` as your style reference for how this codebase
does things.
