#!/bin/bash

check_pypiserver_installed() {
    if ! command -v pypi-server &> /dev/null; then
        echo "pypiserver is not installed. Installing now..."
        pip install pypiserver
    else
        echo "pypiserver is already installed."
    fi
}

check_pypiserver_installed

ADDRESS="0.0.0.0"
PORT="8888"
PACKAGE_DIR="local_pypi_packages"

if [ ! -z "$1" ]; then
    ADDRESS=$1
fi
if [ ! -z "$2" ]; then
    PORT=$2
fi
if [ ! -z "$3" ]; then
    PACKAGE_DIR=$3
fi

PACKAGE_DIR_PATH="$HOME/$PACKAGE_DIR"

if [ ! -d "$PACKAGE_DIR_PATH" ]; then
    echo "Creating package directory at $PACKAGE_DIR_PATH"
    mkdir -p "$PACKAGE_DIR_PATH"
else
    echo "Package directory $PACKAGE_DIR_PATH already exists, skipping creation."
fi

echo "Starting pypiserver on $ADDRESS:$PORT using package directory $PACKAGE_DIR_PATH"
pypi-server -p $PORT -i $ADDRESS "$PACKAGE_DIR_PATH" -P . -a .
