"""
Django settings for PSSProject project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z*2b)k5$n@3l__q60jg^lpz(yi1xdd5(p&mcv-e8j=64yll)pd"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["38.143.106.8", 'www.spgamerica.com', 'spgamerica.com']
# ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # "whitenoise.runserver_nostatic",  # changed
    # "captcha",
    "django.contrib.admin",
    "django_cleanup.apps.CleanupConfig",  # changed
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "PSSApp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",  # changed
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "PSSApp.custom_middleware.RemoveSlashMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "PSSProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "PSSProject.wsgi.application"

APPEND_SLASH = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "HOST": "localhost",
#         "NAME": "spgamerica",
#         "USER": "root",
#         "PASSWORD": "7a*x64JaRw69AMVw",
#     }
# }
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'USER': '',
            'PASSWORD': '',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',  
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,"static")]

STATIC_URL = "/static/"
#STATIC_ROOT = 'static'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]  # changed
# # STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # changed

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


EMAIL_HOST = "smtp.office365.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "noreply@spgamerica.com"
EMAIL_HOST_PASSWORD = "xat3uMo5E@ha"
EMAIL_USE_TLS = True

##old
# RECAPTCHA_PUBLIC_KEY = "6LcKKgAiAAAAACihLfAMobNdLZabLFVGu7kkMUqP"
# RECAPTCHA_PRIVATE_KEY = "6LcKKgAiAAAAALaH75ljfBphUmQEptWdbNIcm1k2"

RECAPTCHA_PUBLIC_KEY = "6LfmsQokAAAAANVOstG295SGeKlrgfeimO8ua8Hq"
RECAPTCHA_PRIVATE_KEY = "6LfmsQokAAAAAD4JdPNgD_PeX5dJyWwetbySgwqa"


RECAPTCHA_REUIRED_SCORE = 1
# RECAPTCHA_REUIRED_SCORE = 0.85
