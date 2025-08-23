from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Service, PingEvent

User = get_user_model()

class TestMonitorAPI(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email="user1@example.com", password="password1")
        self.user2 = User.objects.create_user(email="user2@example.com", password="password2")

        self.service1 = Service.objects.create(name="Service 1", url="http://service1.com", owner=self.user1)
        self.service2 = Service.objects.create(name="Service 2", url="http://service2.com", owner=self.user2)

    def test_list_services(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get("/api/monitor/services/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.service1.name)

    def test_create_service(self):
        self.client.force_authenticate(user=self.user1)
        data = {"name": "New Service", "url": "http://newservice.com"}
        response = self.client.post("/api/monitor/services/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 3)
        self.assertEqual(Service.objects.last().name, "New Service")
        self.assertEqual(Service.objects.last().owner, self.user1)

    def test_list_ping_events(self):
        self.client.force_authenticate(user=self.user1)
        # Create some ping events for service1
        PingEvent.objects.create(service=self.service1, status=PingEvent.Status.UP)
        PingEvent.objects.create(service=self.service1, status=PingEvent.Status.DOWN)
        response = self.client.get(f"/api/monitor/ping-events/?service_id={self.service1.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_ping_events_for_other_user_service(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(f"/api/monitor/ping-events/?service_id={self.service2.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_ping_events_returns_latest_20(self):
        self.client.force_authenticate(user=self.user1)
        # Create 25 ping events for service1
        for i in range(25):
            PingEvent.objects.create(service=self.service1, status=PingEvent.Status.UP)
        response = self.client.get(f"/api/monitor/ping-events/?service_id={self.service1.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 20)

    def test_list_ping_events_for_non_existent_service(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get("/api/monitor/ping-events/?service_id=999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)