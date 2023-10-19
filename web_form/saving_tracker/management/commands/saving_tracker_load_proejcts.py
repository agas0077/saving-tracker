# Third Party Library
import pandas as pd
import saving_tracker.models as stm
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    """Пакетная загрузка данных в базу"""

    def handle(self, *args, **kwargs):
        try:
            print(self.load_projects())
        except Exception as error:
            raise Exception(f"Ошибка загрузки {error}")

    def load_projects(self):
        """Загружает данные в модель projects. Колонки = поля модели."""
        # file_to_load = input('Путь до файла: ')
        file_to_load = r"C:\Users\Andrei.Agasiants\Downloads\Book1.xlsx"
        df = pd.read_excel(file_to_load)
        df = df.fillna("")
        list_of_projects = []
        stm.Project.objects.all().delete()
        for index, row in df.iterrows():
            kwargs = {}
            for column in df.columns:
                obj = row[column]
                if column == "owner":
                    obj, created = User.objects.get_or_create(
                        email=row[column],
                        password="iohefoiawjdokwojqpd12312312312",
                    )
                elif column == "support_function":
                    obj, created = stm.SupportFunction.objects.get_or_create(
                        title=row[column],
                    )
                elif column == "saving_type":
                    obj, created = stm.SavingType.objects.get_or_create(
                        title=row[column],
                    )
                elif column == "high_level_status":
                    obj, created = stm.HighLevelStatus.objects.get_or_create(
                        title=row[column],
                    )
                elif column == "low_level_status":
                    obj, created = stm.LowLevelStatus.objects.get_or_create(
                        title=row[column],
                    )
                elif column == "coordinator":
                    obj, created = User.objects.get_or_create(
                        email=row[column],
                        password="iohefoiawjdokwojqpd12312312312",
                    )
                elif column == "group":
                    obj, created = stm.Group.objects.get_or_create(
                        title=row[column],
                    )
                elif column == "risk_adjustment":
                    obj, created = stm.RiskAdjustment.objects.get_or_create(
                        title=row[column],
                    )
                elif column == "losses_for_attack":
                    obj, created = stm.LossesForAttack.objects.get_or_create(
                        title=row[column],
                    )
                elif column == "business_area":
                    obj, created = stm.BusinessArea.objects.get_or_create(
                        title=row[column],
                    )
                elif column == "stream":
                    obj, created = stm.Stream.objects.get_or_create(
                        title=row[column],
                    )

                kwargs[column] = obj
            p = stm.Project(**kwargs)
            list_of_projects.append(p)
        stm.Project.objects.bulk_create(list_of_projects)
        return f"Загружено {len(list_of_projects)} проектов."
