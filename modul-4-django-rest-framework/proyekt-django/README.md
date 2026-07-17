# 🌐 `proyekt-django` — робочий приклад REST API (Django + DRF)

Повноцінний, **максимально задокументований** навчальний проєкт до [Модуля 4](../README.md).
Це «блог-API»: пости, теги, коментарі, автентифікація токеном і права доступу. На ньому видно
**всю архітектуру** з уроків на живому, робочому коді — його можна запустити й «поколупати».

> Кожен файл усередині має докстрінг-пояснення й коментарі українською. Читайте код —
> він сам є частиною матеріалу.

---

## 🏗️ Архітектура та де що лежить

```
proyekt-django/
├── manage.py                  # CLI Django (runserver, migrate, test, seed...)
├── requirements.txt           # залежності (Django, DRF, django-filter)
├── config/                    # ПАКЕТ ПРОЄКТУ (налаштування всього сайту)
│   ├── settings.py            #   конфіг: INSTALLED_APPS, БД, REST_FRAMEWORK
│   ├── urls.py                #   головні маршрути (/admin, /api, /api/token)
│   ├── wsgi.py / asgi.py      #   точки входу для сервера
└── blog/                      # ЗАСТОСУНОК (уся логіка блогу)
    ├── models.py              #   таблиці БД: Post, Tag, Comment (+ зв'язки)
    ├── serializers.py         #   об'єкт ⇄ JSON + валідація
    ├── views.py               #   ViewSets, generic view, APIView, @action
    ├── permissions.py         #   кастомний IsAuthorOrReadOnly
    ├── urls.py                #   Router (авто-маршрути CRUD)
    ├── admin.py               #   реєстрація моделей в адмінці
    ├── tests.py               #   APITestCase (CRUD, права, фільтри)
    ├── migrations/            #   версії схеми БД
    └── management/commands/
        └── seed.py            #   демо-дані (python manage.py seed)
```

**Потік запиту:** `config/urls.py → blog/urls.py (Router) → views.py (ViewSet) →
serializers.py (⇄ JSON) → models.py (ORM) → база даних`.

---

## 🚀 Запуск (крок за кроком)

```bash
# 1. (Рекомендовано) окреме віртуальне оточення — див. Модуль 2, Урок 2
python -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Встановити залежності
pip install -r requirements.txt

# 3. Створити таблиці в БД
python manage.py migrate

# 4. Наповнити демо-даними (користувач demo / demo12345)
python manage.py seed

# 5. (Необов'язково) свій суперкористувач для адмінки /admin/
python manage.py createsuperuser

# 6. Запустити сервер
python manage.py runserver
#   -> http://127.0.0.1:8000/api/      (браузерне API DRF)
#   -> http://127.0.0.1:8000/admin/    (адмінка)
```

---

## 🔌 Ендпоінти

| Метод(и) | URL | Що робить | Доступ |
|----------|-----|-----------|--------|
| GET, POST | `/api/posts/` | список / створити пост | читати — всім; створити — авторизованим |
| GET, PUT, PATCH, DELETE | `/api/posts/{id}/` | деталі / оновити / видалити | змінювати — лише автор |
| POST | `/api/posts/{id}/publish/` | опублікувати пост | автор |
| GET | `/api/posts/mine/` | мої пости | авторизований |
| GET | `/api/posts/stats/` | статистика (ORM annotate/aggregate) | усім |
| GET, POST | `/api/comments/` | список / додати коментар | створити — авторизованим |
| POST | `/api/register/` | реєстрація користувача | усім |
| POST | `/api/token/` | отримати токен | усім |
| GET | `/api/health/` | перевірка «чи живе API» | усім |

Фільтри для постів: `?status=published`, `?tags__name=python`, `?search=django`,
`?ordering=-created_at`, `?page=2` (можна комбінувати).

---

## 🧪 Приклади запитів (curl)

```bash
# Реєстрація + отримання токена
curl -X POST http://127.0.0.1:8000/api/register/ -H "Content-Type: application/json" \
     -d '{"username":"ivan","password":"secret123"}'
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=ivan&password=secret123"
# -> {"token":"abc123..."}

# Список постів (без токена — читання публічне)
curl http://127.0.0.1:8000/api/posts/

# Створити пост (з токеном; теги — списком назв)
curl -X POST http://127.0.0.1:8000/api/posts/ \
     -H "Authorization: Token abc123..." -H "Content-Type: application/json" \
     -d '{"title":"Мій перший пост","body":"Текст поста","tags":["python","django"]}'

# Опублікувати
curl -X POST http://127.0.0.1:8000/api/posts/1/publish/ -H "Authorization: Token abc123..."
```

---

## ✅ Тести

```bash
python manage.py test
```
Покривають: публічність списку, `401` без токена на створення, автозаповнення автора,
валідацію заголовка, `403` для чужого редагування, дію `publish`, фільтрацію за статусом,
реєстрацію та health-check.

---

## 🎓 Що цей проєкт демонструє з уроків

- **Урок 1:** моделі + міграції; serializers + валідація; APIView / generic view.
- **Урок 2:** ModelViewSet + Router; фільтрація/пошук/сортування; пагінація; Token-автентифікація;
  вбудовані та **кастомні** permissions; правильні status-коди.
- **Понад програму:** зв'язки моделей (FK, M2M), вкладені serializers, різні serializers для
  списку й деталей, `@action`, уникнення **N+1** (`select_related`/`prefetch_related`),
  management-команда, автотести.
