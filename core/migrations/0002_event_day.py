# Generated by Django 5.2 on 2025-04-09 16:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
