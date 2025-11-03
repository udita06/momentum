import pytest
from src.components.todo import add_task, remove_task, get_tasks

def test_add_task():
    initial_tasks = get_tasks()
    add_task("Test Task 1")
    tasks_after_addition = get_tasks()
    assert len(tasks_after_addition) == len(initial_tasks) + 1
    assert "Test Task 1" in tasks_after_addition

def test_remove_task():
    add_task("Test Task 2")
    initial_tasks = get_tasks()
    remove_task("Test Task 2")
    tasks_after_removal = get_tasks()
    assert len(tasks_after_removal) == len(initial_tasks)
    assert "Test Task 2" not in tasks_after_removal

def test_get_tasks():
    add_task("Test Task 3")
    tasks = get_tasks()
    assert "Test Task 3" in tasks
    assert isinstance(tasks, list)  # Ensure it returns a list