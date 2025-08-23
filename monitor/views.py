from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Service, PingEvent
from .serializers import ServiceSerializer, PingEventSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Service.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PingEventViewSet(viewsets.ModelViewSet):
    serializer_class = PingEventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = PingEvent.objects.filter(service__owner=self.request.user)
        service_id = self.request.query_params.get('service_id')
        if service_id:
            try:
                service = Service.objects.get(pk=service_id, owner=self.request.user)
                queryset = queryset.filter(service=service).order_by('-timestamp')[:20]
            except Service.DoesNotExist:
                raise NotFound(detail="Service with the given ID does not exist or you don't have permission to view it.")
        return queryset