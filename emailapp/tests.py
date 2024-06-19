# emailapp/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='password123'
        )

    def test_login(self):
        response = self.client.post(reverse('login'), {'email': 'testuser@example.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)  # Redirects after successful login

    def test_compose_email(self):
        self.client.login(email='testuser@example.com', password='password123')
        response = self.client.post(reverse('compose_email'), {
            'recipient': 'recipient@example.com',
            'subject': 'Test Subject',
            'body': 'Test Body'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful form submission
