"""
Моделі застосунку `blog` — опис таблиць бази даних через Python-класи (Django ORM).

Тут демонструються всі типи зв'язків між таблицями:
- **один-до-багатьох** (ForeignKey): у поста багато коментарів; в автора багато постів;
- **багато-до-багатьох** (ManyToManyField): пост має багато тегів, тег — у багатьох постах.

Після зміни цього файлу треба зробити міграції:
    python manage.py makemigrations
    python manage.py migrate
"""

from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    """Тег (мітка) для постів. Один тег може стояти на багатьох постах."""

    name = models.CharField(max_length=50, unique=True, help_text="Назва тегу, напр. 'python'")

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        # Як об'єкт показується в адмінці/консолі (згадайте __str__ з Модуля 2).
        return self.name


class Post(models.Model):
    """Пост блогу — центральна сутність застосунку."""

    # Статуси поста. TextChoices дає і значення в БД, і людську назву.
    class Status(models.TextChoices):
        DRAFT = "draft", "Чернетка"
        PUBLISHED = "published", "Опубліковано"

    # Зв'язок один-до-багатьох: автор (User) має багато постів.
    # related_name="posts" дозволяє писати user.posts.all().
    # on_delete=CASCADE: якщо видалити користувача — його пости теж видаляться.
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        help_text="Автор поста (встановлюється автоматично з поточного користувача).",
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    # Зв'язок багато-до-багатьох: пост має багато тегів, тег — у багатьох постах.
    # blank=True означає, що пост можна створити й без тегів.
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # ставиться раз при створенні
    updated_at = models.DateTimeField(auto_now=True)      # оновлюється при кожному save

    class Meta:
        ordering = ["-created_at"]  # найновіші пости — першими

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """Коментар до поста. Зв'язок один-до-багатьох: у поста багато коментарів."""

    # related_name="comments" -> post.comments.all() поверне всі коментарі поста.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"Коментар #{self.pk} до '{self.post.title}'"
