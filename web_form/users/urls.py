# Third Party Library
import django.contrib.auth.views as djviews
from django.urls import path
from users.views import AppListView

app_name = "users"

urlpatterns = [
    path(
        "login/",
        djviews.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path("logout/", djviews.LogoutView.as_view(), name="logout"),
    path("", AppListView.as_view(), name="index"),
]
