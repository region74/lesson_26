from django.test import TestCase
from .models import Post, Category
from userapp.models import BlogUser


# Create your tests here.

class PostTestCase(TestCase):
    def test_has_image(self):
        category = Category.objects.create(name='test_category')
        user = BlogUser.objects.create_user(username='testuser', email='tmp@tmp.ru', password='12345tmp')
        post = Post.objects.create(name='test_post', text='some text', user=user, category=category)
        self.assertFalse(post.has_image())
