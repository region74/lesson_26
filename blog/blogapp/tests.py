from django.test import TestCase
from .models import Post, Category
from userapp.models import BlogUser


# faker - простые данные, например случайно имя
# FactoruBoy    - данные для конкретной модели django
# mixer - полностью создать fake модель

# Create your tests here.

class PostTestCaseFake(TestCase):

    def setUp(self):
        category = Category.objects.create(name='test_category')
        user = BlogUser.objects.create_user(username='testuser', email='tmp@tmp.ru', password='12345tmp')
        # если мало данных генерить то лучше так
        self.post = Post.objects.create(name='test_post', text='some text', user=user, category=category)
        self.post_str = Post.objects.create(name='test_post_str', text='some text', user=user, category=category)

    def test_has_image(self):
        self.assertFalse(self.post.has_image())

    def test_some_method(self):
        # если много данных генерить то лучше черз это
        # post=Post.objects.get(name=test_post)
        self.assertTrue(self.post.some_method() == 'Hi from method')

    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str,category:test_category')
