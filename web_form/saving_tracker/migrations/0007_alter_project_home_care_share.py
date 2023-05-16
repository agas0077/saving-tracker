# Generated by Django 4.2 on 2023-04-28 13:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saving_tracker', '0006_project_food_share_project_home_care_share_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='home_care_share',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Home Care, %'),
        ),
    ]
