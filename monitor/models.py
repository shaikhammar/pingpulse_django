from django.db import models
from accounts.models import User # Assuming you created this

class Service(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PingEvent(models.Model):
    class Status(models.TextChoices):
        UP = 'UP', 'Up'
        DOWN = 'DOWN', 'Down'

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='events')
    status = models.CharField(max_length=4, choices=Status.choices)
    response_time = models.FloatField(null=True, blank=True) # in seconds
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service.name} is {self.status} at {self.timestamp}"