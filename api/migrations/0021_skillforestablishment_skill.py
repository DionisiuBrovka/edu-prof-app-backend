# Generated by Django 4.2.7 on 2024-01-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_skill_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillforestablishment',
            name='skill',
            field=models.ManyToManyField(related_name='svod', to='api.skill', verbose_name='Квалификация'),
        ),
    ]
