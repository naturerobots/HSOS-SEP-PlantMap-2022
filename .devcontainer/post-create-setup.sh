#! /bin/bash

#install pre-commit in the git repo
pre-commit install --install-hooks

#generate python classes from protobuf messages
mkdir -p build/gRPC
python3 -m grpc_tools.protoc \
        -I=protobuf-msgs \
        --python_out=build/gRPC  \
        --grpc_python_out=build/gRPC \
        protobuf-msgs/*

# use npm ci to install all exact verion dependencies from package-lock.json
cd vue  && npm ci
