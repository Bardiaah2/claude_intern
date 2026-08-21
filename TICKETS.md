# Closed Tickets

## TF-101: complete_task() silently fails to complete tasks — CLOSED
Root cause: `task.id == str(task_id)` compared int to str, so the match
never succeeded. Fixed to `task.id == task_id`. All tests green.

## TF-102: Add task deletion support — CLOSED
Added `delete_task(task_id)`. Correct approach uses membership check
(`task_id in self._tasks`), returns True/False consistent with
`complete_task`. Test suite covers happy path, double-delete, and
delete-of-nonexistent-id.

## TF-103: add_task() accepts invalid priority values — CLOSED
Validation moved into `Task.__post_init__`, normalizing (lowercase/strip)
then hard-checking against {"low", "medium", "high"}, raising ValueError
on anything else. Correctly implemented via __post_init__ rather than a
hand-rolled __init__, preserving dataclass-generated __eq__/__repr__ and
proper default_factory behavior for created_at.

---

# Open Tickets

## TF-104: Add due dates and overdue detection — CLOSED
Added optional `due_at: datetime | None` to `Task`, `get_overdue_tasks()`
on `TaskManager` (pending + due_at not None + due_at <= now). Type
checking added to `add_task()` using `isinstance()`, deliberately kept
separate from `Task`'s own value validation — TypeError for wrong type,
ValueError for right type/wrong value. Tests cover no due date, future,
past+pending, and past+completed.

---

# Open Tickets

## TF-105: Add update_task() to edit existing tasks
**Priority:** Medium
**Status:** Unassigned → assigning to new intern

### Description
Users need to edit a task after creating it — fix a typo in the title,
bump the priority, push back the due date — without deleting and
re-adding it. Add `update_task(task_id, title=None, priority=None,
due_at=None)` to `TaskManager`. Only the fields actually passed in
should change; anything left as `None` should stay whatever it already
was.

### Acceptance criteria
- [x] `update_task()` updates only the fields provided, leaves the rest
      untouched
- [x] Returns something sensible for found/not-found, consistent with
      how the rest of this codebase signals that
- [x] All existing validation rules still apply — an invalid priority
      (wrong type or wrong value) or an invalid `due_at` type must be
      rejected exactly the same way it would be on creation. No
      exceptions to that.
- [x] Tests covering: a valid partial update (e.g. title only), an
      invalid priority update, an invalid `due_at` type update, and an
      update on a task id that doesn't exist

### Notes
This one sits directly on top of what you already built for TF-103 and
TF-104. Before you write any code: think hard about *how* validation
currently gets triggered on a `Task` at all, and whether that mechanism
still fires if your update logic just does something like
`task.title = new_title` directly on an existing instance.