# Serving AI/ML Models Using the Triton Inference Server

## Overview

NVIDIA's Triton Inference Server is designed to serve machine learning (ML) models in a scalable, efficient, 
and flexible manner, easing the need to redesign model serving or deployment systems every time models are 
deployed. It supports multiple frameworks, including TensorFlow, PyTorch, ONNX, TensorRT, and traditional ML 
models from Scikit-Learn, XGBoost and LightGBM . Triton is designed to handle high-performance inference 
workloads with features like dynamic batching, concurrent model serving, and advanced monitoring. Triton also 
provides HTTP and gRPC endpoints for communication, making it easy to integrate with various client applications.
The Triton Inference Server can be deployed on a single server, in a Docker container, or in a Kubernetes cluster,
offering flexibility in deployment environments. A detailed article on the triton server can be found [here](https://developer.nvidia.com/blog/deploying-ai-deep-learning-models-with-triton-inference-server/).

In this project, a pre-trained ML Model is served using NVIDIA's Triton Inference Server. The model served is the
Question and Answer (QA) Model from Huggingface and is able to retrieve the answer to a question from a given text,
proving useful in searching for answers in a document or file. The project is served within a docker container 
allowing for the setup to be hosted on any server/computer.

The setup can be deployed as a solution in a variety of industries such as the legal and healthcare industries. 

## Using Models in the Triton Inference Server

In production, the models to be served should have been trained and tested by Data Scientists and deemed to be ready
for real-world deployments. The trained model is loaded into the server along with its configuration file which 
outlines the model’s settings, including inputs, outputs, batch size, and other operational details that Triton 
requires to serve the model. The default name of the configuration file is [config.pbtxt](triton/model-repo/tinyroberta/1/config.pbtxt), 
and making changes to the model configuration without updating the Triton server configuration will cause the
Triton Inference Server to fail since the model and server configurations do not match. 

The model directory structure is such that the parent file is named "model-repo" with several models being hosted 
under this directory. Under each model directory in the parent directory, several versions of each model can exist
and can be used for inference, provided the Inference endpoint is directed to the model version. 

In this project, the pretrained model is called "tinyroberta" and has just one version loaded into the "model-repo". 
Also, each model version has its own configuration and backend which must be specified in its configuration file. 
Similar to the configuration, making changes to the model backend without updating the Triton server configuration 
will cause the Triton Inference Server to fail since the model backend and server configurations do not match. The 
backend used in this project is the ONNX backend and the model configuration files have been written to match the 
input and output preferences of the ONNX backend. 

![Model Repository Structure](images/model-repo-structure.jpg)


## Handling Data Pre-Inference and Post-Inference 

In production, data is sent to the model as a payload, already preprocessed and made fit for input into the model. Also, 
the inference results from the model must be post-processed to make the inference results available and readable to users
who sent requests to the model.

In this project, the preprocessing involves extracting inputs from a json file and putting these inputs in a payload
to send to the model for inference. The modules [etl.py](src/etl.py) and [triton.py](src/triton.py) provide functions
that help preprocess the input data from its raw form into a form that can be passed into the trained model. 

Also, after the model makes inference on the input data, the model inference results need to be processed once more. 
The results of the model inference is parsed, and the needed parts are extracted from the parsed inference and then
saved in a format for the user to get back. The module [triton.py](src/triton.py) provides the function that parses
the results of the model inference.


## How to Run Project

The project is run in a docker container, in a bid to avoid environment clashes that could occur. The Dockerfile 
pulls the official Triton Inference Server image from NVIDIA’s NGC, helps in loading the model into the server and 
provides the sample data for testing the inference server. It also downloads all dependencies and packages needed 
to run the server.

If run properly, the server should make inference on 10 text samples and provide results in a dataframe saved to the
results directory as a json file. 

git clone https://github.com/jibbs1703/Model-Deployment-with-Triton.git
cd  Model-Deployment-with-Triton/

chmod +x docker/build_image.sh
docker/build_image.sh

chmod +x docker/run_container.sh
docker/run_container.sh

chmod +x run_and_tests/run_inference.sh
run_and_tests/run_inference.sh

chmod +x run_and_tests/run_tests.sh
run_and_tests/run_tests.sh

