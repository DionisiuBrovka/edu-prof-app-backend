# Generated by Django 4.2.7 on 2023-12-11 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_skillforestablishment_is_opfr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='est',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='api.establishment', verbose_name='УО'),
        ),
    ]
