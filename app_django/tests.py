# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass')

    def test_register(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password': 'newpass',
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_connexion(self):
        response = self.client.post(reverse('connexion'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_mes_pokemons(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('mes_pokemons'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_role(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse('role'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
