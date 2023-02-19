from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class BlogUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)

    # переопределение метода сейв
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Создать профиль
        # если профиль не создан
        if not Profile.objects.filter(user=self).exists():
            Profile.objects.create(user=self)


# Create your models here.

class Profile(models.Model):
    # При создании пользователя создать Profile
    info = models.TextField(blank=True)
    user = models.OneToOneField(BlogUser, on_delete=models.CASCADE)


# @receiver(post_save, sender=BlogUser)
# def create_profile(sender, instance, **kwargs):
#     if not Profile.objects.filter(user=instance).exists():
#         Profile.objects.create(user=instance)
