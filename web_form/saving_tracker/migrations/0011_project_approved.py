# Generated by Django 4.2 on 2023-05-03 13:12

# Third Party Library
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saving_tracker', '0010_alter_project_share_2020_alter_project_share_2021_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='approved',
            field=models.BooleanField(default=True, verbose_name='Согласовано'),
            preserve_default=False,
        ),
    ]
