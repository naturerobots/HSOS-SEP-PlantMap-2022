run-django:
	@cd django && python3 manage.py makemigrations \
		&& python3 manage.py migrate \
		&& python3 manage.py loaddata user company garden permissions \
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

clean-docker-setup:
	@echo "#########################"
	@echo "# Clearing docker setup #"
	@echo "#########################"
	@echo "Shutdown development: "
	@cd .devcontainer && docker compose down
	@echo "Deleting Containers: "
	@docker rm hsos-sep-plantmap-2022_devcontainer-postgres-1 \
		hsos-sep-plantmap-2022_devcontainer-rabbitmq-1 \
		hsos-sep-plantmap-2022_devcontainer-plant-map-dev-1
	@echo "Deleting Images: "
	@docker rmi postgres:latest \
		rabbitmq:latest \
		hsos-sep-plantmap-2022_devcontainer_plant-map-dev:latest \
		vsc-hsos-sep-plantmap-2022-e203421f68d810d8e4b8972a3b2f3674-uid:latest
	@echo "Deleting ALL volumes: "
	@docker volume prune -f
