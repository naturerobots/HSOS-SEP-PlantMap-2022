run-server:
	@cd django && python3 manage.py runserver

run-celery:
	@cd django && celery -A rest-api.tasks worker --loglevel=info
