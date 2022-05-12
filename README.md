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

### Example queries

#### seerep.MetaOperations.GetProjects

```json
{}
```

#### seerep.MetaOperations.GetProjectDetails

```json
{
  "projectuuid": "e1ef73b1258b475a996d2b72924c27ac"
}
```

#### seerep.TfService.GetFrames

```json
{
  "projectuuid": "e1ef73b1258b475a996d2b72924c27ac"
}
```

#### seerep.TfService.GetTransformStamped

```json
{
  "header": {
    "seq": 42,
    "stamp": "1970-01-01T00:02:03.000000123Z",
    "frameId": "map",
    "uuidProject": "e1ef73b1258b475a996d2b72924c27ac",
    "uuidMsgs": ""
  },
  "childFrameId": "ground"
}
```

#### seerep.PointCloudService.GetPointCloud2ByUUID

```json
{
  "projectuuid": "e1ef73b1258b475a996d2b72924c27ac",
  "geometryuuid": "0d927fa6b3534f9580d1db73d483b254"
}
```

#### seerep.PointCloudService.GetPointCloud2

```json
{
  "timeinterval": {
    "timeMin": "1626967568000000000",
    "timeMax": "1626967568000000000"
  },
  "label": [
    "e793d6a3f0af49f49e91d431e1b62b68",
    "8f460e87b27e4fb385e84f4a7dba677f"
  ],
  "projectuuid": "e1ef73b1258b475a996d2b72924c27ac"
}
```

#### seerep.MeasurementService.GetMeasurementByUUID

```json
{
  "projectuuid": "e1ef73b1258b475a996d2b72924c27ac",
  "geometryuuid": "25816c5842f14fe98b1ebc85a4908934"
}
```

#### seerep.MeasurementService.GetMeasurement

```json
{
  "timeinterval": {
    "timeMin": "1626967568000000000",
    "timeMax": "1626967568000000000"
  },
  "label": ["8f460e87b27e4fb385e84f4a7dba677f"],
  "projectuuid": "e1ef73b1258b475a996d2b72924c27ac"
}
```

#### seerep.LabelService.GetClass

```json
{
  "projectuuid": "e1ef73b1258b475a996d2b72924c27ac",
  "classuuid": "8f460e87b27e4fb385e84f4a7dba677f"
}
```

#### seerep.LabelService.GetInstance

```json
{
  "projectuuid": "e1ef73b1258b475a996d2b72924c27ac",
  "instanceuuid": "e793d6a3f0af49f49e91d431e1b62b68"
}
```

## Quality management

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
