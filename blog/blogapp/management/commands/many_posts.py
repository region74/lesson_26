from django.core.management.base import BaseCommand, CommandError
from blogapp.models import Category, Tag, Post
from mixer.backend.django import mixer


class Command(BaseCommand):
    def handle(self, *args, **options):
        Post.objects.all().delete()
        count = 500
        for i in range(count):
            p = (i / count) * 100
            print(f'{i}) {p}%')
            mixer.blend(Post)
