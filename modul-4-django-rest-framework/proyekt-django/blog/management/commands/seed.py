"""
Кастомна management-команда для наповнення БД демо-даними.

Запуск:  python manage.py seed

Створює тестового користувача (demo/demo12345), кілька тегів і постів із коментарями,
щоб одразу було що подивитись в API та адмінці.
"""

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from blog.models import Comment, Post, Tag


class Command(BaseCommand):
    help = "Наповнити базу демо-даними (користувач demo, теги, пости, коментарі)."

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(username="demo")
        if created:
            user.set_password("demo12345")
            user.save()

        tags = [Tag.objects.get_or_create(name=n)[0] for n in ["python", "django", "drf"]]

        if Post.objects.exists():
            self.stdout.write(self.style.WARNING("Дані вже є — пропускаю створення постів."))
            return

        p1 = Post.objects.create(
            author=user, title="Знайомство з Django REST Framework",
            body="DRF робить із Django зручний інструмент для REST API.",
            status=Post.Status.PUBLISHED,
        )
        p1.tags.set(tags)
        p2 = Post.objects.create(
            author=user, title="Чернетка про ViewSets",
            body="ModelViewSet дає весь CRUD одним класом.",
            status=Post.Status.DRAFT,
        )
        p2.tags.set(tags[:2])

        Comment.objects.create(post=p1, author=user, body="Чудова стаття, дякую!")
        Comment.objects.create(post=p1, author=user, body="А коли буде про JWT?")

        self.stdout.write(self.style.SUCCESS(
            "Готово! Користувач: demo / demo12345. Створено 2 пости, 3 теги, 2 коментарі."
        ))
