# taskflow

Lightweight in-memory task tracking library, used internally by a few other
services on the Platform team. Simple by design — no DB, no framework —
so it's a good place for new engineers to get their feet wet.

## Structure

```
taskflow/
  __init__.py  # initialize this library
  models.py    # Task dataclass
  manager.py   # TaskManager: add/complete/query tasks
tests/
  test_manager.py
```

## Running tests

```
python3 -m pytest -v
```

## Status

CI is currently red. See TICKETS.md for the open ticket.
