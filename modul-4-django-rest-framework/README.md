# 🌐 Модуль 4 — Django REST Framework (DRF)

Час перетворити знання Python, ООП та БД на **справжній бекенд** — REST API на **Django + DRF**,
найпопулярнішому стеку для веб-сервісів на Python.

## 📓 Матеріали
- **Урок 1:** [Основи DRF: REST, архітектура, моделі, serializers, перші ендпоінти](lektsiya-1-django-rest-framework-osnovy.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-1.ipynb)
- **Урок 2:** [ViewSets, Routers, фільтри/пагінація, автентифікація та permissions](lektsiya-2-viewsets-routery-autentyfikatsiya.ipynb) · [домашнє завдання](domashnie-zavdannia-lektsiya-2.ipynb)
- **🎁 Бонус:** [JWT, Swagger, CORS](bonus-jwt-swagger-cors.ipynb) `🚀 Middle+`

## Програма модуля

### Урок 1 — Основи Django + DRF
- Що таке REST та HTTP-методи (GET, POST, PUT, PATCH, DELETE), status codes
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
