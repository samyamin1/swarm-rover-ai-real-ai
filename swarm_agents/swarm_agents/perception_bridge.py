#!/usr/bin/env python3
"""
Perception Bridge for AI Model Integration
Handles communication between agents and AI models (Ollama: Llava, Phi-3)
"""

import numpy as np
import json
import ollama
import os
from typing import Tuple

class PerceptionBridge:
    def __init__(self):
        # Initialize Ollama client
        ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
        print(f'ollama_host !!!!!!!!!!!!! {ollama_host}')
        self.ollama_client = ollama.Client(host=ollama_host)
        print(f'PerceptionBridge: Ollama client initialized with host: {ollama_host}')

        # Use only smollm:135m to avoid memory constraints
        self.model_name = "smollm:135m"
        self.check_ollama_models()
        
        print('Perception Bridge initialized')

    def check_ollama_models(self):
        try:
            models = self.ollama_client.list()
            available_models = [m['name'] for m in models['models']]
            if self.model_name not in available_models:
                print(f"PerceptionBridge: Ollama model '{self.model_name}' not found. Please ensure it's pulled.")
                print("Available models:", available_models)
        except Exception as e:
            print(f"PerceptionBridge: Could not connect to Ollama server or list models: {e}")
            print("PerceptionBridge: AI models will not function correctly without Ollama.")

    def process_perception_input(self, textual_scene_description: str) -> Tuple[str, str]:
        """Processes textual scene description to get VLM output and decision."""
        # Use single model for both VLM and decision making to avoid memory issues
        vlm_output = self.run_vision_language_model(textual_scene_description)
        decision = self.run_decision_making_model(vlm_output)
        
        return vlm_output, decision
        
    def run_vision_language_model(self, scene_description: str) -> str:
        """Uses smollm:135m for scene analysis."""
        prompt = f"Analyze this scene description for a search and rescue rover: {scene_description}. Provide a brief summary of what the rover sees."
        
        try:
            response = self.ollama_client.chat(model=self.model_name, messages=[
                {
                    'role': 'user',
                    'content': prompt,
                }
            ])
            vlm_text_output = response['message']['content']
            print(f"PerceptionBridge: Scene analysis: {vlm_text_output[:100]}...")
            return vlm_text_output
        except Exception as e:
            print(f"PerceptionBridge: Error with scene analysis: {e}")
            return "Error in scene analysis."
        
    def run_decision_making_model(self, vlm_output: str) -> str:
        """Uses smollm:135m for decision making with strict command format."""
        decision_prompt = f"""Based on this scene analysis: '{vlm_output}', respond with ONLY ONE of these exact commands:
- SEARCH_AREA (if no targets nearby)
- MOVE_TO_TARGET x,y (if target coordinates are known)
- REPORT_FINDING (if target is found)
- IDLE (if no action needed)

Respond with just the command, nothing else."""
        
        try:
            response = self.ollama_client.chat(model=self.model_name, messages=[
                {
                    'role': 'user',
                    'content': decision_prompt,
                }
            ])
            decision_text = response['message']['content'].strip()
            print(f"PerceptionBridge: Decision: {decision_text}")
            
            # Clean up the response to extract just the command
            decision_text = self._extract_command(decision_text)
            return decision_text
        except Exception as e:
            print(f"PerceptionBridge: Error with decision making: {e}")
            return "SEARCH_AREA"  # Default to search if error
    
    def _extract_command(self, response: str) -> str:
        """Extract the actual command from the AI response."""
        response = response.strip().upper()
        
        # Look for specific commands
        if "SEARCH_AREA" in response:
            return "SEARCH_AREA"
        elif "MOVE_TO_TARGET" in response:
            # Try to extract coordinates
            try:
                # Find the MOVE_TO_TARGET part and extract coordinates
                start = response.find("MOVE_TO_TARGET")
                if start != -1:
                    # Extract the command part
                    command_part = response[start:].split()[0]  # Get first word after MOVE_TO_TARGET
                    if "MOVE_TO_TARGET" in command_part:
                        return "SEARCH_AREA"  # Default to search if no coordinates
                    return command_part
            except:
                pass
            return "SEARCH_AREA"
        elif "REPORT_FINDING" in response:
            return "REPORT_FINDING"
        elif "IDLE" in response:
            return "IDLE"
        else:
            # Default to search if no clear command found
            return "SEARCH_AREA"

# This main block is for testing the PerceptionBridge in isolation if needed
if __name__ == '__main__':
    # Ensure Ollama server is running and models are pulled
    # docker-compose -f ../../docker-compose.yml up ollama
    # ollama pull smollm:135m

    pb = PerceptionBridge()
    test_scene = "There is a red square obstacle at (100, 100) and a green circle target at (250, 250)."
    vlm_out, decision_out = pb.process_perception_input(test_scene)
    print(f"\nFinal VLM Output: {vlm_out}")
    print(f"Final Decision: {decision_out}")