# Generated by Django 4.2.7 on 2023-12-11 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_event_desc_alter_gallery_est'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.specialtygroup', verbose_name='Группа специальностей'),
        ),
    ]
