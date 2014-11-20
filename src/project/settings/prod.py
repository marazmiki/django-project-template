# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from project.settings import rel
import sys
import warnings


DEBUG = False
TEMPLATE_DEBUG = False


ALLOWED_HOSTS = [
    'example.com'
]


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


TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)


# Don't edit below this line
try:
    sys.path.insert(0, rel(''))
    from settings_local import *    # NOQA
except ImportError:
    warnings.warn("File settings_local.py.py not found")
else:
    sys.path = sys.path[1:]
