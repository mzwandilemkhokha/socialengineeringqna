#!/bin/bash

# Upgrade pip to specific version
pip install --upgrade pip==25.0.1

# Install requirements
pip install -r requirements.txt

# Any other setup commands you need
echo "Environment setup complete"
