import pytest
from task_store import TaskStore


def test_add_task_invalid_id():
    store = TaskStore()

    with pytest.raises(ValueError):
        store.add_task("abc", "Task 1")


def test_add_task_invalid_name_type():
    store = TaskStore()

    with pytest.raises(ValueError):
        store.add_task(1, None)


def test_add_task_empty_name():
    store = TaskStore()

    with pytest.raises(ValueError):
        store.add_task(1, "")


def test_get_task_invalid_id():
    store = TaskStore()

    with pytest.raises(ValueError):
        store.get_task("abc")


def test_mark_done_invalid_id():
    store = TaskStore()

    with pytest.raises(ValueError):
        store.mark_done("abc")
