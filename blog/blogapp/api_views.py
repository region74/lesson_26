from .models import Category, Post, Tag
from .serializers import CategorySerializer, PostSerializer, TagSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .permissions import ReadOnly, IsAuthor, IsAuthenticated
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication


class CategoryViewSet(viewsets.ModelViewSet):
    # права доступа
    permission_classes = [IsAdminUser | ReadOnly]
    # queryset = Category.objects.all()
    queryset = Category.objects.select_related().all()
    # queryset = Category.objects.select_related()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    # queryset = Post.objects.all()
    # оптимизируем
    permission_classes = [IsAuthor | ReadOnly | IsAdminUser]
    queryset = Post.objects.prefetch_related('tags')
    serializer_class = PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BaseAuthentication, TokenAuthentication]
    authentication_classes=[SessionAuthentication,BaseAuthentication,TokenAuthentication]
    # permission_classes = [IsAuthenticated|TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
