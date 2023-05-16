from django.urls import reverse
from django.utils.html import format_html
import django_tables2 as tables

from saving_tracker.models import Project


class ProjectTable(tables.Table):
    '''Настройки основной таблице приложения.'''
    class Meta:
        model = Project
        fields = (
            'pk', 'title', 'owner', 'support_function',
            'initial_start_date', 'planned_start_date',
            'saving_potential', 'saving_type', 'high_level_status',
            'comment', 'approved',
        )
        attrs = {"class": "table table-striped table-hover table-bordered"}
        per_page = 10
        order_by = ('-pk')

    def render_title(self, record):
        '''
        Пересоздает столбец с названиями,
        так чтобы названия были сслыками на редактирование.
        '''
        url = reverse('saving_tracker:update_project')
        string = f'<a href="{url}?id={record.id}">{record.title}</a>'
        return format_html(string)

    def render_pk(self, record):
        '''
        Пересоздает столбец с индексом,
        так чтобы рядом с индексом была иконка.
        '''
        status = record.high_level_status.title
        div_start = '<div class="d-flex flex-nowrap align-items-center">'
        div_end = f'{record.pk}</div>'
        string = '<i class="fa {} {} me-1" aria-hidden="true"></i>'
        if status == 'Done':
            string = string.format('fa-check', 'text-success')
        elif status == 'On hold':
            string = string.format('fa-pause', 'text-warning')
        elif status == 'In progress':
            string = string.format('fa-play', 'text-primary')
        elif status == 'Cancel':
            string = string.format('fa-stop', 'text-danger')
        string = ''.join([div_start, string, div_end])
        return format_html(string)


class DownloadTable(tables.Table):
    '''Настройки таблицы, которая скачивается по нажатию кнопки.'''
    class Meta:
        model = Project

    def render_primary_share(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.primary_share * record.saving_potential
        return value

    def render_secondary_share(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.secondary_share * record.saving_potential
        return value

    def render_warehouse_share(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.warehouse_share * record.saving_potential
        return value

    def render_personal_care_share(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.personal_care_share * record.saving_potential
        return value

    def render_home_care_share(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.home_care_share * record.saving_potential
        return value

    def render_tea_share(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.tea_share * record.saving_potential
        return value

    def render_food_share(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.food_share * record.saving_potential
        return value

    def render_ic_share(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.ic_share * record.saving_potential
        return value

    def render_share_2020(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.share_2020 * record.saving_potential
        return value

    def render_share_2021(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.share_2021 * record.saving_potential
        return value

    def render_share_2022(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.share_2022 * record.saving_potential
        return value

    def render_share_2023(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.share_2023 * record.saving_potential
        return value

    def render_share_2024(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.share_2024 * record.saving_potential
        return value

    def render_share_2025(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.share_2025 * record.saving_potential
        return value

    def render_share_2026(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.share_2026 * record.saving_potential
        return value

    def render_share_2027(self, record):
        '''Заменяет долю на фактическое значение.'''
        value = record.share_2027 * record.saving_potential
        return value
