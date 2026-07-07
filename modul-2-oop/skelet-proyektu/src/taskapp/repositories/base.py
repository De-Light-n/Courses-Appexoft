"""Абстракція репозиторію (патерн Repository).

Це **інтерфейс** (контракт) сховища. Сервіси залежать саме від нього, а не від конкретної
бази даних — тому реалізацію легко замінити (пам'ять → PostgreSQL) без зміни бізнес-логіки.
Демонструє **абстракцію** через модуль `abc`.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from taskapp.domain.models import Task


class AbstractTaskRepository(ABC):
    """Контракт сховища завдань. Будь-яка реалізація мусить надати ці методи."""

    @abstractmethod
    def add(self, task: Task) -> Task:
        """Зберегти завдання та повернути його (з призначеним id)."""
        raise NotImplementedError

    @abstractmethod
    def get(self, task_id: int) -> Task | None:
        """Повернути завдання за id або None, якщо не знайдено."""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Task]:
        """Повернути всі завдання."""
        raise NotImplementedError
