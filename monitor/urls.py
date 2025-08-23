from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, PingEventViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'ping-events', PingEventViewSet, basename='pingevent')

urlpatterns = [
    path('', include(router.urls)),
]
