# Generated by Django 4.2.7 on 2023-12-10 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_skill_remove_establishment_specialty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='s_type',
        ),
    ]
