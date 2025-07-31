#!/bin/bash

# Script to set up the development environment

echo "Setting up development environment..."

# Install pip if not already installed
if ! command -v pip &> /dev/null
then
    echo "pip not found, installing..."
    python3 -m ensurepip --default-pip
fi

# Install virtualenv if not already installed
if ! command -v virtualenv &> /dev/null
then
    echo "virtualenv not found, installing..."
    pip install virtualenv
fi

# Create a virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    virtualenv venv
fi

# Activate the virtual environment
source venv/bin/activate

echo "Installing Python dependencies..."
pip install -r requirements.txt

# Placeholder for ROS2 setup if needed outside Docker
# echo "Setting up ROS2 environment..."
# source /opt/ros/humble/setup.bash # Replace humble with your ROS2 distribution
# colcon build --packages-select swarm_agents
# source install/setup.bash

echo "Development environment setup complete. To activate, run: source venv/bin/activate"
