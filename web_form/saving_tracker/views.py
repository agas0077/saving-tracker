# Standard Library
import datetime as dt

# Third Party Library
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from django_tables2.views import SingleTableMixin, SingleTableView
from saving_tracker.filers import ProjectIndexFilter
from saving_tracker.forms import ProjectForm
from saving_tracker.models import DATE_FIELDS, Project
from saving_tracker.tables import DownloadTable, ProjectTable

DATE_FROMAT = "%Y-%m-%d"
DROPDWON_MENU_NAME, DROPDOWN_MENU = "dropdown_menu", (
    ("Все приложения", reverse_lazy("users:index")),
    ("Все проекты", reverse_lazy("saving_tracker:index")),
    ("Создать проект", reverse_lazy("saving_tracker:create_project")),
)


def _convert_date(request_copy):
    """
    Получает на вход копию POST запроса.
    Возвращает datetime.
    Необходимо, так как html возвращает именно строку,
    которую не сохранить в БД.
    """
    for field in DATE_FIELDS:
        try:
            if isinstance(request_copy[field], str):
                request_copy[field] = dt.datetime.strptime(
                    request_copy[field], DATE_FROMAT
                )
        except KeyError:
            pass
        except ValueError:
            pass
    return request_copy


def _send_change_email(form):
    """
    Получет на вход форму, проверенную на валидность и наличие изменений.
    Отправляет письмо координатору с указанимее изменений в проекте.
    """
    if not settings.SEND_EMAIL:
        return

    # recepient_email = form.cleaned_data['coordinator'].email
    recepient_email = "andrei.agasiants@unilever-rus.ru"

    recepient_name = form.cleaned_data["coordinator"].name
    recepient_surname = form.cleaned_data["coordinator"].surname
    title = form.cleaned_data["title"]

    begining = (
        f"{recepient_name} {recepient_surname}, <br><br>"
        "Обратите внимение на изменение в проекте "
        f'"{title}". <br>'
        "Изменения были следующиие: <br>"
        '<ul class="list-group">'
    )
    for field in form.changed_data:
        to_be = form.cleaned_data[field]
        changed_value_string = (
            '<li class="list-group-item">'
            f"Поле {field}. "
            f"Новое значение - {to_be}"
        )
        begining = "".join([begining, changed_value_string])
    ending = "</ul>" "С уважением, <br>" "Команда Digital SC"

    html_string = "".join([begining, ending])
    topic = f'Saving Tracker - Изменение в проекте "{title}"'
    send_mail(
        topic,
        message=html_string,
        from_email=None,
        html_message=html_string,
        recipient_list=[
            recepient_email,
        ],
        fail_silently=True,
    )


class TableDownloadView(ExportMixin, SingleTableView):
    """Вью-класс скачивания таблицы."""

    table_class = DownloadTable
    model = Project


class ProjectListView(SingleTableMixin, FilterView):
    """Вью-класс основной страницы приложения"""

    model = Project
    table_class = ProjectTable
    template_name = "saving_tracker_index.html"
    filterset_class = ProjectIndexFilter

    def get_context_data(self, **kwargs):
        """Добавляет в контекст поля выпадающего меню и ссылки."""
        ctx = super().get_context_data(**kwargs)
        ctx[DROPDWON_MENU_NAME] = DROPDOWN_MENU

        project_status = ["Done", "On hold", "Cancel", "In progress"]
        for status in project_status:
            ctx[status.lower().replace(" ", "_")] = self.object_list.filter(
                high_level_status__title=status
            ).count()

        saving_types = ["Hard", "Soft", "Cost avoidance"]
        for saving in saving_types:
            filtered_queryset = self.object_list.filter(
                saving_type__title=saving
            )
            sum_queryset = filtered_queryset.aggregate(
                Sum("saving_potential")
            )["saving_potential__sum"]
            ctx[saving.lower().replace(" ", "_")] = round(
                sum_queryset if sum_queryset else 0, 1
            )

        return ctx


def create_project(request):
    """Вью-функция создания проекта."""
    form = ProjectForm(request.POST or None, files=request.FILES or None)
    template = "create_project.html"
    context = {
        "form": form,
        DROPDWON_MENU_NAME: DROPDOWN_MENU,
    }
    if not request.method == "POST":
        return render(request, template, context)

    project = request.POST.copy()
    project = _convert_date(project)
    form = ProjectForm(project or None)
    context["form"] = form

    if not form.is_valid():
        return render(request, template, context)

    form.save()
    return redirect("saving_tracker:index")


def update_project(request):
    """Вью-функция редактирования проекта."""
    project_obj = get_object_or_404(Project, pk=request.GET.get("id"))
    form = ProjectForm(instance=project_obj)
    template = "update_project.html"
    context = {
        "form": form,
        "project": project_obj,
        DROPDWON_MENU_NAME: DROPDOWN_MENU,
    }
    print(form["initial_start_date"].value())

    if request.method == "POST":
        project = request.POST.copy()

        project = _convert_date(project)

        changed_form = ProjectForm(project or None, instance=project_obj)

        if changed_form.is_valid():
            changed_form.save()

            if form.has_changed():
                _send_change_email(changed_form)

            return redirect("saving_tracker:index")
        context["form"] = changed_form
        return render(request, template, context)

    return render(request, template, context)
