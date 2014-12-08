## Project variables
##
WSGI_PORT?=8000
WSGI_ADDR?=127.0.0.1
ACTIVATE_SCRIPT=.env/bin/activate
SETTINGS_PROD?=project.settings.prod
SETTINGS_DEV?=project.settings.dev
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

## Main project targets
##

clean:
	find . -name "*.pyc" -exec rm -rf {} \;


dev:
	python manage.py runserver ${WSGI_ADDR}:${WSGI_PORT}


dev_ext:
	WSGI_ADDR=0.0.0.0 SETTINGS_DEV=${SETTINGS_PROD} make dev


run_gunicorn:
	test -d ${LOGDIR} || mkdir -p ${LOGDIR};            \
	test -d ${TMPDIR} || mkdir -p ${TMPDIR};            \
	. ${ACTIVATE_SCRIPT};                               \
	gunicorn                                            \
		--env=DJANGO_SETTINGS_MODULE=${SETTINGS_PROD}   \
		--pythonpath='src'                              \
		--bind=${WSGI_ADDR}:${WSGI_PORT}                \
		--log-level=${LOGLEVEL}                         \
		--log-file=${LOGFILE} 2>>${LOGFILE}             \
		--worker-tmp-dir=${TMPDIR}
		project.wsgi


restart_gunicorn:
	ps auxww |grep gunicorn |grep -v grep |grep -v make | awk '{ print $$2 }' | xargs kill -9


restart_uwsgi:
	ps auxww |grep uwsgi |grep -v grep |grep -v make | awk '{ print $$2 }' | xargs kill -9


shell:
	. ${ACTIVATE_SCRIPT}; \
	python manage.py shell --settings=${SETTINGS_PROD}


shell_dev:
	SETTINGS_PROD=${SETTINGS_DEV} make shell


## These targets are designed for template development and thus
## may be deleted in project

flake8:
	flake8 src/


build_package:
	FILENAME=django-project-template.tar.gz
	tar -zcf $FILENAME    \
		--exclude=.git              \
		--exclude=*.pyc             \
		--exclude=$FILENAME         \
		.
