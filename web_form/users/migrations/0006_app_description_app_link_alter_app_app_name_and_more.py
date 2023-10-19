# Generated by Django 4.2 on 2023-04-25 20:08

# Third Party Library
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userapp_remove_app_unique_app_user_remove_app_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание приложения'),
        ),
        migrations.AddField(
            model_name='app',
            name='link',
            field=models.CharField(default='users:index', max_length=300, verbose_name='Ссылка на приложение в формате Django'),
        ),
        migrations.AlterField(
            model_name='app',
            name='app_name',
            field=models.CharField(max_length=200, verbose_name='Имя приложения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Определяет есть ли у пользователя досутп к адиминке.', verbose_name='Статус администратора'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Статус супер-пользователя'),
        ),
    ]
