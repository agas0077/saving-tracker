# Generated by Django 4.2 on 2023-04-28 13:37

# Third Party Library
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saving_tracker', '0007_alter_project_home_care_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='home_care_share',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='Home Care, %'),
        ),
    ]
