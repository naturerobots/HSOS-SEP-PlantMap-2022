# Installation

## Prerequisites

In order to use the application you need to install:

- [docker](https://docs.docker.com/engine/install/) >= 20.10.16
- [docker compose](https://docs.docker.com/compose/install/) >= 1.25.5
- [VSCode](https://code.visualstudio.com/download)

## VSCode Development Container

To use the application you need to setup the VSCode development container.

1. Clone this repository and open it in VS Code.

   ```sh
   git clone https://github.com/naturerobots/HSOS-SEP-PlantMap-2022.git
   cd HSOS-SEP-PlantMap-2022
   code .
   ```

2. Install the `ms-vscode-remote.remote-containers` and
   `ms-azuretools.vscode-docker` extensions.

   ```sh
   code --install-extension ms-vscode-remote.remote-containers
   code --install-extension ms-azuretools.vscode-docker
   ```

3. Press `F1` or `CTRL+SHIFT+P` and enter `Remote-Containers: Reopen Folder in Container`

   This downloads a docker container for the development of the PlantMap application and
   starts the needed [PostgreSQL](https://www.postgresql.org/) and RabbitMQ. Additionally
   all necessary VS Code extensions and npm packages from the `package.json` are
   installed. Further git pre-commit hooks are set up.
   If you have trouble downloading the container see the [GitHub Container Registry](#github-container-registry) section.

   In case you need to use sudo in the container, the default user is:

   ```text
   user: `docker`
   password: `docker`
   ```

## GitHub Container Registry

The docker image is published to the
GitHub Container Registry. In order to download it, you first need to log in
with your GitHub credentials.

If you have enabled 2-factor authentication, please create an access token [here](https://github.com/settings/tokens).

Use your password or generated token and username to login to the `ghcr.io` container registry as
follows:

```bash
docker login ghcr.io -u USERNAME --password PASSWORD/TOKEN
```

Now you call pull the image with `docker pull` or by simply simply following the steps in the [previous section](#vscode-development-container).

## Running the application

Once you are in the [VSCode Development Container](#vscode-development-container),
the application can be started using convenient make commands.

To start the backend server run:

```sh
make run-backend
```

Once it's running, the backend's REST-Api will by available on port 8000.

To start the frontend website run:

```sh
make run-frontend
```

The frontend runs on port 3000 and is accessible by
opening [http://localhost:3000](http://localhost:3000) in a browser.
Keep in mind that the frontend needs the backend running to work properly.
For information on how to use the application, see [Tutorials](tutorials.md).
