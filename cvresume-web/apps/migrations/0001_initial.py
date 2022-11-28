# Generated by Django 4.1.3 on 2022-11-28 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginning_data', models.DateField(help_text='Начало работы в должности', verbose_name='Начало работы')),
                ('complated_data', models.DateField(blank=True, help_text='Окончание работы')),
            ],
            options={
                'verbose_name': 'Дата обучения',
                'verbose_name_plural': 'Сроки обучения',
            },
        ),
        migrations.CreateModel(
            name='PicturiesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(height_field='Height', max_length=80, upload_to='files/pictures/%Y/%m/%d/', width_field='Width')),
                ('date_created', models.DateTimeField(help_text='Дата загрузки')),
            ],
            options={
                'verbose_name': 'Путь к img',
                'verbose_name_plural': 'Путь к изображениям',
            },
        ),
        migrations.CreateModel(
            name='WorkExperienceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginning_data', models.DateField(help_text='Дата начала обучения', verbose_name='Начало обучения')),
                ('complated_data', models.DateField(blank=True, help_text='Дата окончания обучения', verbose_name='Окончание учёбы')),
                ('preview_text', models.TextField(blank=True, help_text='Превью описание', max_length=100)),
            ],
            options={
                'verbose_name': 'Дата работы',
                'verbose_name_plural': 'Опыт работ',
            },
        ),
        migrations.CreateModel(
            name='PagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(choices=[('ARTICLE', 'Запись'), ('PAGE', 'Страница')], default='PAGE', verbose_name='Тип страницы')),
                ('title', models.TextField(max_length=70, null=True)),
                ('preview_text', models.TextField(blank=True, help_text='Краткое описание не более 50 символов', verbose_name='Краткое описание')),
                ('description', models.CharField(blank=True, max_length=2000, verbose_name='Содержание')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Создана')),
                ('date_change', models.DateTimeField(auto_now_add=True, verbose_name='Отредактирована')),
                ('from_menu', models.BooleanField(null=True, verbose_name='Указать в меню')),
                ('creator', models.ForeignKey(help_text='Пользователь создал', on_delete=django.db.models.deletion.CASCADE, related_name='correctUser', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': ('Страница',),
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_page', models.TextField(choices=[('PARENTS', 'Родительский'), ('CHILDE', 'Дочернеий')], default='PARENTS')),
                ('id_pages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagesChild', to='apps.pagesmodel')),
                ('id_parents_pages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagesParent', to='apps.pagesmodel')),
            ],
            options={
                'verbose_name': 'Заголовок',
                'verbose_name_plural': 'Заголовки страницы',
            },
        ),
    ]
