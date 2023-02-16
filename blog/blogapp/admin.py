from django.contrib import admin
from .models import Category, Post, Tag

admin.site.register(Category)


def clear_rating(modeladmin, request, queryset):
    queryset.update(rating='2')


clear_rating.short_description = 'Выставить рейтинг 2'


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'category', 'display_tags']
    actions = [clear_rating]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

# Register your models here.
