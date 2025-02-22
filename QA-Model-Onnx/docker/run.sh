#!/bin/sh

# Declare Default Variables
IMAGE_NAME="triton"
IMAGE_VERSION="24.08"
CONTAINER_NAME="triton_container_onnx"

# Run Docker Image in Interactive Mode and Expose Ports
docker run -i --rm \
  --name ${CONTAINER_NAME} \
  -p8000:8000 \
  -p8001:8001 \
  -p8002:8002 \
  ${IMAGE_NAME}:${IMAGE_VERSION}
