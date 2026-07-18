"""Конкретна реалізація репозиторію — зберігання у пам'яті.

Зручно для прикладів і тестів. У реальному проєкті тут була б робота з БД (SQL/ORM),
але **інтерфейс лишився б тим самим** — у цьому й сила патерну Repository.
Демонструє **наслідування** та **поліморфізм** (реалізує AbstractTaskRepository).
"""

from __future__ import annotations

from taskapp.domain.models import Task
from taskapp.repositories.base import AbstractTaskRepository


class InMemoryTaskRepository(AbstractTaskRepository):
    """Сховище завдань у звичайному словнику (id -> Task)."""

    def __init__(self) -> None:
        self._items: dict[int, Task] = {}
        self._next_id = 1

    def add(self, task: Task) -> Task:
        if task.id is None:
            task.id = self._next_id
        self._items[task.id] = task
        self._next_id = max(self._next_id, task.id + 1)
        return task

    def get(self, task_id: int) -> Task | None:
        return self._items.get(task_id)

    def list(self) -> list[Task]:
        return list(self._items.values())

    def delete(self, task_id: int) -> None:
        if task_id in self._items:
            del self._items[task_id]