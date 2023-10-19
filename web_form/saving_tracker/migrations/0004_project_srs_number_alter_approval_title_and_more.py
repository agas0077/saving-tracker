# Generated by Django 4.2 on 2023-04-27 09:56

# Third Party Library
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saving_tracker', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='srs_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='SRS'),
        ),
        migrations.AlterField(
            model_name='approval',
            name='title',
            field=models.CharField(max_length=20, unique=True, verbose_name='A'),
        ),
        migrations.AlterField(
            model_name='businessarea',
            name='title',
            field=models.CharField(max_length=20, unique=True, verbose_name='Бизнес сегмент'),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='highlevelstatus',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Статус высокого уровня'),
        ),
        migrations.AlterField(
            model_name='lossesforattack',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='LFA'),
        ),
        migrations.AlterField(
            model_name='lowlevelstatus',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Статус низкого уровня'),
        ),
        migrations.AlterField(
            model_name='project',
            name='business_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to='saving_tracker.businessarea', verbose_name='Бизнес сегмент'),
        ),
        migrations.AlterField(
            model_name='project',
            name='coordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_coordinator', to=settings.AUTH_USER_MODEL, verbose_name='PC'),
        ),
        migrations.AlterField(
            model_name='project',
            name='folder_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на проект'),
        ),
        migrations.AlterField(
            model_name='project',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to='saving_tracker.group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='project',
            name='high_level_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to='saving_tracker.highlevelstatus', verbose_name='Статус высокого уровня'),
        ),
        migrations.AlterField(
            model_name='project',
            name='initial_start_date',
            field=models.DateField(verbose_name='Дата начала проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='local_focus',
            field=models.BooleanField(verbose_name='LF'),
        ),
        migrations.AlterField(
            model_name='project',
            name='losses_for_attack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to='saving_tracker.lossesforattack', verbose_name='LFA'),
        ),
        migrations.AlterField(
            model_name='project',
            name='low_level_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to='saving_tracker.lowlevelstatus', verbose_name='Статус низкого уровня'),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_owner', to=settings.AUTH_USER_MODEL, verbose_name='Владелец прокта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_end_date',
            field=models.DateField(verbose_name='Дата окончания проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='risk_adjustment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to='saving_tracker.riskadjustment', verbose_name='RA'),
        ),
        migrations.AlterField(
            model_name='project',
            name='saving_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to='saving_tracker.savingtype', verbose_name='Тип экономии'),
        ),
        migrations.AlterField(
            model_name='project',
            name='stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to='saving_tracker.stream', verbose_name='S'),
        ),
        migrations.AlterField(
            model_name='project',
            name='support_function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to='saving_tracker.supportfunction', verbose_name='Функция'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Проект'),
        ),
        migrations.AlterField(
            model_name='riskadjustment',
            name='title',
            field=models.CharField(max_length=20, unique=True, verbose_name='RA'),
        ),
        migrations.AlterField(
            model_name='savingtype',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Тип экономии'),
        ),
        migrations.AlterField(
            model_name='stream',
            name='title',
            field=models.CharField(max_length=20, unique=True, verbose_name='S'),
        ),
        migrations.AlterField(
            model_name='supportfunction',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Функция'),
        ),
    ]
