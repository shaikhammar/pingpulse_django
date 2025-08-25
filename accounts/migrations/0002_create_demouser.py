from django.db import migrations
from django.contrib.auth import get_user_model

def create_demouser(apps, schema_editor):
    USER = get_user_model()
    User.objects.create_user(email='demouser@example.com', password='demopassword')

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_demouser),
    ]
