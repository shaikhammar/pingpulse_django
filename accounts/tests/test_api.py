
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthAPITests(APITestCase):

    def test_registration(self):
        url = reverse("rest_register")
        data = {
            "email": "test@example.com",
            "password1": "$Ay687a$",
            "password2": "$Ay687a$"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "test@example.com")

    def test_login(self):
        # First, create a user to log in with
        email = "test@example.com"
        password = "$Ay687a$"
        user = User.objects.create_user(email=email, password=password)

        url = reverse("rest_login")
        data = {
            "email": email,
            "password": password
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("key", response.data)