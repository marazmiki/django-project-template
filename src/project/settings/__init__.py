# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
import getpass
import os
import sys


def rel(*x):
    current_dir = os.path.dirname(__file__)
    project_dir = os.path.join(current_dir, '..', '..')
    return os.path.normpath(os.path.join(project_dir, *x))


def add_to_pythonpath(*args, **kwargs):
    position = kwargs.get('position', 0)
    for path in args:
        if path in sys.path:
            continue
        if position < 0:
            sys.path.append(path)
        else:
            sys.path.insert(position, path)


def get_secret_key(filename='secret_key.txt'):
    with open(rel(filename)) as fp:
        return fp.read()


add_to_pythonpath(
    rel('src/apps'),
    rel('src/project'),
)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)


BASE_DIR = rel('')
SECRET_KEY = get_secret_key()


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    rel('src/project/templates/'),
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



ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = rel('public/static')

MEDIA_URL = '/media/'
MEDIA_ROOT = rel('public/media')

EFFECTIVE_USER = getpass.getuser()
EFFECTIVE_GROUP = getpass.getuser()
