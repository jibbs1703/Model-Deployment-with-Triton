#!/bin/sh

# Docker command goes here (tag=triton:24.08)

# Declare Default Variables
IMAGE_NAME="triton"
IMAGE_VERSION="24.08"
DOCKERFILE_PATH="docker/project.Dockerfile"

# Build Image Using Default Variables
docker build -f ${DOCKERFILE_PATH} -t ${IMAGE_NAME}:${IMAGE_VERSION} .

# Check if the Build was Successful or Not
if [ $? -eq 0 ]; then
    echo "Docker image ${IMAGE_NAME}:${IMAGE_VERSION} built successfully!"
else
    echo "Docker image build failed!"
    exit 1
fi
