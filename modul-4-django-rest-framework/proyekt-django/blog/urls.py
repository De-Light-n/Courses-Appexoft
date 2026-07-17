"""
Маршрути застосунку `blog`.

Для ViewSet-ів не виписуємо кожен path вручну — їх генерує Router.
Підключається в config/urls.py під префіксом /api/.
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet, RegisterView, health

# DefaultRouter створює всі CRUD-маршрути + кореневу сторінку API зі списком ендпоінтів.
router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    # Ендпоінти, не пов'язані з ViewSet, додаємо вручну:
    path("register/", RegisterView.as_view(), name="register"),
    path("health/", health, name="health"),
]

# Додаємо автозгенеровані маршрути роутера (posts/, posts/{id}/, comments/ тощо).
urlpatterns += router.urls
