# Generated by Django 4.2.4 on 2023-12-08 08:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared_files', to=settings.AUTH_USER_MODEL),
        ),
    ]