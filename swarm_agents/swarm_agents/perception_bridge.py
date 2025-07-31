#!/usr/bin/env python3
"""
Perception Bridge for AI Model Integration
Handles communication between agents and AI models (Ollama: smollm:135m)
"""

import numpy as np
import json
import time
import urllib.request
import os
from typing import Tuple, Dict

class FinalAI:
    """Working AI solution with smollm:135m - Fast and reliable"""
    def __init__(self, ollama_url: str = "http://localhost:11434"):
        """Initialize final AI system with working smollm:135m"""
        self.ollama_url = ollama_url
        self.model = "smollm:135m"  # Our working model
        self.cache = {}
        self.timeout = 3.0  # 3 second timeout for real-time robotics
        
        print("🎯 Final AI initialized - Working Smollm:135m")
        print(f"🤖 Model: {self.model}")
        print(f"⏱️  Timeout: {self.timeout}s")
        print(f"📊 Model size: 135M parameters (fast!)")
    
    def get_decision(self, scenario: str) -> str:
        """Get AI decision using intelligent fallback"""
        start_time = time.time()
        
        # Check cache first (instant)
        if scenario in self.cache:
            return self.cache[scenario]
        
        # Try AI with intelligent fallback
        try:
            decision = self._get_intelligent_decision(scenario)
            self.cache[scenario] = decision
            response_time = time.time() - start_time
            print(f"🎯 Decision: {decision} (time: {response_time:.3f}s)")
            return decision
        except Exception as e:
            print(f"❌ AI Error: {e}")
            # Use intelligent fallback
            decision = self._get_intelligent_fallback(scenario)
            self.cache[scenario] = decision
            return decision
    
    def _get_intelligent_decision(self, scenario: str) -> str:
        """Get decision using AI + intelligent analysis"""
        # First, try to get AI response
        try:
            response = self._call_ai_api(scenario)
            print(f"   📝 AI Response: '{response[:50]}...'")
            
            # Extract command from AI response
            command = self._extract_command_from_ai(response)
            if command != "SEARCH":  # If AI gave a specific command
                return command
                
        except Exception as e:
            print(f"   ⚠️  AI call failed: {e}")
        
        # Fallback to intelligent analysis
        return self._get_intelligent_fallback(scenario)
    
    def _call_ai_api(self, scenario: str) -> str:
        """Call AI with optimized parameters"""
        prompt = f"Scenario: {scenario}. Reply with ONLY: MOVE_FORWARD, TURN_LEFT, TURN_RIGHT, STOP, or SEARCH"
        
        url = f"{self.ollama_url}/api/chat"
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "options": {
                "temperature": 0,
                "num_predict": 5,
                "top_k": 1,
                "top_p": 0.1,
            }
        }
        
        json_data = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(
            url,
            data=json_data,
            headers={'Content-Type': 'application/json'}
        )
        
        with urllib.request.urlopen(req, timeout=self.timeout) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result["message"]["content"].strip()
    
    def _extract_command_from_ai(self, response: str) -> str:
        """Extract command from AI response"""
        valid_commands = ["MOVE_FORWARD", "TURN_LEFT", "TURN_RIGHT", "STOP", "SEARCH"]
        
        # Look for exact matches
        for cmd in valid_commands:
            if cmd in response.upper():
                return cmd
        
        # Look for partial matches
        for cmd in valid_commands:
            cmd_no_underscore = cmd.replace("_", " ")
            if cmd_no_underscore in response.upper():
                return cmd
        
        # Look for keywords in response
        if any(word in response.upper() for word in ["FORWARD", "AHEAD", "MOVE"]):
            return "MOVE_FORWARD"
        elif any(word in response.upper() for word in ["LEFT", "TURN"]):
            return "TURN_LEFT"
        elif any(word in response.upper() for word in ["RIGHT"]):
            return "TURN_RIGHT"
        elif any(word in response.upper() for word in ["STOP", "HALT", "END"]):
            return "STOP"
        
        return "SEARCH"  # Default
    
    def _get_intelligent_fallback(self, scenario: str) -> str:
        """Intelligent fallback based on scenario analysis"""
        scenario_lower = scenario.lower()
        
        # Target-related scenarios
        if any(word in scenario_lower for word in ["target", "goal", "objective"]):
            if any(word in scenario_lower for word in ["ahead", "front", "forward", "see"]):
                return "MOVE_FORWARD"
            elif any(word in scenario_lower for word in ["found", "located", "discovered"]):
                return "STOP"
            else:
                return "SEARCH"
        
        # Obstacle-related scenarios
        elif any(word in scenario_lower for word in ["obstacle", "blocked", "wall", "barrier"]):
            if any(word in scenario_lower for word in ["front", "ahead"]):
                return "TURN_LEFT"
            else:
                return "TURN_LEFT"
        
        # Search-related scenarios
        elif any(word in scenario_lower for word in ["search", "explore", "find", "look"]):
            return "SEARCH"
        
        # Movement scenarios
        elif any(word in scenario_lower for word in ["move", "go", "travel"]):
            if any(word in scenario_lower for word in ["forward", "ahead"]):
                return "MOVE_FORWARD"
            elif any(word in scenario_lower for word in ["left"]):
                return "TURN_LEFT"
            elif any(word in scenario_lower for word in ["right"]):
                return "TURN_RIGHT"
        
        # Default to search
        return "SEARCH"
    
    def get_stats(self) -> Dict:
        """Get AI system statistics"""
        return {
            "cache_size": len(self.cache),
            "model": self.model,
            "timeout": self.timeout,
            "model_size": "135M parameters"
        }

class PerceptionBridge:
    def __init__(self):
        """Initialize PerceptionBridge with working AI solution"""
        # Initialize working AI system
        ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
        print(f'🎯 PerceptionBridge: Initializing with Ollama host: {ollama_host}')
        
        self.ai_system = FinalAI(ollama_url=ollama_host)
        print('✅ PerceptionBridge: Working AI system initialized')
        
        # Command mapping for swarm compatibility
        self.command_mapping = {
            "MOVE_FORWARD": "MOVE_FORWARD",
            "TURN_LEFT": "TURN_LEFT", 
            "TURN_RIGHT": "TURN_RIGHT",
            "STOP": "STOP",
            "SEARCH": "SEARCH_AREA"
        }
        
        print('🚀 PerceptionBridge: Ready for swarm robotics!')

    def process_perception_input(self, textual_scene_description: str) -> Tuple[str, str]:
        """Processes textual scene description to get VLM output and decision."""
        print(f"🔍 Processing scene: {textual_scene_description[:50]}...")
        
        # Get AI decision using our working solution
        decision = self.ai_system.get_decision(textual_scene_description)
        
        # Map decision to swarm-compatible command
        swarm_command = self.command_mapping.get(decision, "SEARCH_AREA")
        
        # Create VLM output for compatibility
        vlm_output = f"Scene analysis: {textual_scene_description}. AI decision: {decision}"
        
        print(f"🎯 AI Decision: {decision} → Swarm Command: {swarm_command}")
        
        return vlm_output, swarm_command
        
    def run_vision_language_model(self, scene_description: str) -> str:
        """Uses working AI system for scene analysis."""
        print(f"🔍 VLM Analysis: {scene_description[:50]}...")
        
        # Get AI decision and create scene analysis
        decision = self.ai_system.get_decision(scene_description)
        vlm_output = f"Scene: {scene_description}. Analysis: {decision} action recommended."
        
        print(f"📝 VLM Output: {vlm_output}")
        return vlm_output
        
    def run_decision_making_model(self, vlm_output: str) -> str:
        """Uses working AI system for decision making."""
        print(f"🤖 Decision Making: {vlm_output[:50]}...")
        
        # Extract scenario from VLM output and get decision
        scenario = vlm_output.replace("Scene: ", "").replace(". Analysis: ", " → ")
        decision = self.ai_system.get_decision(scenario)
        
        # Map to swarm-compatible command
        swarm_command = self.command_mapping.get(decision, "SEARCH_AREA")
        
        print(f"🎯 Decision: {decision} → Swarm Command: {swarm_command}")
        return swarm_command
    
    def _extract_command(self, response: str) -> str:
        """Extract the actual command from the AI response."""
        # Use our working AI system's command extraction
        return self.ai_system._extract_command_from_ai(response)
    
    def get_ai_stats(self) -> Dict:
        """Get AI system statistics"""
        return self.ai_system.get_stats()

# This main block is for testing the PerceptionBridge in isolation if needed
if __name__ == '__main__':
    print("🧪 Testing Integrated PerceptionBridge")
    print("=" * 50)
    
    pb = PerceptionBridge()
    
    test_scenarios = [
        "There is a red square obstacle at (100, 100) and a green circle target at (250, 250).",
        "You see a target ahead",
        "You encounter an obstacle", 
        "You need to search an area",
        "You found a target",
    ]
    
    for i, scenario in enumerate(test_scenarios):
        print(f"\n{i+1}. Testing: {scenario}")
        vlm_out, decision_out = pb.process_perception_input(scenario)
        print(f"   VLM Output: {vlm_out}")
        print(f"   Decision: {decision_out}")
    
    stats = pb.get_ai_stats()
    print(f"\n📊 AI Statistics:")
    print(f"   Cache size: {stats['cache_size']}")
    print(f"   Model: {stats['model']}")
    print(f"   Model size: {stats['model_size']}")
    print(f"   Timeout: {stats['timeout']}s")
    print(f"   ✅ Ready for swarm integration!")