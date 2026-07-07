"""Точка входу застосунку (composition root).

Саме тут ми «збираємо» залежності разом: створюємо конкретний репозиторій і передаємо
його в сервіс. Решта коду не знає, яке саме сховище використовується.

Запуск:  PYTHONPATH=src python -m taskapp.main
"""

from __future__ import annotations

from taskapp.config import settings
from taskapp.repositories.in_memory import InMemoryTaskRepository
from taskapp.services.task_service import TaskService


def main() -> None:
    print(f"Запуск {settings.app_name} (debug={settings.debug}, db={settings.database_url})")

    # Впровадження залежності: обираємо реалізацію сховища тут, в одному місці.
    repo = InMemoryTaskRepository()
    service = TaskService(repo)

    service.create_task("Написати README")
    service.create_task("Налаштувати лінтер")
    interview = service.create_task("Підготуватися до співбесіди")

    service.complete_task(interview.id)

    print("Усі завдання:")
    for task in service.all_tasks():
        print("  ", task)


if __name__ == "__main__":
    main()
