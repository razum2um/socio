# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client

from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.core.mail import outbox

class SignUpTest (TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test', email='test@mail.com')
        self.email = 'demo@demo.de'
        self.client = Client()

    def test_sign_up_render(self):
        response = self.client.get(reverse('sign_up'))

        self.assertEquals(response.status_code, 200)
        self.assertNotEqual(response.context['sign_up_form'], None)

    def test_sign_up(self):
        response = self.client.post(reverse('sign_up'), {'email': self.email })


#        self.assertEquals(len(outbox), 1)
        self.assertEquals(User.objects.filter(username=self.email).count(), 1)
        self.assertRedirects(response, reverse('index'))

    def test_sign_up_authenticated(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('sign_up'))

        self.assertRedirects(response, reverse('index'))

    def test_sign_out(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('sign_out'))

        self.assertRedirects(response, reverse('index'))

    def test_sign_in_render(self):
        response = self.client.get(reverse('sign_in'))

#        self.assertEquals(response.status_code, 200)
#        self.assertNotEqual(response.context['sign_in_form'], None)

