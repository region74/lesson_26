from django.test import Client
from django.test import TestCase
from faker import Faker
from .models import BlogUser


class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # что еще проверим
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        # post зарос
        response = self.client.post('/contact/', {'name': self.fake.name(), 'message': self.fake.text(),
                                                  'email': self.fake.email()})
        self.assertEqual(response.status_code, 302)

        # проверка контекста
        response = self.client.get('/')
        self.assertTrue('posts' in response.context)
        # response.context['name']

    def test_login_required(self):
        user = BlogUser.objects.create_user(username='test_user', email='tmp@tmp.ru', password='12345tmp')
        # он не вошел
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 302)
        # он вошел
        self.client.login(username='test_user', password='12345tmp')
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)
