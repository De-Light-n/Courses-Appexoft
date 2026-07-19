"""
Кастомні permissions застосунку `blog`.

Permission відповідає на питання «чи можна ЦЬОМУ користувачу зробити ЦЮ дію?».
Тут — класичне правило «редагувати/видаляти може лише автор об'єкта».
"""

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Читати (GET/HEAD/OPTIONS) — дозволено всім.
    Змінювати/видаляти (POST/PUT/PATCH/DELETE) — лише автору об'єкта.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        # SAFE_METHODS = ("GET", "HEAD", "OPTIONS") — безпечні, лише читання.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Для змін — об'єкт має належати тому, хто робить запит.
        return obj.author == request.user
