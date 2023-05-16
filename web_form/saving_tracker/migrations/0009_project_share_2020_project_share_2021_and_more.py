# Generated by Django 4.2 on 2023-04-28 14:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saving_tracker', '0008_alter_project_home_care_share'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='share_2020',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Доля 2020, kE'),
        ),
        migrations.AddField(
            model_name='project',
            name='share_2021',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Доля 2021, kE'),
        ),
        migrations.AddField(
            model_name='project',
            name='share_2022',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Доля 2022, kE'),
        ),
        migrations.AddField(
            model_name='project',
            name='share_2023',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Доля 2023, kE'),
        ),
        migrations.AddField(
            model_name='project',
            name='share_2024',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Доля 2024, kE'),
        ),
        migrations.AddField(
            model_name='project',
            name='share_2025',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Доля 2025, kE'),
        ),
        migrations.AddField(
            model_name='project',
            name='share_2026',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Доля 2026, kE'),
        ),
        migrations.AddField(
            model_name='project',
            name='share_2027',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Доля 2027, kE'),
        ),
    ]
