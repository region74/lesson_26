from django.db import models


# Create your models here.

class Category(models.Model):
    # Id не надо
    name = models.CharField(max_length=20, unique=True)
    # Бланк это тип поле может быть пустым
    description = models.TextField(blank=True)

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


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=50, unique=True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # Связь с категорией
    # один много
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # связь с тегом
    # много-много
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
