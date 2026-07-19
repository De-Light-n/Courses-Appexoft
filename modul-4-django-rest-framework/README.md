# 🌐 Модуль 4 — Django REST Framework (DRF)

Час перетворити знання Python, ООП та БД на **справжній бекенд** — REST API на **Django + DRF**,
найпопулярнішому стеку для веб-сервісів на Python.

## 📓 Матеріали
- **🌐 Веб-основи:** [Як працює веб (клієнт-сервер, DNS, HTTP/HTTPS, WebSocket, Webhooks)](veb-osnovy-yak-pratsyuye-veb.ipynb) — почніть звідси для розуміння вебу
- **Урок 1:** [Основи DRF: REST, архітектура, моделі, ORM, serializers, перші ендпоінти](lektsiya-1-django-rest-framework-osnovy.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-1.ipynb)
- **Урок 2:** [ViewSets, Routers, фільтри/пагінація, автентифікація та permissions](lektsiya-2-viewsets-routery-autentyfikatsiya.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-2.ipynb)
- **🎁 Бонус:** [JWT, Swagger, CORS](bonus-jwt-swagger-cors.ipynb) `🚀 Middle+`

## 🏗️ Робочий проєкт-приклад
У теці [**`proyekt-django/`**](proyekt-django/) — **повноцінний задокументований REST API** (блог:
пости, теги, коментарі, токен-автентифікація, права, тести). Це вся архітектура модуля на живому
коді: моделі зі зв'язками (FK, M2M), serializers (вкладені, валідація), `ModelViewSet` + Router,
кастомні permissions, фільтри/пагінація, `@action`, уникнення N+1, автотести й seed-команда.
Запуск і пояснення — у [proyekt-django/README.md](proyekt-django/README.md).

```bash
cd proyekt-django && pip install -r requirements.txt
python manage.py migrate && python manage.py seed && python manage.py runserver
```

## Програма модуля

### Урок 1 — Основи Django + DRF
- Що таке REST та **всі HTTP-методи** (GET/POST/PUT/PATCH/DELETE + HEAD/OPTIONS/TRACE/CONNECT), safe/idempotent, status codes
- Архітектура Django (MVT) + DRF; шлях запиту
- Структура бекенд-проєкту (проєкт vs app)
- Встановлення та налаштування DRF
- Моделі та міграції
- Serializers (`ModelSerializer`, поля, валідація)
- `APIView` — перший ендпоінт
- Generic Views (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`)

### Урок 2 — Продакшн-інструменти DRF
- ViewSets та `ModelViewSet` (+ `@action`)
- Routers (`DefaultRouter`, `SimpleRouter`)
- Фільтрація, пошук, сортування
- Пагінація
- Автентифікація (Session, Basic, Token) + Token Auth на практиці
- Permissions (вбудовані + кастомні)
- Обробка помилок та статус-коди
- 🔎 Понад базу: зв'язки моделей і вкладені serializers, N+1 (`select_related`/`prefetch_related`), тестування, throttling/versioning

### 🎁 Бонус (Middle+)
- JWT (`djangorestframework-simplejwt`)
- Swagger / OpenAPI (`drf-spectacular`)
- CORS (`django-cors-headers`)

## 🛠 Як ми працюємо
DRF запускається **у справжньому проєкті**, а не в зошиті, тож приклади подано як блоки коду з
реалістичним виводом. Домашки виконуються в окремому Django-проєкті-пісочниці; код і вивід
вставляєте у зошит домашки. Здача — через Pull Request (гілка `<нік>/hw-m4-l<урок>`,
див. [CONTRIBUTING.md](../CONTRIBUTING.md)).

> 💡 Для практики знадобиться: `pip install django djangorestframework django-filter`
> (для бонусу — ще `djangorestframework-simplejwt drf-spectacular django-cors-headers`).
