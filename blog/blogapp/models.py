from django.db import models
from django.utils.functional import cached_property

from userapp.models import BlogUser


# 3 типа наследования джанго
# абстрактный класс
# класическое наследование
# прокси

class ActiveManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)


class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


# class UpdatedObjectsManager(models.Manager):
#     def get_queryset(self):
#         all_objects = super().get_queryset()
#         # Дата обновления не равна дате создания F-запрос
#         return all_objects.filter(update)


class TimeStamp(models.Model):
    """
    Адстрактное наследование - для нее не создаются новые таблицы
    данные хранятся в каждом наследнике
    """
    create = models.DateTimeField(auto_now_add=True)
    # оптимизация ускорится поиск типо от индексирования
    update = models.DateTimeField(auto_now=True,db_index=True)

    class Meta:
        abstract = True


# Create your models here.

class Category(models.Model):
    # Id не надо
    name = models.CharField(max_length=20, unique=True, verbose_name='Name')
    # Бланк это тип поле может быть пустым
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # # основыне типы полей
    # # дата
    # models.DateTimeField
    # models.DateField
    # models.TimeField
    # # Числа
    # models.IntegerField
    # models.PositiveIntegerField
    # models.PositiveSmallIntegerField
    # models.FloatField
    # models.DecimalField
    # # Логика
    # models.BooleanField
    # # Байты
    # models.BinaryField
    # # Картинка
    # models.ImageField
    # # Файл
    # models.FileField
    # # url,email
    # models.URLField
    # models.EmailField

    # Чтобы в админке выводилось нормально, а не object
    def __str__(self):
        return self.name


class Chiled(ActiveManager):
    pass


class Tag(IsActiveMixin):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Post(TimeStamp, IsActiveMixin):
    name = models.CharField(max_length=50, unique=True)
    text = models.TextField()
    # Связь с категорией
    # один много
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_posts')
    # связь с тегом
    # много-много
    tags = models.ManyToManyField(Tag)
    # Картинка
    # 2 варианта хранения пикч 1 -в базе 2 -на диске
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.name},category:{self.category.name}'

    def display_tags(self):
        tags = self.tags.all()
        result = ';'.join([item.name for item in tags])
        return result

    def has_image(self):
        return bool(self.image)

    def some_method(self):
        return 'Hi from method'

    @cached_property
    def get_all_tags(self):
        tags = Tag.objects.all()
        return tags

# Классическое наследование
# obj=CoreObjects.object.all()
# obj.tag
# obj.post

# class CoreObject(models.Model):
#     name = models.CharField(max_length=20)
#
#
# class Car(CoreObject):
#     description = models.TextField(max_length=50)
#
#
# class Flyboard(CoreObject):
#     description = models.TextField(max_length=50)
