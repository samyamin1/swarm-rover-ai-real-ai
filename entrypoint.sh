#!/bin/bash

# Start Ollama server in the background
ollama serve &

# Wait for Ollama server to be ready
while ! curl -s http://localhost:11434 > /dev/null; do
  echo "Waiting for Ollama server to start..."
  sleep 5
done

echo "Ollama server is running. Pulling models..."

# Pull models
ollama pull smollm:135m
ollama pull moondream:2

echo "Models pulled. Keeping container alive."

# Keep the container running
tail -f /dev/null