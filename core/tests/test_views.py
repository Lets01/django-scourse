#coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from model_mommy import mommy


User = get_user_model()


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


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_login_ok(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        data = {'username': self.user.username, 'password': '123'}
        response = self.client.post(self.login_url, data)
        redirect_url = reverse(settings.LOGIN_REDIRECT_URL)
        self.assertRedirects(response, redirect_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated())

    def test_login_error(self):
        data = {'username': self.user.username, 'password': '1234'}
        response = self.client.post(self.login_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        error_msg = ('Por favor, entre com um usuário  e senha corretos.'
                     ' Note que ambos os campos diferenciam maiúsculas e minúsculas.')
        self.assertFormError(response, 'form', None, error_msg)


class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_ok(self):
        data = {'username': 'gileno', 'password1': 'teste123', 'password2': 'teste123'}
        response = self.client.post(self.register_url, data)
        index_url = reverse('index')
        self.assertRedirects(response, index_url)
        self.assertEquals(User.objects.count(), 1)