# Generated by Django 4.2.4 on 2023-12-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileapp', '0002_uploadedfile_shared_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='shared',
            field=models.BooleanField(default=False),
        ),
    ]
