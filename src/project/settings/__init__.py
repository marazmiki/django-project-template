# coding: utf-8
# Django settings for {{ project_name }} project.

import os
import getpass


def rel(*x):
    x = ['..'] * 3 + list(x)
    return os.path.normpath(os.path.join(os.path.dirname(__file__), *x))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '{{ project_name }}',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

##
## Lozalization and internationalization
##
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'Asia/Novosibirsk'

##
## Handling static files settings
##
MEDIA_ROOT = rel('public/media/')
MEDIA_URL = '/media/'

STATIC_ROOT = rel('public/static/')
STATIC_URL = '/static/'


STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

##
## Templates settings
##
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    rel('src/project/templates/'),
)

##
## Project specified settings
##

SITE_ID = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

# List of callables that know how to import templates from various sources.

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'django_config_gen',
    'pipeline',
    'base',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

##
## The django-config-gen settings
##
CONFIG_GEN_GENERATED_DIR = rel('')
CONFIG_GEN_TEMPLATES_DIR = rel('src/project/templates/configs')


EFFECTIVE_USER = getpass.getuser()
EFFECTIVE_GROUP = getpass.getpass()


from settings.pipeline import *

try:
    from settings_local import *
except ImportError as e:
    pass
