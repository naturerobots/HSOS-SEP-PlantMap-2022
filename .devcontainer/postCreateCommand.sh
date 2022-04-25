#! /bin/bash

#copy vs code config to root
cp -r /home/docker/workspace/src/.devcontainer/.vscode/* /home/docker/workspace/src/.vscode/

#install pre-commit in the git repo
mkdir -p build/gRPC
cd /home/docker/workspace/src || exit 1
pre-commit install --install-hooks

#generate python classes from protobuf messages
python3 -m grpc_tools.protoc \
        -I=protobuf-msgs \
        --python_out=build/gRPC  \
        --grpc_python_out=build/gRPC \
        protobuf-msgs/*

cd frontend || exit 1
npm install
