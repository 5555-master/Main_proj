# Generated by Django 4.0.1 on 2022-01-31 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
    ]
