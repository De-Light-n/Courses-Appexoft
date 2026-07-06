# 🌿 Встановлення та налаштування Git

Методичка: як встановити Git на Windows / macOS / Linux, налаштувати його
та підключити до GitHub.

---

## 🪟 Windows

1. **Завантаж інсталятор:** <https://git-scm.com/downloads> → обери **Windows**
   (завантаження почнеться автоматично).
2. **Запусти** файл `Git-x.xx.x-64-bit.exe` і на екрані ліцензії тисни **Next**.
3. **Папка встановлення** — залиш за замовчуванням (`C:\Program Files\Git`) → **Next**.
4. **Компоненти** — залиш галочки за замовчуванням → **Next**.
5. **Редактор за замовчуванням** — обери **Use Visual Studio Code as Git's default editor** → **Next**.
6. **Назва початкової гілки** — обери **Override the default branch name for new repositories**
   і впиши **`main`** → **Next**.
7. **PATH** — обери рекомендований (середній) варіант
   **Git from the command line and also from 3rd-party software** → **Next**.
8. **Решта екранів** (HTTPS, line endings, terminal, credential manager тощо) —
   залишай **значення за замовчуванням** і тисни **Next**, у кінці — **Install**.
9. Після установки натисни **Finish**.

---

## 🍎 macOS

### Спосіб 1. Через Homebrew (рекомендовано)

```bash
brew install git
```

**А якщо Homebrew немає?** Перевір:
```bash
brew --version
```
Якщо `command not found` — постав Homebrew однією командою (з <https://brew.sh/>):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
- Термінал попросить **пароль від Mac** (символи під час вводу не видно — це нормально).
- Якщо немає **Xcode Command Line Tools**, Homebrew поставить їх сам.

Після установки додай `brew` у PATH:
```bash
# Apple Silicon (M1/M2/M3)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```
На Intel-Mac шлях — `/usr/local/bin/brew` (зазвичай уже в PATH).
Потім: `brew install git`.

### Спосіб 2. Без Homebrew

- **Офіційний інсталятор:** <https://git-scm.com/downloads> → **macOS** → встанови `.dmg`.
- **Або Xcode Command Line Tools** (Git іде в комплекті):
  ```bash
  xcode-select --install
  ```

---

## 🐧 Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install -y git
```

---

## ✅ Перевірка, що Git встановлено

Відкрий термінал (Windows: **Git Bash** або PowerShell) і виконай:
```bash
git --version
```
Якщо бачиш `git version 2.xx.x` — усе працює.

---

## 🔧 Первинне налаштування (робиться один раз)

Ці налаштування підписують твої коміти. Email має **збігатися** з email в акаунті GitHub.

```bash
git config --global user.name "Ваше Імʼя"
git config --global user.email "your@email.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
```

**Перевірити всі налаштування:**
```bash
git config --global --list
```
Маєш побачити рядки `user.name=…`, `user.email=…`, `init.defaultBranch=main`.

---

## 🔗 Підключення до GitHub

GitHub **не приймає пароль** — потрібен **Personal Access Token** або **SSH-ключ**.

### Варіант А — Personal Access Token (простіше)

1. Відкрий <https://github.com/settings/tokens> → **Generate new token (classic)**.
2. Признач scope **`repo`**, згенеруй і **скопіюй** токен (`ghp_…`).
3. При першому `git push` введи:
   - **Username** — твій логін GitHub;
   - **Password** — встав **токен** (не пароль!).

Токен збережеться, і далі push працюватиме без запитів.

### Варіант Б — SSH-ключ (надійніше на майбутнє)

```bash
# 1) згенерувати ключ (Enter на всі питання)
ssh-keygen -t ed25519 -C "your@email.com"

# 2) показати публічний ключ і скопіювати вивід
cat ~/.ssh/id_ed25519.pub
```
Потім: GitHub → **Settings → SSH and GPG keys → New SSH key** → встав ключ.

---

## 🧪 Перевірка — перший репозиторій

```bash
mkdir test-git && cd test-git
git init
echo "# Тест" > README.md
git add .
git commit -m "Перший коміт"
git log --oneline
```
Якщо в `git log --oneline` видно твій коміт — усе налаштовано правильно.

---

## 🆘 Якщо щось пішло не так

| Проблема | Рішення |
|---|---|
| `git: command not found` | Git не в PATH — перевстанови з опцією *Git from the command line…* |
| `Authentication failed` при push | Використовуй **токен**, а не пароль; або перейди на SSH |
| Коміти з чужим іменем | Перевір `git config --global user.name` / `user.email` |
| Просить логін щоразу | Введи токен один раз — credential manager його запам'ятає |

---

## 📋 Шпаргалка (команди налаштування)

```bash
git config --global user.name "Ваше Імʼя"
git config --global user.email "your@email.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --global --list      # перевірка
```
