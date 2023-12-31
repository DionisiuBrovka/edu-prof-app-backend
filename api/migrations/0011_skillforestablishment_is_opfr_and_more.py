# Generated by Django 4.2.7 on 2023-12-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_skillforestablishment_avd_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillforestablishment',
            name='is_opfr',
            field=models.BooleanField(default=False, verbose_name='Введется ли набор обучающихся с ОПФР'),
        ),
        migrations.AddField(
            model_name='skillforestablishment',
            name='opfr_qnic',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Особенности ОПФР'),
        ),
    ]
