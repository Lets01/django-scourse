#coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

# Ao rodar os testes o django cria um banco temporario e depois destrói esse banco

class IndexViewTestCase(TestCase):

    # criar algo
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    # remover algo
    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')