#!/bin/bash

FILENAME=django-project-template.tgz

tar -zcf django-project-template.tgz    \
    --exclude=.git                      \
    --exclude=*.pyc                     \
    --exclude=$FILENAME                 \
    --exclude=$0                        \
    .