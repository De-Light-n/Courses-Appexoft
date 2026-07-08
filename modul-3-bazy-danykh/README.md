# 🗄️ Модуль 3 — Бази даних та SQL

Навчимося зберігати дані «по-дорослому» — у **базах даних**. Спершу опануємо мову **SQL**
на практиці, а потім — як працювати з БД із Python (psycopg2, SQLAlchemy, alembic).

## 📓 Матеріали
- **Урок 1:** [Основи SQL (реляційні БД, таблиці, запити, JOIN, транзакції, ін'єкції)](lektsiya-1-sql-osnovy.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-1.ipynb)
- **Урок 2:** [Бази даних із Python (ACID, індекси, EXPLAIN, psycopg2, SQLAlchemy, CRUD, alembic)](lektsiya-2-bd-z-python-sqlalchemy.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-2.ipynb)

## Програма модуля

### Урок 1 — SQL та реляційні бази даних
- Реляційні та нереляційні БД
- Структура БД (таблиці, рядки, стовпці) і типи даних
- Обмеження (constraints)
- Зв'язки між таблицями (primary key, foreign key); one-to-one / one-to-many / many-to-many
- Нормалізація та денормалізація
- DDL: `CREATE`, `ALTER`, `DROP` (+ `CASCADE`)
- DML: `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`
- `JOIN` (inner, left, right, full, cross)
- Агрегація (`COUNT`, `SUM`, `MIN`, `MAX`, `AVG`)
- Функції та процедури, `VIEW`
- Транзакції
- 🔎 SQL-ін'єкції та захист від них

### Урок 2 — Бази даних із Python
- ACID
- Індекси; `EXPLAIN` / `EXPLAIN ANALYZE`; оптимізація запитів
- Підключення до БД із Python: `psycopg2` (без ORM)
- SQLAlchemy; реалізація CRUD
- Міграції з `alembic`
- Порівняння SQLite, MySQL, PostgreSQL

## 🛠 Як ми запускаємо SQL

В **Уроці 1** ми пишемо **справжній SQL** прямо в зошиті через вбудований у Python модуль
**`sqlite3`** — жодного встановлення не потрібно, кожен запит одразу виконується й показує результат.
Той самий SQL працює й у PostgreSQL/MySQL — відмінності діалектів позначені в тексті.

В **Уроці 2** підключатимемось до **PostgreSQL** через `psycopg2` та **SQLAlchemy**.
Для зручного перегляду БД корисний GUI **DBeaver** (див. [zavantazhennya-program.md](../zavantazhennya-program.md)).
