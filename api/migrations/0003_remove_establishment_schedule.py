# Generated by Django 4.2.7 on 2023-12-05 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_establishment_specialty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establishment',
            name='schedule',
        ),
    ]