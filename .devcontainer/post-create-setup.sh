#! /bin/bash

# Install pre-commit in the git repository
pre-commit install --install-hooks
pre-commit install --hook-type commit-msg

# Generate python classes from protobuf messages
mkdir -p build/gRPC
python3 -m grpc_tools.protoc \
        -I=protobuf-msgs \
        --python_out=build/gRPC  \
        --grpc_python_out=build/gRPC \
        protobuf-msgs/*

# Create storage folders
mkdir -p django/storage/logs
mkdir -p django/storage/images

# Install npm dependencies from package-lock.json
cd vue  && npm ci
