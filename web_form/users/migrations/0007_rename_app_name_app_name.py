# Generated by Django 4.2 on 2023-04-25 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_app_description_app_link_alter_app_app_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='app_name',
            new_name='name',
        ),
    ]