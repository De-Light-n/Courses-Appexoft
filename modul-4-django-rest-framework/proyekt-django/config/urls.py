"""
Головна таблиця маршрутів проєкту (root URLconf).

Django, отримавши запит, зіставляє його URL зі списком `urlpatterns` згори вниз.
Тут ми лише «розкладаємо» великі гілки:
- /admin/     -> адмінка Django
- /api/       -> усі маршрути застосунку blog (див. blog/urls.py)
- /api/token/ -> отримати токен за логіном/паролем
- /api-auth/  -> форма входу для «браузерного» API DRF (зручно під час розробки)
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),

    # Усі ендпоінти API живуть під префіксом /api/ (делеговано в blog/urls.py).
    path("api/", include("blog.urls")),

    # POST {username, password} -> {"token": "..."}.
    path("api/token/", obtain_auth_token, name="api-token"),

    # Логін/логаут для DRF Browsable API (кнопка "Log in" у правому верхньому куті).
    path("api-auth/", include("rest_framework.urls")),
]
