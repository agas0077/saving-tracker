import pandas as pd

from django.core.management.base import BaseCommand

import saving_tracker.models as stm


class Command(BaseCommand):
    """ Пакетная загрузка данных в базу"""

    def handle(self, *args, **kwargs):
        try:
            print(self.load_models())
        except Exception as error:
            raise Exception(f'Ошибка загрузки {error}')

    def load_models(self):
        """
        Загружает стандартные списки в базу данных.
        Колонки - названия моделей
        """

        file_to_load = input('Path: ')
        df = pd.read_csv(file_to_load, delimiter=';')
        for name, model in stm.__dict__.items():
            if name in df.columns:
                s = df[~df[name].isnull()]
                for i, value in s[name].items():
                    try:
                        model.objects.create(title=value)
                    except:
                        continue
