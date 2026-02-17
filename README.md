# Todo Console App - Phase 2: Foundation ✅

**Hackathon Project - Phase 2**
**Status**: Foundation Complete
**Date**: February 17, 2026

---

## Phase 2 Overview

Phase 2 establishes the **core infrastructure** that all user stories depend on. This phase implements foundational data models, storage layer, and exception handling using **Test-Driven Development (TDD)**.

**Completed**: 7/7 tasks (T009-T015)
**Tests**: 34 passing (19 Task model + 15 TaskRepository)
**Coverage**: 100% on foundation components

---

## What's Implemented

### 1. Exception Classes (`src/models/exceptions.py`)
- `TodoError` - Base exception for the application
- `TaskNotFoundError` - Raised when task ID doesn't exist
- `ValidationError` - Raised when input validation fails

### 2. Task Model (`src/models/task.py`)
**Dataclass with validation**:
- `title` - Required, 1-200 characters
- `description` - Optional, max 1000 characters
- `completed` - Boolean status (default: False)
- `id` - Auto-assigned by repository
- `created_at` - Timestamp

**Methods**:
- `toggle_completion()` - Toggle task status
- `update_title(new_title)` - Update title with validation
- `update_description(new_description)` - Update description with validation

### 3. TaskRepository (`src/services/task_repository.py`)
**In-memory storage with dictionary**:
- `add(task)` - Add task and assign unique ID
- `get(task_id)` - Retrieve task by ID
- `get_all()` - Get all tasks
- `update(task_id, title?, description?)` - Update task
- `delete(task_id)` - Remove task
- `exists(task_id)` - Check if task exists

---

## Quick Start

### Prerequisites
- Python 3.13+
- UV package manager

### Setup
```bash
# Navigate to project
cd hackathon2shzaib

# Activate virtual environment (if not already active)
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### Run Phase 2 Tests
```bash
# Run all Phase 2 tests
uv run pytest tests/unit/test_task_model.py tests/unit/test_task_repository.py -v

# Run with coverage
uv run pytest tests/unit/ --cov=src/models --cov=src/services --cov-report=term-missing

# Run specific test file
uv run pytest tests/unit/test_task_model.py -v
uv run pytest tests/unit/test_task_repository.py -v
```

### Expected Output
```
============================= test session starts =============================
collected 34 items

tests/unit/test_task_model.py ..................... [19 passed]
tests/unit/test_task_repository.py ............... [15 passed]

============================== 34 passed in 1.38s ==============================

Coverage Report:
Name                              Stmts   Miss  Cover
-------------------------------------------------------
src/models/exceptions.py              8      0   100%
src/models/task.py                   39      0   100%
src/services/task_repository.py      31      0   100%
-------------------------------------------------------
TOTAL                                78      0   100%
```

---

## Code Quality Checks

### Type Checking
```bash
uv run mypy src/models/ src/services/
# Expected: Success: no issues found
```

### Linting
```bash
uv run ruff check src/models/ src/services/
# Expected: All checks passed!
```

### Formatting
```bash
uv run ruff format --check src/models/ src/services/
# Expected: All files formatted correctly
```

---

## Project Structure

```
hackathon2shzaib/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── exceptions.py       ✅ Phase 2
│   │   └── task.py             ✅ Phase 2
│   └── services/
│       ├── __init__.py
│       └── task_repository.py  ✅ Phase 2
├── tests/
│   ├── unit/
│   │   ├── test_task_model.py          ✅ Phase 2 (19 tests)
│   │   └── test_task_repository.py     ✅ Phase 2 (15 tests)
│   └── conftest.py
├── pyproject.toml
├── .python-version
└── README.md (this file)
```

---

## Test Coverage Details

### Task Model Tests (19 tests)
- ✅ Task creation with title only
- ✅ Task creation with title and description
- ✅ Empty title validation
- ✅ Title too long validation (>200 chars)
- ✅ Description too long validation (>1000 chars)
- ✅ Whitespace stripping
- ✅ Completion toggling
- ✅ Title updates with validation
- ✅ Description updates with validation

### TaskRepository Tests (15 tests)
- ✅ Adding tasks with ID assignment
- ✅ Sequential ID generation
- ✅ Getting existing tasks
- ✅ TaskNotFoundError for invalid IDs
- ✅ Getting all tasks (empty/populated)
- ✅ Updating task title/description
- ✅ Deleting tasks
- ✅ Checking task existence

---

## Usage Examples

### Create and Validate Tasks
```python
from src.models.task import Task
from src.models.exceptions import ValidationError

# Valid task
task = Task(title="Buy groceries", description="Milk, eggs, bread")
print(f"Task: {task.title}")  # Output: Task: Buy groceries

# Invalid task (empty title)
try:
    task = Task(title="")
except ValidationError as e:
    print(f"Error: {e}")  # Output: Error: Title is required and must be 1-200 characters
```

### Use TaskRepository
```python
from src.models.task import Task
from src.services.task_repository import TaskRepository

# Create repository
repo = TaskRepository()

# Add tasks
task1 = Task(title="Buy groceries")
task2 = Task(title="Call mom")

added1 = repo.add(task1)
added2 = repo.add(task2)

print(f"Task 1 ID: {added1.id}")  # Output: Task 1 ID: 1
print(f"Task 2 ID: {added2.id}")  # Output: Task 2 ID: 2

# Get all tasks
all_tasks = repo.get_all()
print(f"Total tasks: {len(all_tasks)}")  # Output: Total tasks: 2

# Update task
updated = repo.update(1, title="Buy groceries and fruits")
print(f"Updated: {updated.title}")  # Output: Updated: Buy groceries and fruits

# Delete task
repo.delete(2)
print(f"Remaining: {len(repo.get_all())}")  # Output: Remaining: 1
```

---

## TDD Approach

Phase 2 followed strict **Test-Driven Development**:

1. **RED Phase**: Write failing tests first
   - Wrote 19 tests for Task model
   - Wrote 15 tests for TaskRepository
   - All tests failed initially (no implementation)

2. **GREEN Phase**: Implement minimal code to pass tests
   - Implemented Task dataclass with validation
   - Implemented TaskRepository with in-memory storage
   - All 34 tests passing

3. **REFACTOR Phase**: Improve code while keeping tests green
   - Added comprehensive docstrings
   - Added type hints everywhere
   - Improved error messages

---

## What's Next

### Phase 3: User Story 1 - Create and View Tasks (MVP)

**Goal**: Users can add tasks and view their task list

**Components to implement**:
- TaskService (business logic layer)
- CLI commands (add, list)
- Output formatter
- Main entry point with argparse
- Integration tests

**Deliverable**: Working MVP where users can create and view tasks via command line

---

## Verification Checklist

Before moving to Phase 3, verify:

- [ ] All 34 tests passing
- [ ] 100% coverage on foundation components
- [ ] Mypy type checking passes
- [ ] Ruff linting passes
- [ ] No TODO comments in code
- [ ] All docstrings present
- [ ] Exception handling works correctly

### Run Full Verification
```bash
# Run all checks
uv run pytest tests/unit/ -v && \
uv run mypy src/models/ src/services/ && \
uv run ruff check src/models/ src/services/

# If all pass, Phase 2 is complete ✅
```

---

## Constitutional Compliance

✅ **Spec-Driven Development** - Following SDD workflow
✅ **Python Excellence** - Type hints, docstrings, PEP 8
✅ **Test-First Development** - TDD strictly followed
✅ **Simplicity and Focus** - Minimal implementation
✅ **Clean Architecture** - Clear separation of concerns

---

## Troubleshooting

### Tests Failing
```bash
# Run with verbose output
uv run pytest tests/unit/ -vv

# Run specific test
uv run pytest tests/unit/test_task_model.py::TestTaskCreation::test_create_task_with_title_only -v
```

### Coverage Below 100%
```bash
# Check which lines are missing
uv run pytest tests/unit/ --cov=src/models --cov=src/services --cov-report=html

# Open htmlcov/index.html to see uncovered lines
```

### Type Errors
```bash
# Run mypy with verbose output
uv run mypy src/models/ src/services/ --show-error-codes
```

---

## Resources

- **Specification**: `specs/001-todo-console-app/spec.md`
- **Implementation Plan**: `specs/001-todo-console-app/plan.md`
- **Data Model**: `specs/001-todo-console-app/data-model.md`
- **Tasks**: `specs/001-todo-console-app/tasks.md`

---

**Phase 2 Status**: ✅ Complete
**Foundation Ready**: ✅ Yes
**Next Phase**: Phase 3 - User Story 1 (MVP)
**Ready to Push**: ✅ Yes
