from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.urls import reverse


class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер user model, который использует поле email в качестве
    уникального идентификатора, вместо username.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Создает и сохранеяет объект пользователя с email и password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создает и сохранеяет объект супер-пользователя с email и password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя"""

    USERNAME_FIELD = 'email'
    username = None
    objects = CustomUserManager()

    email = models.EmailField('Email', max_length=254, unique=True)

    name = models.CharField('Имя пользователя', max_length=100)
    surname = models.CharField('Фамилия пользователя', max_length=100)

    is_staff = models.BooleanField(
        'Статус администратора',
        default=False,
        help_text='Определяет есть ли у пользователя досутп к адиминке.',
    )
    is_superuser = models.BooleanField(
        'Статус супер-пользователя',
        default=False,
    )

    def save(self, *args, **kwargs):
        self.name, self.surname = self._get_name_and_surname()
        return super().save(*args, **kwargs)

    def _get_name_and_surname(self):
        name_point_surname = self.email.split('@')[0]
        try:
            name, surname = name_point_surname.split('.')
        except ValueError:
            name = name_point_surname
            surname = 'no surname'
        name = name.capitalize()
        surname = surname.capitalize()
        return (name, surname)

    def __str__(self):
        if self.surname == 'no surname':
            return self.email
        return f'{self.name} {self.surname}'


class App(models.Model):
    """
    Моедль существующих приложений.
    """
    title = models.CharField(
        'Имя приложения', max_length=200)
    description = models.TextField('Описание приложения', blank=True,
                                   null=True)
    app_name = models.CharField('Namespace из web_form.urls',
                                default='users',
                                max_length=300)

    def get_absolute_url(self):
        return reverse(f'{self.app_name}:index')

    def __str__(self):
        return self.title


class UserApp(models.Model):
    """
    Модель связи пользователь-приложение для определения прав
    доступа к приложениям.
    Содержит только уникальные записи.
    """
    app = models.ForeignKey(App, on_delete=models.CASCADE,
                            related_name='user_app_app')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_app_user')

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=['app', 'user'],
                name='unique_app_user'
            ),
        )
