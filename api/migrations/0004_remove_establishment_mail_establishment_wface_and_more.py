# Generated by Django 4.2.7 on 2023-12-10 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_establishment_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establishment',
            name='mail',
        ),
        migrations.AddField(
            model_name='establishment',
            name='wface',
            field=models.URLField(blank=True, null=True, verbose_name='Фейсбук'),
        ),
        migrations.AddField(
            model_name='establishment',
            name='wtic',
            field=models.URLField(blank=True, null=True, verbose_name='Тик-ток'),
        ),
        migrations.AddField(
            model_name='establishment',
            name='wtwit',
            field=models.URLField(blank=True, null=True, verbose_name='Твиттер'),
        ),
        migrations.AlterField(
            model_name='event',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='api.establishment', verbose_name='Организатор'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='est',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='api.establishment', verbose_name='УО'),
        ),
    ]
