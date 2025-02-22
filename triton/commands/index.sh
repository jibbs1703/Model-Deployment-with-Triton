#!/bin/sh

# Send Request to Get Model Configuration
echo "Getting Model Configuration"
curl -v localhost:8000/v2/models/tinyroberta/config

# Send Request to Get Information about the Model Repository
echo "Getting Information about Model Repository"
curl -v localhost:8000/v2/models/tinyroberta

# For some reason, the code below does not return model repository information
echo "Getting Information about Model Repository"
curl -v localhost:8000/v2/repository/index
