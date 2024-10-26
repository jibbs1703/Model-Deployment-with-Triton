#!/bin/sh

# Retrieve Model Statistics from Triton
echo "Retrieve Model Statistics"
curl -v localhost:8000/v2/models/tinyroberta/versions/1/stats

# Retrieve Model Metrics from Triton
echo "Retrieve Model Metrics"
curl -v localhost:8002/metrics