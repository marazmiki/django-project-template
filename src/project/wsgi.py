# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
