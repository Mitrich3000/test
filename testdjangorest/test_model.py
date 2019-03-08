from django.test import TestCase

from .models import Products


class ProductsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Products.objects.create(name='Продукт1', category_id=1)

    def test_name_label(self):
        product = Products.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_category_label(self):
        product = Products.objects.get(id=1)
        field_label = product._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'Категория')

    def test_name_max_length(self):
        product = Products.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)
