#!/bin/sh

echo "Starting service in daemon mode..."
docker-compose -f ./docker-config/docker-compose.yml up -d --build --force python-playground

# docker rm -f python-playground