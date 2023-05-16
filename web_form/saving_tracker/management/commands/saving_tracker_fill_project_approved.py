import pandas as pd

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import saving_tracker.models as stm

User = get_user_model()


class Command(BaseCommand):
    '''Пакетная загрузка данных в базу'''

    def handle(self, *args, **kwargs):
        try:
            print(self.fill_approved())
        except Exception as error:
            raise Exception(f'Ошибка загрузки {error}')

    def fill_approved(self):
        '''Заполнят колонку approved на основе условия'''
        projects = stm.Project.objects.all()
        for project in projects:
            print(type(project.saving_potential))
            if project.saving_potential >= 40:
                project.approved = False
            else:
                project.approved = True
            project.save()
        return f'Загружено {len(projects)} проектов.'
