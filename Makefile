DJANGO_CMD=python manage.py

runserver:
	${DJANGO_CMD} runserver

makemigrations:
	${DJANGO_CMD} makemigrations

migrate:
	${DJANGO_CMD} migrate

createsuperuser:
	${DJANGO_CMD} createsuperuser

shell:
	${DJANGO_CMD} shell_plus
