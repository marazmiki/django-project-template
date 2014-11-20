# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from project.settings import *    # NOQA
import sys
import warnings


DEBUG = True
TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': rel('db.sqlite3'),
    }
}


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


# Don't edit below this line
try:
    sys.path.insert(0, rel(''))
    from settings_local import *    # NOQA
except ImportError:
    warnings.warn("File settings_local.py.py not found")
else:
    sys.path = sys.path[1:]
