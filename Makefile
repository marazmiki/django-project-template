WSGI_PORT?=8000
WSGI_ADDR?=127.0.0.1
ACTIVATE_SCRIPT=.env/bin/activate


dev:
	. ${ACTIVATE_SCRIPT}; \
	python manage.py runserver ${WSGI_ADDR}:${WSGI_PORT}


dev_ext:
	WSGI_ADDR=0.0.0.0 make dev
