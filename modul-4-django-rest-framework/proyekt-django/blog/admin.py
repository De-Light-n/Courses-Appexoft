"""
Реєстрація моделей в адмінці Django (/admin/).

Адмінка Django — безкоштовний веб-інтерфейс для перегляду/редагування даних.
Створіть суперкористувача (`python manage.py createsuperuser`) і зайдіть на /admin/.
"""

from django.contrib import admin

from .models import Comment, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_at")  # колонки у списку
    list_filter = ("status", "created_at")                       # фільтри збоку
    search_fields = ("title", "body")                            # рядок пошуку
    filter_horizontal = ("tags",)                                # зручний вибір M2M


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at")


admin.site.register(Tag)
