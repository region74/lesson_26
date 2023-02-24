from django.urls import path, include
from .models import Category
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


