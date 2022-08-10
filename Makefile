run-django:
	@cd django && python3 manage.py makemigrations \
		&& python3 manage.py migrate \
		&& python3 manage.py loaddata user company garden bed permissions coordinate \
		&& python3 manage.py runserver

run-celery:
	@cd django && celery -A restapi.tasks worker --loglevel=info

run-backend:
	@echo "###############"
	@echo "# Run backend #"
	@echo "###############"
	@make run-celery & make run-django

run-frontend:
	@echo "#######################"
	@echo "# Run vue in dev mode #"
	@echo "#######################"
	@cd vue && npm run dev

run-frontend-prod:
	@echo "#####################################"
	@echo "# Build and run vite for production #"
	@echo "#####################################"
	@cd vue && npm run build && npm run preview
