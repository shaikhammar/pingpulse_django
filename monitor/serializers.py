from rest_framework import serializers
from .models import Service, PingEvent

class ServiceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Service
        fields = ['id', 'name', 'url', 'owner', 'created_at']

class PingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PingEvent
        fields = '__all__'
