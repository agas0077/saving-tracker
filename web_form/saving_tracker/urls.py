# Third Party Library
from django.urls import path
from saving_tracker import views

app_name = "saving_tracker"

urlpatterns = [
    path("index/", views.ProjectListView.as_view(), name="index"),
    path("update_project/", views.update_project, name="update_project"),
    path("create_project/", views.create_project, name="create_project"),
    path(
        "download_table/",
        views.TableDownloadView.as_view(),
        name="download_table",
    ),
]
