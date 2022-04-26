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

#####*FRONTEND*#####
echo '####################################################'
echo '#install npm'
echo '####################################################'
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
apt-get update -q && apt install nodejs -y

echo '####################################################'
echo '#install create-vue'
echo '####################################################'
npm install -g create-vue


echo '####################################################'
echo '#install axios'
echo '####################################################'
npm install --save axios
npm install --save vue-axios

echo '####################################################'
echo '#install leaflet'
echo '####################################################'
npm i leaflet
npm i @types/leaflet

echo '####################################################'
echo '#install fortawesome'
echo '####################################################'
npm i --save @fortawesome/fontawesome-svg-core
npm i --save @fortawesome/free-solid-svg-icons
npm i --save @fortawesome/vue-fontawesome@prerelease

echo '####################################################'
echo '#install tailwindcss'
echo '####################################################'
npm i tailwindcss postcss autoprefixer

echo '####################################################'
echo '#install daisyui'
echo '####################################################'
npm i daisyui

# remove apt lists so that they are not saved in the image layers
rm -rf /var/lib/apt/lists/*
