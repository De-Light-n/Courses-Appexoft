"""Доменні моделі (сутності).

`Task` демонструє **інкапсуляцію** та **`@property`**: назву не можна зробити порожньою —
валідація живе всередині об'єкта, а не розкидана по всьому коду.
"""

from __future__ import annotations


class Task:
    """Завдання у списку справ."""

    def __init__(self, title: str, id: int | None = None, done: bool = False) -> None:
        self.id = id            # призначає репозиторій при збереженні
        self._title = ""        # "приховане" поле (домовленість: _ = внутрішнє)
        self.title = title      # присвоєння пройде через сеттер із валідацією
        self.done = done

    @property
    def title(self) -> str:
        """Назва завдання (тільки для читання ззовні через геттер)."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        value = value.strip()
        if not value:
            raise ValueError("Назва завдання не може бути порожньою")
        self._title = value

    def mark_done(self) -> None:
        """Позначити завдання виконаним."""
        self.done = True

    def __repr__(self) -> str:
        status = "✓" if self.done else " "
        return f"Task(id={self.id}, [{status}] {self.title!r})"
