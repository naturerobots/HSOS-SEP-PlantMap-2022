#! /bin/bash

echo '#enable noninteractive installs'
export DEBIAN_FRONTEND="noninteractive"

echo '#install other required tools'
apt-get -qq update && apt-get -qq install -y -o=Dpkg::Use-Pty=0 \
        bash-completion \
        curl \
        git \
        sudo \
        ssh \
        vim \
        gpg

echo '# install pre-commit hooks to /root/.cache/pre-commit/'
apt-get update -qq && apt-get install -y -qq --no-install-recommends \
    git \
    python3-pip \
    ruby shellcheck \
    clang-format-10 \
    python3-catkin-lint

pip3 install --upgrade pip
pip3 install pre-commit

echo '####################################################'
echo '#install django'
echo '####################################################'
pip3 install django==4.0 djangorestframework django-cors-headers

echo '####################################################'
echo '#install python grpc'
echo '####################################################'
pip3 install grpcio grpcio-tools

# remove apt lists so that they are not saved in the image layers
rm -rf /var/lib/apt/lists/*
