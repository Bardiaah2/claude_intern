# Closed Tickets
 
## TF-101: complete_task() silently fails to complete tasks — CLOSED
Root cause: `task.id == str(task_id)` compared int to str, so the match
never succeeded. Fixed to `task.id == task_id`. All tests green.
 
---
 
# Open Tickets
 
## TF-102: Add task deletion support — CLOSED
Added `delete_task(task_id)`. Correct approach uses membership check
(`task_id in self._tasks`), returns True/False consistent with
`complete_task`. Test suite covers happy path, double-delete, and
delete-of-nonexistent-id.
 
---
 
# Open Tickets
 
## TF-103: add_task() accepts invalid priority values
**Reported by:** QA
**Priority:** Medium
**Status:** Unassigned → assigning to new intern
 
### Description
QA noticed `add_task()` happily accepts any string as `priority` — not
just `low`/`medium`/`high`. e.g. `tm.add_task("food", priority="urgent")`
succeeds silently. Since `get_tasks_by_priority()` (and presumably other
code down the line) assumes only those three values exist*, a task with a
typo'd or made-up priority becomes invisible to any priority-based
lookup, even though it's a perfectly real task sitting in `_tasks`.
 
### Acceptance criteria
- [x] `add_task()` rejects invalid priority values
- [x] Decide what "rejects" means — raise an exception? default silently
      to `"medium"`? something else? Your call, but be ready to explain
      why you picked it
- [x] Add tests covering both valid and invalid priority values
- [x] Existing tests still pass
### Notes
Remember the discussion on TF-101 about internal code staying strict and
failing loud instead of silently doing the wrong thing? This is a good
place to actually put that into practice.

\* claude got this wrong. `get_tasks_by_priority()` doesn't take specific 
strings, neither does the Task class. I braught it up and now I'm fixing
them so that they only accept 3 priorities.