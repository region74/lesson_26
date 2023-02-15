from django.test import TestCase
from .models import Post, Category
from userapp.models import BlogUser
from faker import Faker
from mixer.backend.django import mixer


# faker - простые данные, например случайно имя
# FactoruBoy    - данные для конкретной модели django
# mixer - полностью создать fake модель

# Create your tests here.

class PostTestCaseFaker(TestCase):

    def setUp(self):
        faker = Faker()
        category = Category.objects.create(name='test_category')
        user = BlogUser.objects.create_user(username=faker.name(), email='tmp@tmp.ru', password='12345tmp')
        # если мало данных генерить то лучше так
        self.post = Post.objects.create(name=faker.name(), text=faker.name(), user=user, category=category)
        self.post_str = Post.objects.create(name='test_post_str', text='some text', user=user, category=category)

    def test_has_image(self):
        self.assertFalse(self.post.has_image())

    def test_some_method(self):
        # если много данных генерить то лучше черз это
        # post=Post.objects.get(name=test_post)
        self.assertTrue(self.post.some_method() == 'Hi from method')

    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str,category:test_category')


class PostTestCaseMixer(TestCase):

    def setUp(self):
        faker = Faker()
        self.post = mixer.blend(Post)

        # Хороший вариант
        # category = mixer.blend(Category, name='test_category')
        # self.post_str = mixer.blend(Post, name='test_post_str', category=category)

        # Еще лучше варик (короткая запись)
        self.post_str = mixer.blend(Post, name='test_post_str', category__name='test_category')

    def test_has_image(self):
        self.assertFalse(self.post.has_image())

    def test_some_method(self):
        self.assertTrue(self.post.some_method() == 'Hi from method')

    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str,category:test_category')
