from django.test import TestCase
from django.urls import reverse
from rango_app.models import Category

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

class ViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to Rango!')

    def test_add_category_view(self):
        response = self.client.get(reverse('add_category'))
        self.assertEqual(response.status_code, 200)
