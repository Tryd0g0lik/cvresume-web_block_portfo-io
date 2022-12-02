# Generated by Django 4.1.3 on 2022-12-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesmodel',
            name='public',
            field=models.TextField(choices=[('PUBLIC', 'Публикация'), ('NOPUBLIC', '----')], default='NOPUBLIC', help_text='Публикуем на странице или нет. По умолчанию, публикации нет', verbose_name='Публикация'),
        ),
    ]
