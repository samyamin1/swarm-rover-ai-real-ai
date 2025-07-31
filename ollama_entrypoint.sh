#!/bin/bash

# Start Ollama server in the background
ollama serve &

# Wait for Ollama server to be ready
while ! curl -s http://localhost:11434 > /dev/null; do
  echo "Waiting for Ollama server to start..."
  sleep 5
done

echo "Ollama server is running. Pulling models..."

# Pull models until they are available
until ollama pull llava:7b; do
  echo "Failed to pull llava:7b, retrying in 10 seconds..."
  sleep 10
done

until ollama pull smollm:135m; do
  echo "Failed to pull smollm:135m, retrying in 10 seconds..."
  sleep 10
done

echo "Models pulled. Keeping container alive."

# Keep the container running
tail -f /dev/null