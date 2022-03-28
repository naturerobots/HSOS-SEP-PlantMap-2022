#! /bin/bash

#copy vs code config to root
cp -r /home/docker/workspace/src/.devcontainer/.vscode/* /home/docker/workspace/.vscode/

#build the workspace 
#TODO

#install pre-commit in the git repo
cd /home/docker/workspace/src || exit 1
pre-commit install --install-hooks
