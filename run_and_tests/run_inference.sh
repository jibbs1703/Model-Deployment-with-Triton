#!/bin/sh

# Declare Default Variables
CONTAINER_NAME="triton_demo_container"

# Enter into Running Container
docker exec -it ${CONTAINER_NAME} bash

# Execute run.py to start server
python3 run.py