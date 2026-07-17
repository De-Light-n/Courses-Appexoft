"""
Serializers застосунку `blog` — перетворення об'єктів моделей ⇄ JSON + валідація.

Тут показано кілька важливих прийомів:
- `ModelSerializer` (авто-поля за моделлю);
- read-only поля (`author` не приймаємо від клієнта — беремо з request.user у view);
- вкладені (nested) serializers (коментарі всередині поста);
- `SlugRelatedField` для тегів (клієнт шле НАЗВИ тегів, а не id);
- `SerializerMethodField` (обчислюване поле — кількість коментарів);
- валідація полів (`validate_<поле>`) та кількох полів разом (`validate`).
"""

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Comment, Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class CommentSerializer(serializers.ModelSerializer):
    # Показуємо ім'я автора рядком (read-only) замість id — зручніше клієнту.
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "body", "created_at"]
        read_only_fields = ["id", "author", "created_at"]


class PostListSerializer(serializers.ModelSerializer):
    """Компактний serializer для СПИСКУ постів (без важкого поля body)."""

    author = serializers.StringRelatedField(read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()  # обчислюване поле

    class Meta:
        model = Post
        fields = ["id", "title", "author", "status", "tags", "comment_count", "created_at"]

    def get_comment_count(self, obj: Post) -> int:
        # DRF викликає цей метод для поля comment_count.
        return obj.comments.count()


class PostDetailSerializer(serializers.ModelSerializer):
    """Повний serializer для ОДНОГО поста (створення/оновлення/деталі)."""

    # author лише для читання — клієнт його не задає (див. perform_create у view).
    author = serializers.StringRelatedField(read_only=True)
    # Клієнт передає теги ЯК СПИСОК НАЗВ: {"tags": ["python", "drf"]}.
    tags = serializers.SlugRelatedField(
        slug_field="name",
        many=True,
        queryset=Tag.objects.all(),
        required=False,
    )
    # Вкладені коментарі — лише для читання (створюються окремим ендпоінтом).
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id", "title", "body", "author", "status",
            "tags", "comments", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at"]

    def validate_title(self, value: str) -> str:
        """Валідація одного поля: заголовок не може бути закоротким."""
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Заголовок закороткий (мінімум 5 символів).")
        return value

    def validate(self, data: dict) -> dict:
        """Валідація кількох полів разом: не публікувати пост без тексту."""
        status = data.get("status", getattr(self.instance, "status", None))
        body = data.get("body", getattr(self.instance, "body", ""))
        if status == Post.Status.PUBLISHED and not (body and body.strip()):
            raise serializers.ValidationError("Не можна опублікувати пост без тексту.")
        return data


class UserSerializer(serializers.ModelSerializer):
    """Для реєстрації нового користувача (пароль пишемо, але не читаємо)."""

    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def create(self, validated_data: dict) -> User:
        # create_user хешує пароль (не можна зберігати пароль відкритим текстом!).
        return User.objects.create_user(**validated_data)
