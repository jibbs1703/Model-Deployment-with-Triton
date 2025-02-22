#!/bin/sh

# Declare Default Variables
CONTAINER_NAME="triton_container_pytorch"

# Enter into Running Container and Perform Pytest
docker exec -it ${CONTAINER_NAME} bash -c "pytest tests/test_flatten_data.py"
