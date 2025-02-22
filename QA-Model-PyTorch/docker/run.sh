#!/bin/sh

# Declare Default Variables
IMAGE_NAME="triton"
IMAGE_VERSION="24.08"
CONTAINER_NAME="triton_container_pytorch"

# Run Docker Image in Interactive Mode and Expose Ports for Inference Server
docker run -i --rm \
  --name ${CONTAINER_NAME} \
  -p8000:8000 \
  -p8001:8001 \
  -p8002:8002 \
  ${IMAGE_NAME}:${IMAGE_VERSION}

# Check if the Container Started Successfully or Not
if [ $? -ne 0 ]; then
  echo "Docker run failed!"
  exit 1
fi
echo "Docker container started successfully."
