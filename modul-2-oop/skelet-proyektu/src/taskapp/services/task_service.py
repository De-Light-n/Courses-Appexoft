"""Сервісний шар — бізнес-логіка.

`TaskService` **не знає**, як саме зберігаються дані — він працює через абстрактний репозиторій.
Це **розділення відповідальностей**: домен описує «що», репозиторій — «де зберігати»,
сервіс — «що з цим робити». Репозиторій передається ззовні (**впровадження залежностей**),
що відповідає принципу інверсії залежностей (буква D у SOLID).
"""

from __future__ import annotations

from taskapp.domain.models import Task
from taskapp.exceptions import TaskNotFoundError
from taskapp.repositories.base import AbstractTaskRepository


class TaskService:
    """Операції над завданнями (створити, виконати, отримати список)."""

    def __init__(self, repository: AbstractTaskRepository) -> None:
        # Залежимо від АБСТРАКЦІЇ (інтерфейсу), а не від конкретного сховища.
        self._repo = repository

    def create_task(self, title: str) -> Task:
        task = Task(title=title)          # валідація назви — усередині моделі
        return self._repo.add(task)

    def complete_task(self, task_id: int) -> Task:
        task = self._repo.get(task_id)
        if task is None:
            raise TaskNotFoundError(f"Завдання {task_id} не знайдено")
        task.mark_done()
        return task

    def all_tasks(self) -> list[Task]:
        return self._repo.list()

    def delete_task(self, task_id: int) -> None:
        task = self._repo.get(task_id)
        if task is None:
            raise TaskNotFoundError(f"Завдання {task_id} не знайдено")
        self._repo.delete(task_id)