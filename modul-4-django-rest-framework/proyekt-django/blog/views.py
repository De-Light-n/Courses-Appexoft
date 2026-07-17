"""
Views застосунку `blog` — логіка ендпоінтів API.

Показано два підходи:
1. `PostViewSet` / `CommentViewSet` (ModelViewSet) — увесь CRUD + маршрути через Router;
2. `RegisterView` (APIView) та `health` (function-based @api_view) — для повноти картини.

Також показано «продакшн-дрібниці»:
- різні serializers для списку й деталей (`get_serializer_class`);
- автозаповнення автора з поточного користувача (`perform_create`);
- фільтрація/пошук/сортування;
- власна дія `@action` (publish);
- уникнення проблеми N+1 через select_related/prefetch_related.
"""

from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Comment, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    PostDetailSerializer,
    PostListSerializer,
    UserSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD над постами. Один клас = 6 ендпоінтів:
        GET    /api/posts/          -> список   (list)
        POST   /api/posts/          -> створити (create)
        GET    /api/posts/{id}/     -> деталі   (retrieve)
        PUT    /api/posts/{id}/     -> замінити (update)
        PATCH  /api/posts/{id}/     -> частково (partial_update)
        DELETE /api/posts/{id}/     -> видалити (destroy)
    Плюс власна дія:
        POST   /api/posts/{id}/publish/  -> опублікувати
        GET    /api/posts/mine/          -> мої пости
    """

    # select_related (для ForeignKey author) + prefetch_related (для M2M tags та
    # зворотного FK comments) вантажать усе одним пакетом запитів -> без N+1.
    queryset = (
        Post.objects.select_related("author")
        .prefetch_related("tags", "comments")
        .all()
    )
    # Права: читати всім; змінювати — автентифікованим; редагувати/видаляти — лише автору.
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    # Звуження вибірки через query-параметри:
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "tags__name"]   # ?status=published&tags__name=python
    search_fields = ["title", "body"]             # ?search=django
    ordering_fields = ["created_at", "title"]     # ?ordering=-created_at

    def get_serializer_class(self):
        # Для списку — компактний serializer; для решти — повний.
        if self.action == "list":
            return PostListSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        # Автор НЕ приходить від клієнта — беремо поточного користувача.
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        """POST /api/posts/{id}/publish/ — перевести пост у статус 'опубліковано'."""
        post = self.get_object()  # також перевіряє права об'єкта (IsAuthorOrReadOnly)
        post.status = Post.Status.PUBLISHED
        post.save(update_fields=["status", "updated_at"])
        return Response({"status": "опубліковано", "id": post.id})

    @action(detail=False)
    def mine(self, request):
        """GET /api/posts/mine/ — лише пости поточного користувача."""
        if not request.user.is_authenticated:
            return Response({"detail": "Потрібна автентифікація."},
                            status=status.HTTP_401_UNAUTHORIZED)
        posts = self.get_queryset().filter(author=request.user)
        page = self.paginate_queryset(posts)
        serializer = PostListSerializer(page or posts, many=True)
        return self.get_paginated_response(serializer.data) if page is not None \
            else Response(serializer.data)

    @action(detail=False, permission_classes=[AllowAny])
    def stats(self, request):
        """
        GET /api/posts/stats/ — статистика через ORM annotate/aggregate.
        aggregate -> одне число по всій вибірці; annotate -> число на кожну ГРУПУ.
        """
        total = Post.objects.aggregate(total=Count("id"))["total"]     # одне число
        by_status = (
            Post.objects.values("status")            # групуємо за статусом
            .annotate(count=Count("id"))             # рахуємо в кожній групі
            .order_by("status")
        )
        return Response({"total": total, "by_status": list(by_status)})


class CommentViewSet(viewsets.ModelViewSet):
    """CRUD над коментарями (post передається в тілі при створенні)."""

    queryset = Comment.objects.select_related("author", "post").all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RegisterView(generics.CreateAPIView):
    """
    POST /api/register/ — реєстрація нового користувача.
    Приклад generic-view (CreateAPIView) з відкритим доступом.
    """

    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # реєструватись може будь-хто


@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    """GET /api/health/ — найпростіший ендпоінт (function-based view) для перевірки, що API живе."""
    return Response({"status": "ok"})
