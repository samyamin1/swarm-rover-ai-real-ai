#!/usr/bin/env python3
"""
Script to manage AI models via Ollama.
Models (llava, phi3) are pulled directly by the Ollama service.
"""

import os

MODEL_DIR = "./models/"

def main():
    os.makedirs(MODEL_DIR, exist_ok=True)
    print("Ollama models (llava, phi3) are managed and pulled by the Ollama Docker service.")
    print("Please ensure your docker-compose.yml is configured to pull these models.")
    print("No direct model downloads are performed by this script anymore.")

if __name__ == "__main__":
    main()