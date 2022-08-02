run-server:
	@cd django && python3 manage.py runserver

run-celery:
	@cd django && celery -A restapi.tasks worker --loglevel=info

migrate:
	@cd django && python3 manage.py migrate

demo-post:
	@curl -X POST http://localhost:8000/beds/e1ef73b1258b475a996d2b72924c27ac/task

run-frontend:
	@cd vue && npm run dev

run-frontend-prod:
	@echo "#############################"
	@echo "# build vite for production #"
	@echo "#############################"
	@cd vue && npm run build
	@echo "##########################"
	@echo "# run vite in production #"
	@echo "##########################"
	@cd vue && npm run preview

start-mkdocs:
	@mkdocs serve

cleanup-docker:
	@echo "Warning: This command can only be used on the Host machine and the remote devcontainer connection by VS Code needs to be closed"
	@echo "shutdown production"
	@cd django && docker compose down
	@echo "shutdown development"
	@cd .devcontainer && docker compose down
	@echo "kill all exited containers"
	@-docker rm -f $(docker ps -qa --no-trunc --filter "status=exited")
	@echo "delete container systemwide"
	@docker system prune -a

potree-entwine-ept:
	@docker run -it -v `pwd`/django/storage/media/pointclouds/:/pointclouds/ connormanning/entwine build -c /pointclouds/config.json

potree-entwine-ept-bak:
	@docker run -it -v `pwd`/models/:/django/storage/media/pointclouds/ connormanning/entwine build \
    -i /pointclouds/las/0bf37a0851b7402d88674e153f58e6f8 - Cloud.las \
    -o /pointclouds \
	-r EPSG:4978 \
	--dataType binary
