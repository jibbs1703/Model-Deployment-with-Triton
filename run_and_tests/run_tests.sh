#!/bin/sh

# Declare Default Variables
CONTAINER_NAME="triton_demo_container"

# Enter into Running Container
docker exec -it ${CONTAINER_NAME} bash

pytest tests/test_flatten_data.py