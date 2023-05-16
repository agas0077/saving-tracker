from django_filters import FilterSet

from saving_tracker.models import Project


class ProjectIndexFilter(FilterSet):
    '''
    Фильтр главной таблицы приложения.
    Каждое новое поле в fields добавляет блок ввода в шаблоне.
    '''
    class Meta:
        model = Project
        fields = {"title": ["contains"]}
