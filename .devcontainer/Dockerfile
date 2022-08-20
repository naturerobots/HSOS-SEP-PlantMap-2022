FROM ubuntu:22.04

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends -y \
    bash-completion \
    build-essential \
    curl \
    git \
    sudo \
    ssh \
    vim \
    gcc \
    python3-pip \
    python3-dev \
    python3-tk \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    gpg \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

# Install pre-commit hooks to /root/.cache/pre-commit/
RUN pip3 install pre-commit \
    && apt-get update -qq && apt-get install -y -qq --no-install-recommends \
        ruby shellcheck \
        clang-format-11 \
    && rm -rf /var/lib/apt/lists/*

# Install Django dependencies
RUN pip3 install django==4.0.1 \
    djangorestframework==3.13.1 \
    django-cors-headers==3.12.0 \
    django-rest-knox==4.2.0 \
    Pillow==9.1.1 \
    psycopg2==2.9.3 \
    grpcio==1.46.1 \
    grpcio-tools==1.46.1 \
    tzdata==2022.1 \
    celery==5.2.6 \
    numpy==1.22.4 \
    scipy==1.8.1 \
    plyfile==0.7.4 \
    pymap3d==2.9.0

# Install npm 14.x
RUN curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash - \
        && apt-get update -qq && apt-get -qq install --no-install-recommends -y nodejs \
        && rm -rf /var/lib/apt/lists/*

# Install MkDocs
RUN pip3 install mkdocs mkdocs-material mkdocs-glightbox

# Add non root user
RUN useradd -u 1000 --create-home --shell /bin/bash docker && echo "docker:docker" | chpasswd && adduser docker sudo

RUN mkdir -p /home/docker/.vscode-server/extensions \
    && chown -R docker /home/docker/.vscode-server \
    && mkdir -p /workdir \
    && chown -R docker /workdir

# Run as user 'docker' after here
USER docker

ENV PYTHONPATH="/workdir/build/gRPC"

CMD while sleep 1000; do :; done
