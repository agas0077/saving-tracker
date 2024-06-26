"""
Django settings for web_form project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# Standard Library
import os
from pathlib import Path

# Third Party Library
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "saving-tracker.andreicode.ru",
]
CSRF_TRUSTED_ORIGINS = [
    "https://saving-tracker.andreicode.ru",
]

AUTH_USER_MODEL = "users.user"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_tables2",
    "django_filters",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "bootstrap3",
    "users.apps.UsersConfig",
    "saving_tracker.apps.SavingTrackerConfig",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "web_form.middleware.login_required_middleware.LoginRequiredMiddleware",
]

ROOT_URLCONF = "web_form.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "web_form", "templates"),
            os.path.join(BASE_DIR, "users", "templates"),
            os.path.join(BASE_DIR, "saving_tracker", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "web_form.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE") or "django.db.backends.sqlite3",
        "NAME": os.getenv("DB_NAME") or BASE_DIR / "db.sqlite3",
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSOWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "web_form", "static"),
    os.path.join(BASE_DIR, "users", "static"),
    os.path.join(BASE_DIR, "saving_tracker", "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Login params
SOCIALACCOUNT_ENABLED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
USER_MODEL_USERNAME_FIELD = "email"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "APP": {
            "client_id": os.getenv("GOOGLE_CID"),
            "secret": os.getenv("GOOGLE_CSECRET"),
            "key": "",
        },
    }
}

LOGIN_URL = "users:login"
LOGIN_REDIRECT_URL = "users:index"
LOGOUT_REDIRECT_URL = "users:login"
OPEN_URLS = [
    "/login/",
    "/accounts/",
]

# Email params
SEND_EMAIL = os.getenv("SEND_EMAIL") == "True"
if SEND_EMAIL:
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL")
    DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
    EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
