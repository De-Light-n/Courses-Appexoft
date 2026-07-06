# ⬇️ Програми для розробки — посилання на завантаження

Усе необхідне для Python-розробки та роботи з базами даних.
Завантажуйте **тільки з офіційних сайтів** — так безпечно й без вірусів.

> 🪟 **Windows** • 🍎 **macOS** • 🐧 **Linux** — для кожної програми обирайте
> свою систему. На Windows під час установки шукайте галочку **«Add to PATH»**.

---

## 🧰 Обов'язковий мінімум

| Програма | Для чого | Завантажити |
|---|---|---|
| **Visual Studio Code** | Головний редактор коду | <https://code.visualstudio.com/Download> |
| **Python** | Мова програмування (беріть 3.12+) | <https://www.python.org/downloads/> |
| **Git** | Контроль версій, робота з GitHub | <https://git-scm.com/downloads> |
| **DBeaver Community** | GUI для баз даних (SQL) | <https://dbeaver.io/download/> |

---

## 🐍 Python

- **Офіційний інсталятор:** <https://www.python.org/downloads/>
  - 🪟 Windows: під час установки **обов'язково** постав галочку
    **☑ Add python.exe to PATH**, далі *Install Now*.
  - 🍎 macOS: завантаж `.pkg` або встанови через Homebrew: `brew install python`
  - 🐧 Linux: зазвичай уже є; інакше `sudo apt install python3 python3-pip python3-venv`
- **Перевірка після установки** (у терміналі / PowerShell):
  ```bash
  python --version      # або python3 --version
  pip --version
  ```

### ⚡ uv — швидкий менеджер пакетів/віртуальних середовищ (рекомендую)
Сучасна заміна `pip` + `venv`, дуже швидка. У курсі трапляється `uv.lock`.
- Сайт і встановлення: <https://docs.astral.sh/uv/getting-started/installation/>
  ```bash
  # macOS / Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
  ```powershell
  # Windows (PowerShell)
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

---

## 🧩 Visual Studio Code

- **Завантажити:** <https://code.visualstudio.com/Download>
- Після установки — постав розширення для Python/Jupyter/AI однією командою:
  див. **[vscode-setup.md](vscode-setup.md)** у цьому ж репозиторії.
- 🍎 macOS порада: відкрий VS Code → `Cmd+Shift+P` →
  **Shell Command: Install 'code' command in PATH**, щоб команда `code` працювала в терміналі.

---

## 🌿 Git + GitHub

- **Git:** <https://git-scm.com/downloads>
- **GitHub Desktop** (GUI, якщо не любиш термінал): <https://desktop.github.com/>
- **Перевірка та базове налаштування:**
  ```bash
  git --version
  git config --global user.name "Ім'я Прізвище"
  git config --global user.email "your@email.com"
  ```
- Для push на GitHub потрібен **Personal Access Token** або **SSH-ключ**
  (пароль GitHub більше не приймає) — токени тут:
  <https://github.com/settings/tokens>

---

## 🗄️ Бази даних

| Програма | Для чого | Завантажити |
|---|---|---|
| **DBeaver Community** | Універсальний GUI-клієнт (Postgres, MySQL, SQLite…) | <https://dbeaver.io/download/> |
| **PostgreSQL** | Найпопулярніша БД для бекенду | <https://www.postgresql.org/download/> |
| **pgAdmin** | Офіційний GUI саме для PostgreSQL | <https://www.pgadmin.org/download/> |
| **MySQL Community** | Альтернативна популярна БД | <https://dev.mysql.com/downloads/mysql/> |
| **SQLite** | Легка файлова БД (часто вбудована) | <https://www.sqlite.org/download.html> |

> 💡 Найпростіший старт: постав **DBeaver** — він підключається до будь-якої БД.
> А саму PostgreSQL зручно піднімати через **Docker** (див. нижче), не встановлюючи локально.

---

## 🐳 Docker (контейнери)

- **Docker Desktop:** <https://www.docker.com/products/docker-desktop/>
  - 🪟 Windows потребує **WSL 2**: <https://learn.microsoft.com/windows/wsl/install>
- Перевірка: `docker --version` та `docker compose version`
- Приклад: підняти PostgreSQL однією командою —
  ```bash
  docker run --name pg -e POSTGRES_PASSWORD=secret -p 5432:5432 -d postgres
  ```

---

## 🌐 Веб-розробка (за потреби)

| Програма | Для чого | Завантажити |
|---|---|---|
| **Node.js (LTS)** | JavaScript-рантайм, npm | <https://nodejs.org/en/download> |
| **Google Chrome** | Браузер + DevTools | <https://www.google.com/chrome/> |
| **Postman** | Тестування API | <https://www.postman.com/downloads/> |

---

## 🧪 Перевірка, що все встановилось

Виконай у терміналі (macOS/Linux) або PowerShell (Windows):

```bash
python --version      # або python3 --version
pip --version
git --version
code --version
docker --version
uv --version
```

Якщо якась команда пише *"not found"* / *"не знайдено"* — програма не встановлена
або не додана в **PATH** (перевстанови з галочкою *Add to PATH*).

---

## 💡 Поради

- **Windows:** майже скрізь під час установки шукай галочку **Add to PATH** —
  без неї команди не працюватимуть у терміналі.
- **macOS:** зручно ставити все через [Homebrew](https://brew.sh/):
  ```bash
  brew install python git node
  brew install --cask visual-studio-code dbeaver-community docker
  ```
- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt update && sudo apt install -y python3 python3-pip python3-venv git
  ```
- Став **тільки те, що потрібно зараз** — Docker, Node.js та інше можна додати пізніше.
- Для звичайних ноутбуків із курсу достатньо: **VS Code + Python + Git**.
