# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from celery import Celery
from django.conf import settings
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


app = Celery('project')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
