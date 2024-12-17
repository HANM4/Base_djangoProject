"""
Django settings for baseProjectRename project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# _ENV shows whether a file with configuration keys exists in the derektory.
# _ENV == True , uses keys from the local.env file
# _ENV == False , uses keys from the system environment
if os.path.exists(str(BASE_DIR / "local.env")):
    _LOCAL_ENV = True
else:
    _LOCAL_ENV = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if _LOCAL_ENV:
    SECRET_KEY = config("SECRET_KEY", default="", cast=str)
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = ['django',]

if _LOCAL_ENV:
    DEBUG = config("DEBUG", default="", cast=str)
    ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="", cast=lambda v: [s for s in v.split(';')])
else:
    DEBUG = os.environ.get('DEBUG')
    ALLOWED_HOSTS = [s for s in os.environ.get('ALLOWED_HOSTS').split(";")]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'baseProjectRename.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'baseProjectRename.wsgi.application'

#CSRF
CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if _LOCAL_ENV:
    DATABASES = {
        'default': {
            'ENGINE': config("ENGINE", default="", cast=str),
            'NAME': config("NAME", default="", cast=str),
            'USER': config("USER", default="", cast=str),
            'PASSWORD': config("PASSWORD", default="", cast=str),
            'HOST': config("HOST", default="", cast=str),
            'PORT': config("PORT", default="", cast=str),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('ENGINE'),
            'NAME': os.environ.get('NAME'),
            'USER': os.environ.get('USER'),
            'PASSWORD': os.environ.get('PASSWORD'),
            'HOST': os.environ.get('HOST'),
            'PORT': os.environ.get('PORT'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATICFILES_DIRS = [
    BASE_DIR / "baseProject" / "static",
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Add project-wide static files directory
# https://docs.djangoproject.com/en/5.0/ref/settings/#media-root

MEDIA_URL = "media/"
MEDIA_ROOT = str(BASE_DIR.parent / "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if _LOCAL_ENV:
    INTERNAL_IPS = config("INTERNAL_IPS", default="", cast=lambda v: [s for s in v.split(';')])
else:
    INTERNAL_IPS = [s for s in os.environ.get('INTERNAL_IPS').split(';')]
