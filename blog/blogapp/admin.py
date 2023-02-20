from django.contrib import admin
from django.db.models import F

from .models import Category, Post, Tag

admin.site.register(Category)


def clear_rating(modeladmin, request, queryset):
    queryset.update(rating='2')


clear_rating.short_description = 'Выставить рейтинг 2'


def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


set_active.short_description = 'Активировать'


def reverse_set_active(modeladmin, request, queryset):
    queryset.update(is_active=False if F('is_active') == True else True)


reverse_set_active.short_description = 'Инверсия статуса'


def add_raiting(modeladmin, request, queryset):
    queryset.update(rating=F('rating') + 1)


add_raiting.short_description = 'Добавить рейтинг'


def set_passive(modeladmin, request, queryset):
    queryset.update(is_active=False)


set_passive.short_description = 'Деактивировать '


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'rating','category', 'display_tags', 'is_active']
    actions = [clear_rating, set_active, set_passive, reverse_set_active, add_raiting]


admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    actions = [set_active, set_passive]


admin.site.register(Tag, TagAdmin)

# Register your models here.
