run-server:
	@cd django && python3 manage.py runserver

run-celery:
	@cd django && celery -A restapi.tasks worker --loglevel=info

migrate:
	@cd django && python3 manage.py migrate

demo-post:
	@curl -X POST http://localhost:8000/e1ef73b1258b475a996d2b72924c27ac/task

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
