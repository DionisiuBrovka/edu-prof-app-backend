# Generated by Django 4.2.7 on 2023-12-11 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_skillforestablishment'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillforestablishment',
            name='avd',
            field=models.FloatField(blank=True, null=True, verbose_name='Средний балл'),
        ),
        migrations.AddField(
            model_name='skillforestablishment',
            name='b_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество набора на бюджет'),
        ),
        migrations.AddField(
            model_name='skillforestablishment',
            name='b_long',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Продолжительность обучения на бюджете'),
        ),
        migrations.AddField(
            model_name='skillforestablishment',
            name='est',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='api.establishment', verbose_name='УО'),
        ),
        migrations.AddField(
            model_name='skillforestablishment',
            name='p_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество набора на платное'),
        ),
        migrations.AddField(
            model_name='skillforestablishment',
            name='p_long',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Продолжительность обучения на платном'),
        ),
        migrations.AddField(
            model_name='skillforestablishment',
            name='rule',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Правила набора'),
        ),
        migrations.AddField(
            model_name='skillforestablishment',
            name='s_type',
            field=models.CharField(choices=[('9', 'На основе общего базового образования (после 9 кл.)'), ('11', 'На основе общего среднего образования (после 11 кл.)'), ('ПТО', 'На основе ПТО')], default=1, max_length=3, verbose_name='На базе ...'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillforestablishment',
            name='skill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.specialty', verbose_name='Квалификация'),
            preserve_default=False,
        ),
    ]