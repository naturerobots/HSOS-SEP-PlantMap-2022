FROM ubuntu:20.04

WORKDIR /PlantMap

RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends -y \
    bash-completion \
        curl \
        git \
        sudo \
        ssh \
        vim \
        gcc \
        python3-pip \
        python3-dev \
        libpq-dev \
        gpg \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

RUN apt-get update -qq && apt-get install -y -qq --no-install-recommends \
    ruby shellcheck \
    clang-format-10 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pre-commit

####################################################
# Install django
####################################################
RUN pip3 install django==4.0 djangorestframework django-cors-headers psycopg2==2.9.3

####################################################
# Install python gRPC
####################################################
RUN pip3 install grpcio grpcio-tools

####################################################
# Install npm 14.x
####################################################
RUN curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash - \
        && apt-get update -qq && apt-get -qq install --no-install-recommends -y nodejs \
        && rm -rf /var/lib/apt/lists/*

####################################################
# Install frontend dependencies
####################################################
RUN npm install -g create-vue

RUN useradd -u 1001 --create-home --shell /bin/bash docker && echo "docker:docker" | chpasswd && adduser docker sudo

RUN mkdir -p /home/docker/.vscode-server/extensions \
    && chown -R docker /home/docker/.vscode-server \
    && mkdir -p /PlantMap \
    && chown -R docker /PlantMap

ENTRYPOINT [ "/bin/sh", "-c", "while sleep 1000; do :; done" ]
