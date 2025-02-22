FROM nvcr.io/nvidia/tritonserver:24.08-py3 AS ngc

WORKDIR /deploy

COPY run.py .

COPY results results

COPY src src

COPY tests tests

COPY triton triton

# Pip Installs
RUN python3 -m pip install -U pandas pytest transformers "huggingface_hub[cli]" \
    && python3 -m pip install torch --index-url https://download.pytorch.org/whl/cpu

# Download dataset
RUN mkdir /deploy/dataset \
    && wget https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json -O /deploy/dataset/squadv2.json

# Download model
RUN huggingface-cli download deepset/tinyroberta-squad2 --local-dir /deploy/model
