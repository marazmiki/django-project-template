#!/bin/bash

FILENAME=django-project-template.tar.gz

tar -zcf $FILENAME              \
    --exclude=.git              \
    --exclude=*.pyc             \
    --exclude=$FILENAME         \
    --exclude=$0                \
    .