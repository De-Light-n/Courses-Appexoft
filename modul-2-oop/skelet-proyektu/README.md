# 📦 taskapp — скелет Python-проєкту

Навчальний приклад **продакшн-подібної** структури проєкту на чистому Python (без зовнішніх
залежностей). Показує, як розкладати код по шарах і застосовувати патерн **Repository** та
**сервісний шар**.

## 🗂 Структура

```
skelet-proyektu/
├── pyproject.toml          # метадані проєкту + конфіг лінтера (ruff) і pytest
├── .env.example            # приклад змінних середовища (скопіювати у .env)
├── .gitignore
├── src/
│   └── taskapp/
│       ├── config.py       # конфігурація з env (12-factor)
│       ├── exceptions.py   # власні винятки застосунку
│       ├── domain/         # 🟢 ШАР ДОМЕНУ: бізнес-сутності (не знають про БД/фреймворки)
│       │   └── models.py   #    Task — інкапсуляція + @property
│       ├── repositories/   # 🔵 ШАР ДОСТУПУ ДО ДАНИХ (Repository pattern)
│       │   ├── base.py     #    AbstractTaskRepository — абстракція (інтерфейс)
│       │   └── in_memory.py#    InMemoryTaskRepository — конкретна реалізація
│       ├── services/       # 🟣 СЕРВІСНИЙ ШАР: бізнес-логіка
│       │   └── task_service.py
│       └── main.py         # точка входу (composition root)
└── tests/
    └── test_task_service.py
```

## 🧠 Які теми модуля тут видно

| Тема | Де у коді |
|---|---|
| Класи та об'єкти | `domain/models.py`, усі шари |
| Інкапсуляція, `@property` | `domain/models.py` (`Task.title`) |
| Абстракція, `abc` | `repositories/base.py` |
| Наслідування / поліморфізм | `InMemoryTaskRepository(AbstractTaskRepository)` |
| `@classmethod` | `config.py` (`Settings.from_env`) |
| Патерн Repository | `repositories/` |
| Сервісний шар | `services/task_service.py` |
| Розділення відповідальностей | розбиття на `domain` / `repositories` / `services` |
| Змінні середовища | `config.py` + `.env.example` |
| Лінтер | секція `[tool.ruff]` у `pyproject.toml` |

## ▶️ Як запустити

```bash
# з теки skelet-proyektu/
PYTHONPATH=src python -m taskapp.main
```

Очікуваний вивід — створення кількох завдань і позначення одного виконаним.

## ✅ Як запустити тести

```bash
# варіант 1 — без сторонніх бібліотек:
PYTHONPATH=src python tests/test_task_service.py

# варіант 2 — через pytest (спершу: pip install pytest):
pytest
```

## 🧹 Лінтер (перевірка стилю коду)

```bash
pip install ruff
ruff check .        # знайти проблеми
ruff format .       # відформатувати код
```

## 🔑 Змінні середовища

```bash
cp .env.example .env   # і за потреби відредагувати значення
```
Код читає їх у `config.py`. **Секрети (паролі, ключі) ніколи не комітять** — тому `.env` у `.gitignore`.
