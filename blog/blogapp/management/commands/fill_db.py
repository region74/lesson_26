from django.core.management.base import BaseCommand, CommandError
from blogapp.models import Category, Tag, Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Выбираем все категории
        categories = Category.objects.all()
        print(categories)
        print(type(categories))
        for item in categories:
            print(item)
            print(type(item))
        print('END')

        # Выбрать одну категорию
        category = Category.objects.get(name='Игры')
        print(category)
        print(type(category))

        # Несколько
        category = Category.objects.filter(name='Игры')
        print(category)
        print(type(category))

        # Связанные поля
        # ForeignKey
        posts = Post.objects.first()
        print(posts)
        print(type(posts.category))
        print(posts.category.name)
        # ManyToMany
        print(posts.tags.all())
        print(posts.tags.first())
        print(posts.tags.first().name)
        print(type(posts.tags.first()))

        # Создание данных
        Category.objects.create(name='Новая', description='что то')

        # Изменение
        category = Category.objects.get(name='Новая')
        category.name = 'Измененная'
        category.save()

        # Удаление
        # можно одну или несколько
        category.delete()

        # Category.objects.all().delete()
