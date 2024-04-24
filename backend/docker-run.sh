#!/bin/sh

docker run -p 5000:5000 --name web --network bridge-network -it web 
