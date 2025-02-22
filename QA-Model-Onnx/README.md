# Model Serving in Triton via the ONNX Backend

In this project, a pre-trained ML Model is served using NVIDIA's Triton Inference Server. The model served is the
Question and Answer (QA) Model from Huggingface and is able to retrieve the answer to a question from a given text,
proving useful in searching for answers in a document or file. The project is served within a docker container
allowing for the setup to be hosted on any server/computer.

The setup can be deployed as a solution in a variety of industries such as the legal and healthcare industries.

## Handling Data Pre-Inference and Post-Inference

In production, data is sent to the model as a payload, already preprocessed and made fit for input into the model. Also,
the inference results from the model must be post-processed to make the inference results available and readable to users
who sent requests to the model.

In this project, the preprocessing involves extracting inputs from a json file and putting these inputs in a payload
to send to the model for inference. The modules `etl.py` and `triton.py` provide helper functions that help preprocess
the input data from its raw form into a form that can be passed into the trained model.

Also, after the model makes inference on the input data, the model inference results need to be processed once more.
The results of the model inference is parsed, and the needed parts are extracted from the parsed inference and then
saved in a format for the user to get back. The module `triton.py` provides the function that parses
the results of the model inference.


## How to Run Project

The project is run in a docker container, in a bid to avoid environment clashes that could occur. The Dockerfile
pulls the official Triton Inference Server image from NVIDIA’s NGC, helps in loading the model into the server and
provides the sample data for testing the inference server. It also downloads all dependencies and packages needed
to run the server.

If run properly, the server should make inference on 10 text samples and provide results in a dataframe saved to the
results directory as a json file. Another option is to persist the results folder between the host machine and the
docker container, allowing the model results to show up in the results folder of the local machine.

```commandline
git clone https://github.com/jibbs1703/Model-Deployment-with-Triton.git
cd  Model-Deployment-with-Triton/
cd  QA-Model-Onnx
```

```bash
chmod +x docker/build.sh
docker/build.sh

```

```bash
chmod +x docker/run.sh
docker/run.sh

```

```bash
chmod +x scripts/inference.sh
scripts/inference.sh
```

```bash
chmod +x scripts/tests.sh
scripts/tests.sh
```
