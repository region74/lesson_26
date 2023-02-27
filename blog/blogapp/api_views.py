from .models import Category, Post, Tag
from .serializers import CategorySerializer, PostSerializer, TagSerializer
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    # queryset = Category.objects.all()
    queryset = Category.objects.select_related().all()
    # queryset = Category.objects.select_related()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    # queryset = Post.objects.all()
    # оптимизируем
    queryset = Post.objects.prefetch_related('tags')
    serializer_class = PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
