#!/bin/bash

echo "Delete containers"
docker rm -f $(docker ps -qa)

echo "Delete images"
docker rmi -f $(docker images -q)

echo "Delete Volume"
docker volume rm -f $(docker volume ls -q)