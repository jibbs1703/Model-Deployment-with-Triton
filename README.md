# Serving AI/ML Models Using the Triton Inference Server

## Overview

NVIDIA's Triton Inference Server is designed to serve machine learning (ML) models in a scalable, efficient, 
and flexible manner, easing the need to redesign model serving or deployment systems every time models are 
deployed. It supports multiple frameworks, including TensorFlow, PyTorch, ONNX, TensorRT, and traditional ML 
models from Scikit-Learn, XGBoost and LightGBM . Triton is designed to handle high-performance inference 
workloads with features like dynamic batching, concurrent model serving, and advanced monitoring. Triton also 
provides HTTP and gRPC endpoints for communication, making it easy to integrate with various client applications.
The Triton Inference Server can be deployed on a single server, in a Docker container, or in a Kubernetes cluster,
offering flexibility in deployment environments.

In this project, a pre-trained ML Model is served using NVIDIA's Triton Inference Server. The model served is the
Question and Answer (QA) Model from Huggingface and is able to retrieve the answer to a question from a given text,
proving useful in searching for answers in a document or file. The project is served within a docker container 
allowing for the setup to be hosted on any server/computer.

The setup can be deployed as a solution in a variety of industries such as the legal and healthcare industries. 

## How to Run Project

git clone https://github.com/jibbs1703/Model-Deployment-with-Triton.git
cd  Model-Deployment-with-Triton/

chmod +x docker/build_image.sh
docker/build_image.sh

chmod +x docker/run_container.sh
docker/run_container.sh

chmod +x docker/run_inference.sh
docker/run_inference.sh

