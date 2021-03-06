# coding=utf-8


from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from model_mommy import mommy
from catalog.models import Category, Product


class ProductListTestCase(TestCase):
    # criar algo
    def setUp(self):
        self.url = reverse('catalog:product_list')
        self.client = Client()
        mommy.make('catalog.Product',_quantity=3)

    def tearDown(self):
        Product.objects.all().delete()

    def test_view_okl(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    # Verifica se a quantidade de produtos esta dentro do esperado
    # def test_context(self):
    #     response = self.client.get(self.url)
    #     self.assertTrue('product_list' in response.context)
    #     product_list = response.context['product_list']
    #     self.assertEquals(product_list.count(),3)