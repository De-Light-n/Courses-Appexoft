# 🔧 Модуль 4 — Git та якість коду

Інструменти, без яких не обходиться жоден розробник: **Git** (контроль версій) і культура
**якості коду** (стиль, типи, документація, лінтери, автоперевірки).

## 📓 Матеріали
- **Урок 1:** [Git та системи контролю версій (гілки, merge/rebase, stash, cherry-pick, Gitflow)](lektsiya-1-git.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-1.ipynb)
- **Урок 2:** [Якість коду (PEP 8, DRY/KISS/YAGNI, type hints, docstrings, ruff/black/isort/mypy/flake8, pre-commit)](lektsiya-2-yakist-koda.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-2.ipynb)

## Програма модуля

### Урок 1 — Git
- Що таке Git і навіщо; Git проти GitHub
- Три зони (working dir / staging / repository) і коміти
- Основні команди (і які ще можуть спитати)
- Гілки як граф; `merge` проти `rebase` (з діаграмами)
- 🔎 `git stash`, 🔎 `git cherry-pick`
- 🔎 Gitflow та інші workflow (GitHub Flow, trunk-based)
- `reset` / `revert` / `restore`, `fetch` / `pull`, конфлікти, `reflog`

### Урок 2 — Якість коду
- Навіщо якість коду
- 🔎 PEP 8 (стиль, іменування)
- 🔎 DRY / KISS / YAGNI
- 🔎 Type hints (typing, `str | None`, mypy)
- 🔎 Docstrings (PEP 257, Google-стиль)
- 🔧 Інструменти: flake8, black, isort, mypy, ruff
- 🔎 pre-commit hooks

## 🛠 Як ми працюємо
Git вивчаємо **в терміналі** (див. [vstanovlennya-git.md](../vstanovlennya-git.md)); інструменти
якості ставляться через `pip` (`ruff`, `mypy`, `pre-commit`). Робочий процес зі здачі домашок
через Pull Request описано в [CONTRIBUTING.md](../CONTRIBUTING.md).
