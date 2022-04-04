# README

## Quick Start

### VS Code Devcontainer

1. Clone this repo and open it in VS Code.
2. Install the extensions `ms-vscode-remote.remote-containers` and `ms-azuretools.vscode-docker`.
3. Press `F1` or `CTRL + SHIFT + P` and enter `Remote-Containers: Reopen Folder in Container`
4. This creates a docker container based on
   [ghcr.io/naturerobots/hsos-sep-plant-map-2022:main](https://github.com/naturerobots/HSOS-SEP-PlantMap-2022/pkgs/container/hsos-sep-plant-map-2022),
   installs all necessary VS Code extensions, builds the workspace a first time, sets up
   Intellisense, installs the [pre-commit](#precommit) hooks and opens it in VS Code.

   Use `pre-commit run -a` in the workspace folder to check the code style before commiting. In the Docker image the
   pre-commit checks are installed in the git so a commit is just possible if the checks succeed.

5. default user: `docker` with password: `docker`

### Login to GitHub Container Registry

Login to the GitHub Container Docker Registry with `docker login ghrc.io`

If you have enabled 2-factor authentication, create an access token, see [https://github.com/settings/tokens](https://github.com/settings/tokens)

Use your generated token and the `ghcr.io` container registry as follows:

```bash
docker login ghcr.io -u USERNAME --password YOUR_TOKEN
```

or

```bash
export CR_PAT=YOUR_TOKEN
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
```

Try to pull the docker image manually: `docker pull ghcr.io/naturerobots/hsos-sep-plant-map-2022:latest`

## Pre-Commit Formatting Checks

This repo has a [pre-commit](https://pre-commit.com/) check that runs in CI. You can use this locally and set it up to
run automatically before you commit something. In the devcontainer it is already pre-installed. To install, use pip:

```bash
pip3 install --user pre-commit
```

To run over all the files in the repo manually:

```bash
pre-commit run -a
```

To run pre-commit automatically before committing in the local repo, install the git hooks (run it in the repo folder):

```bash
pre-commit install
```

## SEEREP instance

In order to provide you spatial, temporal and semantical information about gardens, we host a public SEEREP instance.
This instance is available under `https://seerep.naturerobots.de` and can be queried using a gRPC interface in
combination with Protobuf messages. All required protofiles (with inline documentation) are located in the the folder
[seerep-protos](seerep-protos).

If you like to get an overview of the API before using it in your code, we recomment the free tool [Kreya](https://kreya.app/).
Just add a Kreya project, import the protos from the seerep-protos directory and add the endpoint `https://seerep.naturerobots.de`
in the project settings and you are ready to try the API.
