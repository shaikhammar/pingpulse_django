from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthAPITests(APITestCase):

    def test_login_demouser(self):
        # This test relies on the demouser created in the migration 0002_create_demouser.py
        url = reverse("rest_login")
        data = {
            "email": "demouser@example.com",
            "password": "demopassword"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("key", response.data)