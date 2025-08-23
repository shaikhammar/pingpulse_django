import requests
from celery import shared_task
from .models import Service, PingEvent

@shared_task
def run_all_health_checks():
    for service in Service.objects.all():
        check_service.delay(service.id)

@shared_task
def check_service(service_id):
    """
    Checks a single service.
    """
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        return

    try:
        response = requests.get(service.url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        PingEvent.objects.create(
            service=service,
            status=PingEvent.Status.UP,
            response_time=response.elapsed.total_seconds()
        )

    except requests.RequestException:
        PingEvent.objects.create(
            service=service,
            status=PingEvent.Status.DOWN,
            response_time=0
        )
