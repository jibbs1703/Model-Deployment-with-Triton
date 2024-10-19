FROM nvcr.io/nvidia/tritonserver:24.08-py3 AS ngc

WORKDIR /deploy

COPY run.py .

COPY results results

COPY src src

COPY tests tests

COPY triton triton