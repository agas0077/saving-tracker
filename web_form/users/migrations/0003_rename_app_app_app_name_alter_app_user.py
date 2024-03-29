# Generated by Django 4.2 on 2023-04-25 14:22

# Third Party Library
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_app_unique_app_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='app',
            new_name='app_name',
        ),
        migrations.AlterField(
            model_name='app',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app_users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
