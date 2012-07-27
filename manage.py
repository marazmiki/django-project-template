#!/usr/bin/env python
# coding: utf-8

import os
import sys


def get_cwd():
    return os.path.dirname(__file__)


def get_extra_dirs():
    return ['compat', 'apps', 'project', '']


def add_path(path):
    sys.path.insert(0, os.path.normpath(os.path.realpath(os.path.join(get_cwd(),'src', path))))

if __name__ == '__main__':
    for directory in get_extra_dirs():
        add_path(directory)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
