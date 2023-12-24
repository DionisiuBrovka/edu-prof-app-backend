# Generated by Django 4.2.7 on 2023-12-24 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_skill_specialty_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='establishment',
            options={'ordering': ['-title'], 'verbose_name': 'Образовательное учреждение', 'verbose_name_plural': 'Образовательные учреждения'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-e_date'], 'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['q'], 'verbose_name': 'Вопрос - Ответ', 'verbose_name_plural': 'Вопрос - Ответ'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['title'], 'verbose_name': 'Квалификация', 'verbose_name_plural': 'Квалификации'},
        ),
        migrations.AlterModelOptions(
            name='specialty',
            options={'ordering': ['title'], 'verbose_name': 'Специальность', 'verbose_name_plural': 'Специальности'},
        ),
        migrations.AlterModelOptions(
            name='specialtygroup',
            options={'ordering': ['-title'], 'verbose_name': 'Группа специальностей', 'verbose_name_plural': 'Группы специальностей'},
        ),
        migrations.AlterField(
            model_name='skillforestablishment',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='svod', to='api.skill', verbose_name='Квалификация'),
        ),
    ]