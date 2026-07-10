# 🐍 Модуль 1 — Вступ до Python та основи

Перший модуль курсу: від `print("Привіт")` до функцій, декораторів і генераторів. Тут
закладається фундамент, на якому стоятимуть усі наступні модулі (ООП, бази даних, DRF).

## 📓 Матеріали
- **Урок 1:** [Синтаксис, змінні, типи, оператори](lektsiya-1-syntaksys-zminni-typy-danych-operatory.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-1.ipynb)
- **Урок 2:** [Умовні оператори та цикли](lektsiya-2-umovni-operatory-ta-tsykly.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-2.ipynb)
- **Урок 3:** [Рядки та колекції](lektsiya-3-ryadky-ta-kolektsiyi.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-3.ipynb)
- **Урок 4:** [Функції, замикання, декоратори, генератори](lektsiya-4-funktsiyi-oblast-vydymosti-legb.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-4.ipynb)
- **🎁 Бонус:** [Багатозадачність: `threading`, `multiprocessing`, `asyncio`](bonus-asyncio-threading-multiprocessing.ipynb) `🚀 Middle+`

## Програма модуля

### Урок 1 — Синтаксис, змінні, типи, оператори
- Що таке Python; як виконується код (🔎 CPython, байткод, PVM, GIL — оглядово)
- `print()`, змінні, коментарі
- Типи даних: `int`, `float`, `str`, `bool`, `None`
- Оператори (арифметичні, порівняння, логічні), перетворення типів
- `input()`, `is` проти `==`
- 🔎 Керування пам'яттю (reference counting + garbage collector)

### Урок 2 — Умовні оператори та цикли
- `if / elif / else`, тернарний оператор
- Цикли `for` та `while`, `range`
- `break`, `continue`, `for/else`
- `enumerate`, `zip`

### Урок 3 — Рядки та колекції
- Рядки: зрізи, методи, f-strings
- `list`, `tuple`, `set`, `dict`
- 🔎 Як влаштовані `list`/`dict`/`set` усередині (динамічний масив, хеш-таблиця)
- 🔎 Big-O та шпаргалка складності операцій
- List comprehension, глибока копія

### Урок 4 — Функції, замикання, декоратори, генератори
- Функції, аргументи (позиційні/іменовані/`*args`/`**kwargs`)
- 🔎 Область видимості (LEGB), замикання
- Декоратори (зокрема з параметрами)
- `try / except / finally`
- Генератори та ітератори, `with` (менеджери контексту)
- 🔎 GIL

### 🎁 Бонус — Багатозадачність (Middle+)
- Concurrency проти parallelism, роль GIL
- `threading` (Lock, Semaphore, Queue, ThreadPoolExecutor)
- `multiprocessing` (оглядово)
- `asyncio` (event loop, `await`, `create_task`, `gather`)

## 🛠 Як ми працюємо
Кожен зошит можна запускати комірку за коміркою (`Shift + Enter`) і експериментувати. Домашки
здаються через Pull Request (гілка `<нік>/hw-m1-l<урок>`, див. [CONTRIBUTING.md](../CONTRIBUTING.md)).
