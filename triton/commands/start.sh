#!/bin/sh

tritonserver --model-repository triton/model-repo --strict-readiness true --exit-on-error true &