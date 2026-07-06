# 🧩 Розширення VS Code для Python + AI + Web розробки

Готовий набір розширень і команди, щоб встановити їх усі однією дією.

> **Команда `code` не знайдена?** Нічого налаштовувати не треба — блоки нижче
> самі знаходять VS Code (навіть якщо він у `~/Downloads`, а не в PATH).
> Щоб `code` працювала завжди: відкрийте VS Code → `Cmd+Shift+P` →
> **Shell Command: Install 'code' command in PATH** (і перезапустіть термінал).

---

## 🎯 Встановити ОДНЕ розширення

```bash
# знаходимо VS Code автоматично (PATH → /Applications → ~/Applications → ~/Downloads)
code=$(command -v code \
  || echo /Applications/"Visual Studio Code.app"/Contents/Resources/app/bin/code)
[ -x "$code" ] || code=~/"Downloads/Visual Studio Code.app/Contents/Resources/app/bin/code"

# ↓ підставте потрібний ідентифікатор розширення
"$code" --install-extension ms-python.python --force
```

Ідентифікатор (`publisher.name`) видно на сторінці розширення в Marketplace
або в самому VS Code на вкладці розширення (внизу праворуч, кнопка ⚙ → *Copy Extension ID*).

---

## 🚀 Швидке встановлення (усе одразу)

### macOS / Linux (bash / zsh)

```bash
# 1) знаходимо бінарник code автоматично
code=$(command -v code \
  || echo /Applications/"Visual Studio Code.app"/Contents/Resources/app/bin/code)
[ -x "$code" ] || code=~/"Downloads/Visual Studio Code.app/Contents/Resources/app/bin/code"

# 2) список і встановлення
extensions=(
  # --- Python core ---
  ms-python.python                 # мова Python (базове)
  ms-python.vscode-pylance         # швидкий IntelliSense / типи
  ms-python.debugpy                # дебагер
  charliermarsh.ruff               # лінтер + форматер (швидкий, все-в-одному)
  ms-python.black-formatter        # форматер Black
  ms-python.mypy-type-checker      # статична перевірка типів
  KevinRose.vsc-python-indent      # розумні відступи
  njpwerner.autodocstring          # авто-докстрінги

  # --- Jupyter / Data / AI ---
  ms-toolsai.jupyter               # ноутбуки .ipynb
  ms-toolsai.jupyter-renderers     # рендер графіків/таблиць
  ms-toolsai.vscode-jupyter-cell-tags
  ms-toolsai.datawrangler          # перегляд/очистка даних

  # --- AI-асистенти ---
  anthropic.claude-code            # Claude Code
  github.copilot                   # Copilot
  github.copilot-chat              # Copilot Chat
  continue.continue                # Continue (локальні/будь-які моделі)

  # --- Web (front-end) ---
  esbenp.prettier-vscode           # форматер JS/TS/HTML/CSS
  dbaeumer.vscode-eslint           # лінтер JS/TS
  bradlc.vscode-tailwindcss        # Tailwind CSS
  dsznajder.es7-react-js-snippets  # React сніпети
  Vue.volar                        # Vue 3
  formulahendry.auto-rename-tag    # авто-перейменування тегів
  formulahendry.auto-close-tag     # авто-закриття тегів
  ritwickdey.LiveServer            # локальний сервер із live-reload

  # --- API / Backend ---
  humao.rest-client                # тестування HTTP прямо з .http файлів
  rangav.vscode-thunder-client     # Postman-подібний клієнт
  ms-azuretools.vscode-docker      # Docker
  redhat.vscode-yaml               # YAML
  ms-vscode-remote.remote-containers  # Dev Containers

  # --- Git ---
  eamodio.gitlens                  # історія/blame/аннотації
  mhutchie.git-graph               # граф комітів

  # --- Загальні / DX ---
  usernamehw.errorlens             # помилки прямо в рядку
  streetsidesoftware.code-spell-checker
  christian-kohler.path-intellisense  # автодоповнення шляхів
  editorconfig.editorconfig
  yzhang.markdown-all-in-one       # Markdown
  PKief.material-icon-theme        # іконки файлів
)

for ext in "${extensions[@]}"; do
  code --install-extension "$ext" --force
done
```

### Windows (PowerShell)

```powershell
$extensions = @(
  "ms-python.python","ms-python.vscode-pylance","ms-python.debugpy",
  "charliermarsh.ruff","ms-python.black-formatter","ms-python.mypy-type-checker",
  "KevinRose.vsc-python-indent","njpwerner.autodocstring",
  "ms-toolsai.jupyter","ms-toolsai.jupyter-renderers",
  "ms-toolsai.vscode-jupyter-cell-tags","ms-toolsai.datawrangler",
  "anthropic.claude-code","github.copilot","github.copilot-chat","continue.continue",
  "esbenp.prettier-vscode","dbaeumer.vscode-eslint","bradlc.vscode-tailwindcss",
  "dsznajder.es7-react-js-snippets","Vue.volar",
  "formulahendry.auto-rename-tag","formulahendry.auto-close-tag","ritwickdey.LiveServer",
  "humao.rest-client","rangav.vscode-thunder-client","ms-azuretools.vscode-docker",
  "redhat.vscode-yaml","ms-vscode-remote.remote-containers",
  "eamodio.gitlens","mhutchie.git-graph",
  "usernamehw.errorlens","streetsidesoftware.code-spell-checker",
  "christian-kohler.path-intellisense","editorconfig.editorconfig",
  "yzhang.markdown-all-in-one","PKief.material-icon-theme"
)
foreach ($ext in $extensions) { code --install-extension $ext --force }
```

---

## 📦 Що входить у набір

| Категорія | Розширення |
|---|---|
| **Python core** | Python, Pylance, debugpy, Ruff, Black, Mypy, Python Indent, autoDocstring |
| **Jupyter / AI-data** | Jupyter (+renderers, cell-tags), Data Wrangler |
| **AI-асистенти** | Claude Code, GitHub Copilot (+Chat), Continue |
| **Web front-end** | Prettier, ESLint, Tailwind CSS, React snippets, Volar (Vue), auto-rename/close-tag, Live Server |
| **API / backend** | REST Client, Thunder Client, Docker, YAML, Dev Containers |
| **Git** | GitLens, Git Graph |
| **Загальні / DX** | Error Lens, Code Spell Checker, Path Intellisense, EditorConfig, Markdown All in One, Material Icons |

---

## 🛠 Корисні команди

```bash
# показати всі встановлені розширення
code --list-extensions

# зберегти свій список у файл (щоб перенести на інший ПК)
code --list-extensions > my-extensions.txt

# встановити зі збереженого списку
cat my-extensions.txt | xargs -L1 code --install-extension

# видалити розширення
code --uninstall-extension <publisher.name>
```

---

## 💡 Примітки

- **Ruff** замінює одразу лінтер + форматер (Flake8/isort/Black) — якщо користуєтесь ним, Black/Mypy можна не ставити.
- **Copilot** і **Claude Code** платні/за передплатою; **Continue** можна під'єднати до безкоштовних або локальних моделей.
- Для чистих ноутбуків з курсу достатньо блоку **Python core + Jupyter**.
