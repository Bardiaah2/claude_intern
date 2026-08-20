# Closed Tickets

## TF-101: complete_task() silently fails to complete tasks — CLOSED
Root cause: `task.id == str(task_id)` compared int to str, so the match
never succeeded. Fixed to `task.id == task_id`. All tests green.

closed on 862ea73

## TF-102: Add task deletion support — CLOSED
Added `delete_task(task_id)`. Correct approach uses membership check
(`task_id in self._tasks`), returns True/False consistent with
`complete_task`. Test suite covers happy path, double-delete, and
delete-of-nonexistent-id.

closed on 29bdb45

## TF-103: add_task() accepts invalid priority values — CLOSED
Validation moved into `Task.__post_init__`, normalizing (lowercase/strip)
then hard-checking against {"low", "medium", "high"}, raising ValueError
on anything else. Correctly implemented via __post_init__ rather than a
hand-rolled __init__, preserving dataclass-generated __eq__/__repr__ and
proper default_factory behavior for created_at.

closed on dcc3eb5

---

# Open Tickets

## TF-104: Add due dates and overdue detection
**Priority:** Medium
**Status:** Unassigned → assigning to new intern

### Description
Product wants tasks to optionally have a due date, plus a way to see
which tasks are overdue — due date has passed, and the task isn't done
yet.

### Acceptance criteria
- [x] `Task` gains an optional due date. Existing code that creates tasks
      without one must keep working exactly as before
- [x] `add_task()` supports optionally passing a due date
- [x] New `get_overdue_tasks()` method on `TaskManager` returns pending
      tasks whose due date has passed
- [x] A task with no due date is never considered overdue
- [x] A completed task is never considered overdue, even if its due date
      is in the past
- [x] Tests covering: no due date, future due date, past due date + still
      pending, past due date + completed

### Notes
Think about what type a due date should be, and stay consistent with how
`created_at` is already handled in this codebase. Also — think carefully
about default values here. You already had to reason hard about defaults
once on this ticket set (inside `Task`); bring that same level of
paranoia to this one too.