"""Конфігурація застосунку.

Значення беремо зі **змінних середовища** (підхід 12-factor), а не хардкодимо в коді.
Демонструє `@dataclass` та `@classmethod` як альтернативний конструктор.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Незмінний (frozen) набір налаштувань застосунку."""

    app_name: str
    debug: bool
    database_url: str

    @classmethod
    def from_env(cls) -> "Settings":
        """Створити налаштування зі змінних середовища (з розумними значеннями за замовчуванням)."""
        return cls(
            app_name=os.getenv("APP_NAME", "taskapp"),
            debug=os.getenv("DEBUG", "false").lower() == "true",
            database_url=os.getenv("DATABASE_URL", "memory://"),
        )


# Єдиний екземпляр налаштувань на весь застосунок.
settings = Settings.from_env()
