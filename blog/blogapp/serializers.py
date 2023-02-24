from django.urls import path, include
from .models import Category,Post
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        exclude = ['user']


