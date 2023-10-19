# Third Party Library
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import App, User, UserApp


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("name", "surname")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    exclude = (
        "username",
        "last_name",
        "date_joined",
        "is_active",
        "first_name",
    )
    list_display = ("email", "name", "surname", "is_staff")
    search_fields = ("name", "surname", "email")
    list_filter = ("is_staff", "groups")
    ordering = None
    list_display = ("email", "name", "surname")
    empty_value_display = "-пусто-"


class AppAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "app_name",
    )
    empty_value_display = "-пусто-"


class UserAppAdmin(admin.ModelAdmin):
    empty_value_display = "-пусто-"
    list_display = (
        "user",
        "app",
    )
    list_filter = ("user__email", "app__title")


admin.site.register(User, UserAdmin)
admin.site.register(App, AppAdmin)
admin.site.register(UserApp, UserAppAdmin)
