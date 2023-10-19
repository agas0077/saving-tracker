# Third Party Library
from django.views.generic import ListView
from users.models import App

# Create your views here.


class AppListView(ListView):
    """Вью-класс страницы с выбором доступных пользователю приложений."""

    template_name = "users_index.html"
    model = App

    def get_queryset(self):
        queryset = App.objects.filter(user_app_app__user=self.request.user.pk)
        print(queryset)
        return queryset
