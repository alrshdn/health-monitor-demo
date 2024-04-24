#!/bin/sh

export MONGODB_VERSION=latest

docker stop mongodb && docker rm mongodb
docker run --network bridge-network --name mongodb mongodb/mongodb-community-server:$MONGODB_VERSION

