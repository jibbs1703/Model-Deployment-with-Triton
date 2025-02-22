#!/bin/sh

# Declare Default Variables
CONTAINER_NAME="triton_container_onnx"

# Enter into Running Container and Execute run.py to Use Model on Payload
docker exec -it ${CONTAINER_NAME} bash  -c "python3 run.py"
