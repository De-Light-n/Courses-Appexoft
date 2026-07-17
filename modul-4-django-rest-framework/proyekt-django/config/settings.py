"""
Налаштування Django-проєкту `config`.

Це «мозок» проєкту: тут підключаються застосунки (INSTALLED_APPS), база даних, middleware
та конфігурація Django REST Framework (REST_FRAMEWORK).

⚠️ Це НАВЧАЛЬНИЙ проєкт (DEBUG=True, секретний ключ у коді). У продакшені секрети виносять
   у змінні середовища (.env) — див. Модуль 2, Урок 2 (розділ про env).

Докладно: https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Корінь проєкту (тека, де лежить manage.py). Шляхи будуємо як BASE_DIR / "щось".
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Безпека (для розробки) ---------------------------------------------------
# У ПРОДАКШЕНІ: SECRET_KEY брати з env, DEBUG=False, ALLOWED_HOSTS = ["ваш.домен"].
SECRET_KEY = "django-insecure-khuqyedp^nmbsr606@#om9u4f2gx40&xurky+uep6pxyl%nhmw"
DEBUG = True
ALLOWED_HOSTS = []

# --- Застосунки ---------------------------------------------------------------
INSTALLED_APPS = [
    # Вбудовані застосунки Django:
    "django.contrib.admin",          # адмінка
    "django.contrib.auth",           # користувачі, групи, права
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Сторонні (встановлені через pip):
    "rest_framework",                # Django REST Framework
    "rest_framework.authtoken",      # Token-автентифікація (таблиця токенів)
    "django_filters",                # фільтрація за полями
    # Наші застосунки:
    "blog",                          # застосунок блогу (моделі/serializers/views)
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"          # головна таблиця маршрутів

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# --- База даних ---------------------------------------------------------------
# SQLite — файл db.sqlite3 у корені проєкту (0 налаштувань). У проді — PostgreSQL.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- Валідація паролів ---------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Локалізація --------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --- Статика ------------------------------------------------------------------
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =============================================================================
# Django REST Framework — уся конфігурація API в одному місці.
# Це «глобальні значення за замовчуванням»; будь-який view може їх перевизначити.
# =============================================================================
REST_FRAMEWORK = {
    # Хто робить запит (автентифікація). Token — для API-клієнтів, Session — для
    # зручного «браузерного» API під час розробки.
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    # Що дозволено за замовчуванням: читати всім, змінювати — лише автентифікованим.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    # Механізми звуження вибірки (?status=..., ?search=..., ?ordering=...).
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    # Пагінація: по 10 записів на сторінку (?page=2).
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}
