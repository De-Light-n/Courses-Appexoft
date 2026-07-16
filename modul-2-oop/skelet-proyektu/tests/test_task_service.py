"""Юніт-тести сервісного шару.

Завдяки патерну Repository тести **швидкі й ізольовані**: підставляємо InMemory-сховище,
жодної реальної БД не потрібно. Так тестують сервіси у продакшн-проєктах.
"""

from taskapp.exceptions import TaskNotFoundError
from taskapp.repositories.in_memory import InMemoryTaskRepository
from taskapp.services.task_service import TaskService


def make_service() -> TaskService:
    return TaskService(InMemoryTaskRepository())


def test_create_task_assigns_id():
    service = make_service()
    task = service.create_task("Тест")
    assert task.id == 1
    assert task.title == "Тест"
    assert task.done is False


def test_titles_are_validated():
    service = make_service()
    try:
        service.create_task("   ")   # порожня назва (лише пробіли)
        raise AssertionError("мало б кинути ValueError")
    except ValueError:
        pass


def test_complete_task():
    service = make_service()
    task = service.create_task("Зробити")
    service.complete_task(task.id)
    assert task.done is True


def test_complete_missing_task_raises():
    service = make_service()
    try:
        service.complete_task(999)
        raise AssertionError("мало б кинути TaskNotFoundError")
    except TaskNotFoundError:
        pass


if __name__ == "__main__":
    # Дозволяє запустити тести без pytest: PYTHONPATH=src python tests/test_task_service.py
    test_create_task_assigns_id()
    test_titles_are_validated()
    test_complete_task()
    test_complete_missing_task_raises()
    print("Усі тести пройдено ✅")