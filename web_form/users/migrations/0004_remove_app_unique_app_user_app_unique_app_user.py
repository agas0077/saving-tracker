# Generated by Django 4.2 on 2023-04-25 14:23

# Third Party Library
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_app_app_app_name_alter_app_user'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='app',
            name='unique_app_user',
        ),
        migrations.AddConstraint(
            model_name='app',
            constraint=models.UniqueConstraint(fields=('app_name', 'user'), name='unique_app_user'),
        ),
    ]
