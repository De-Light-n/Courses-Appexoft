"""
Тести API застосунку `blog` (DRF `APITestCase`).

Запуск:  python manage.py test
Кожен тест працює в окремій тимчасовій БД, яку Django створює й видаляє автоматично.
Покриваємо: список, автентифікацію на створення, права автора, фільтрацію та @action.
"""

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Post


class PostAPITests(APITestCase):
    def setUp(self):
        # Два користувачі: автор і «чужий».
        self.author = User.objects.create_user(username="author", password="pass12345")
        self.other = User.objects.create_user(username="other", password="pass12345")
        self.author_token = Token.objects.create(user=self.author)
        # Готовий пост від author.
        self.post = Post.objects.create(
            author=self.author, title="Перший пост", body="Тіло поста", status=Post.Status.PUBLISHED
        )

    def auth(self, token):
        """Додати заголовок Authorization: Token <...> до подальших запитів."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    # --- читання (публічне) ---------------------------------------------------
    def test_list_posts_is_public(self):
        resp = self.client.get("/api/posts/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # З пагінацією відповідь має ключ results.
        self.assertEqual(resp.data["count"], 1)

    # --- створення потребує автентифікації ------------------------------------
    def test_create_requires_auth(self):
        resp = self.client.post("/api/posts/", {"title": "Новий пост", "body": "текст"})
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_with_token_sets_author(self):
        self.auth(self.author_token)
        resp = self.client.post(
            "/api/posts/", {"title": "Новий пост", "body": "достатньо тексту"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.data["author"], "author")  # автор проставлений автоматично

    # --- валідація ------------------------------------------------------------
    def test_short_title_is_rejected(self):
        self.auth(self.author_token)
        resp = self.client.post("/api/posts/", {"title": "abc", "body": "текст"}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", resp.data)

    # --- права: чужий не може редагувати --------------------------------------
    def test_other_user_cannot_edit(self):
        other_token = Token.objects.create(user=self.other)
        self.auth(other_token)
        resp = self.client.patch(
            f"/api/posts/{self.post.id}/", {"title": "Змінено чужим"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_author_can_edit(self):
        self.auth(self.author_token)
        resp = self.client.patch(
            f"/api/posts/{self.post.id}/", {"title": "Оновлений заголовок"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    # --- власна дія publish ---------------------------------------------------
    def test_publish_action(self):
        draft = Post.objects.create(
            author=self.author, title="Чернетка поста", body="текст", status=Post.Status.DRAFT
        )
        self.auth(self.author_token)
        resp = self.client.post(f"/api/posts/{draft.id}/publish/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        draft.refresh_from_db()
        self.assertEqual(draft.status, Post.Status.PUBLISHED)

    # --- фільтрація -----------------------------------------------------------
    def test_filter_by_status(self):
        Post.objects.create(author=self.author, title="Чернетка тут", body="x", status=Post.Status.DRAFT)
        resp = self.client.get("/api/posts/?status=published")
        self.assertEqual(resp.data["count"], 1)  # лише 1 опублікований (з setUp)

    # --- статистика (annotate/aggregate) --------------------------------------
    def test_stats_aggregation(self):
        Post.objects.create(author=self.author, title="Чернетка тут", body="x", status=Post.Status.DRAFT)
        resp = self.client.get("/api/posts/stats/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["total"], 2)  # aggregate: усього постів
        by_status = {row["status"]: row["count"] for row in resp.data["by_status"]}
        self.assertEqual(by_status, {"draft": 1, "published": 1})  # annotate: по групах


class RegisterAndHealthTests(APITestCase):
    def test_health(self):
        resp = self.client.get("/api/health/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, {"status": "ok"})

    def test_register_creates_user(self):
        resp = self.client.post(
            "/api/register/", {"username": "newbie", "password": "secret123"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newbie").exists())
