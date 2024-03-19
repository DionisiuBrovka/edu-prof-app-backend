# Generated by Django 4.2.7 on 2024-03-10 07:36

import data.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название учреждения образования')),
                ('short_title', models.CharField(max_length=35, verbose_name='Сокращенное название')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('adress', models.CharField(max_length=255, verbose_name='Адрес')),
                ('tel', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта')),
                ('wsite', models.URLField(blank=True, null=True, verbose_name='Веб сайт')),
                ('wtel', models.URLField(blank=True, null=True, verbose_name='Телеграм')),
                ('wvk', models.URLField(blank=True, null=True, verbose_name='Вк')),
                ('winsta', models.URLField(blank=True, null=True, verbose_name='Инстаграм')),
                ('wface', models.URLField(blank=True, null=True, verbose_name='Фейсбук')),
                ('wtwit', models.URLField(blank=True, null=True, verbose_name='Твиттер')),
                ('wtic', models.URLField(blank=True, null=True, verbose_name='Тик-ток')),
                ('wother', models.URLField(blank=True, null=True, verbose_name='Прочее')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=data.models.establishmentWrapper, verbose_name='Логотип')),
                ('prev', models.ImageField(blank=True, null=True, upload_to=data.models.establishmentWrapper, verbose_name='Превью')),
                ('promo_medio', models.FileField(blank=True, null=True, upload_to=data.models.establishmentWrapper, verbose_name='Промо ролик')),
                ('coords', models.CharField(blank=True, max_length=255, null=True, verbose_name='Координаты на карте')),
            ],
            options={
                'verbose_name': 'Образовательное учреждение',
                'verbose_name_plural': 'Образовательные учреждения',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q', models.TextField(verbose_name='Вопрос')),
                ('a', models.TextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос - Ответ',
                'verbose_name_plural': 'Вопрос - Ответ',
                'ordering': ['q'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='Код')),
                ('title', models.CharField(max_length=255, verbose_name='Название квалификации')),
                ('searchtag', models.TextField(blank=True, null=True, verbose_name='Теги для поиска')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to=data.models.skillWrapper, verbose_name='Описание фото')),
            ],
            options={
                'verbose_name': 'Квалификация',
                'verbose_name_plural': 'Квалификации',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='SpecialtyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название группы специальностей')),
            ],
            options={
                'verbose_name': 'Группа специальностей',
                'verbose_name_plural': 'Группы специальностей',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='Код')),
                ('title', models.CharField(max_length=255, verbose_name='Название специальности')),
                ('c_type', models.CharField(choices=[('ССО', 'ССО'), ('ПТО', 'ПТО')], max_length=3, verbose_name='Тип')),
                ('prev', models.ImageField(blank=True, null=True, upload_to=data.models.specialtyWrapper, verbose_name='Превью')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='ИД иконки флаттер')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.specialtygroup', verbose_name='Группа специальностей')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='SkillForEstablishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_type', models.CharField(choices=[('9', 'На основе общего базового образования (после 9 кл.)'), ('11', 'На основе общего среднего образования (после 11 кл.)'), ('ПТО', 'На основе ПТО')], max_length=3, verbose_name='На базе ...')),
                ('b_count', models.IntegerField(blank=True, null=True, verbose_name='Количество набора на бюджет')),
                ('b_long', models.CharField(blank=True, max_length=255, null=True, verbose_name='Продолжительность обучения на бюджете')),
                ('b_avd', models.FloatField(blank=True, null=True, verbose_name='Средний балл бюджет')),
                ('p_count', models.IntegerField(blank=True, null=True, verbose_name='Количество набора на платное')),
                ('p_long', models.CharField(blank=True, max_length=255, null=True, verbose_name='Продолжительность обучения на платном')),
                ('p_avd', models.FloatField(blank=True, null=True, verbose_name='Средний балл платное')),
                ('rule', models.CharField(blank=True, max_length=255, null=True, verbose_name='Правила набора')),
                ('is_opfr', models.BooleanField(default=False, verbose_name='Введется ли набор обучающихся с ОПФР')),
                ('opfr_qnic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Особенности ОПФР')),
                ('est', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='data.establishment', verbose_name='УО')),
                ('skill', models.ManyToManyField(related_name='svod', to='data.skill', verbose_name='Квалификация')),
            ],
            options={
                'verbose_name': 'Сводная таблица',
                'verbose_name_plural': 'Сводная таблица',
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='data.specialty', verbose_name='Специальность'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=data.models.galleryWrapper, verbose_name='Превью')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('est', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='data.establishment', verbose_name='УО')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галереи',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_date', models.DateTimeField(verbose_name='Дата мероприятия')),
                ('title', models.CharField(max_length=255, verbose_name='Название мероприятия')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('prev', models.ImageField(blank=True, null=True, upload_to=data.models.eventWrapper, verbose_name='Превью')),
                ('e_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на страницу мероприятия')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='data.establishment', verbose_name='Организатор')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ['-e_date'],
            },
        ),
    ]