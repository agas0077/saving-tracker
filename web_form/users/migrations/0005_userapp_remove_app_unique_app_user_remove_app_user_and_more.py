# Generated by Django 4.2 on 2023-04-25 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_app_unique_app_user_app_unique_app_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='app',
            name='unique_app_user',
        ),
        migrations.RemoveField(
            model_name='app',
            name='user',
        ),
        migrations.AddField(
            model_name='userapp',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_app_app', to='users.app'),
        ),
        migrations.AddField(
            model_name='userapp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_app_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='userapp',
            constraint=models.UniqueConstraint(fields=('app', 'user'), name='unique_app_user'),
        ),
    ]
