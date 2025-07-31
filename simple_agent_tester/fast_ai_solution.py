#!/usr/bin/env python3
"""
Fast AI Solution - Direct Ollama Calls
Uses subprocess to call ollama directly, avoiding API timeout issues
"""

import time
import subprocess
import json
from typing import Dict, Optional

class FastAI:
    def __init__(self):
        """Initialize fast AI system using direct ollama calls"""
        self.models = [
            "qwen2.5:0.5b",    # 397 MB - Fast and working!
            "smollm:135m",      # 91 MB
        ]
        self.current_model = 0
        self.cache = {}
        self.timeout = 20.0  # 20 second timeout for testing
        
        print("🚀 Fast AI initialized - Direct ollama calls")
        print(f"📦 Available models: {', '.join(self.models)}")
        print(f"⏱️  Timeout: {self.timeout} seconds")
    
    def get_decision(self, scenario: str) -> str:
        """Get AI decision using direct ollama calls"""
        start_time = time.time()
        
        # Check cache first (instant)
        if scenario in self.cache:
            return self.cache[scenario]
        
        # Try AI with direct ollama call
        try:
            decision = self._call_ollama_direct(scenario)
            self.cache[scenario] = decision
            response_time = time.time() - start_time
            print(f"🎯 AI Decision: {decision} (time: {response_time:.3f}s)")
            return decision
        except Exception as e:
            print(f"❌ AI Error: {e}")
            # Try next model
            self.current_model = (self.current_model + 1) % len(self.models)
            if self.current_model == 0:  # Tried all models
                return "SEARCH"  # Final fallback
            return self.get_decision(scenario)  # Retry with next model
    
    def _call_ollama_direct(self, scenario: str) -> str:
        """Call ollama directly using subprocess"""
        model = self.models[self.current_model]
        
        # Optimized prompt for fast response
        prompt = f"Scenario: {scenario}. Reply with ONLY: MOVE_FORWARD, TURN_LEFT, TURN_RIGHT, STOP, or SEARCH"
        
        try:
            # Call ollama directly with longer timeout
            result = subprocess.run([
                "docker", "exec", "swarm_rover_ai_real_ai-ollama-1", 
                "ollama", "run", model, prompt
            ], capture_output=True, text=True, timeout=self.timeout)
            
            if result.returncode == 0:
                response = result.stdout.strip()
                return self._extract_command(response)
            else:
                raise Exception(f"Ollama error: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            raise Exception(f"Timeout on {model} after {self.timeout}s")
        except Exception as e:
            raise Exception(f"Subprocess error: {e}")
    
    def _extract_command(self, response: str) -> str:
        """Extract command from AI response"""
        valid_commands = ["MOVE_FORWARD", "TURN_LEFT", "TURN_RIGHT", "STOP", "SEARCH"]
        
        # Look for exact matches
        for cmd in valid_commands:
            if cmd in response.upper():
                return cmd
        
        # Look for partial matches
        for cmd in valid_commands:
            if cmd.replace("_", " ") in response.upper():
                return cmd
        
        return "SEARCH"  # Default
    
    def get_stats(self) -> Dict:
        """Get AI system statistics"""
        return {
            "cache_size": len(self.cache),
            "current_model": self.models[self.current_model],
            "total_models": len(self.models),
            "models": self.models,
            "timeout": self.timeout
        }

def test_fast_ai():
    """Test the fast AI system"""
    print("🧪 Testing Fast AI System (Direct Ollama Calls)")
    print("=" * 55)
    
    ai = FastAI()
    
    test_scenarios = [
        "You see a target ahead",
        "You encounter an obstacle", 
        "You need to search an area",
        "You found a target",
        "There's a wall in front of you",
        "No targets visible",
    ]
    
    print("\n📋 Testing scenarios:")
    for i, scenario in enumerate(test_scenarios):
        start_time = time.time()
        decision = ai.get_decision(scenario)
        response_time = time.time() - start_time
        
        print(f"{i+1}. {scenario}")
        print(f"   Decision: {decision} ({response_time:.3f}s)")
    
    stats = ai.get_stats()
    print(f"\n📊 Statistics:")
    print(f"   Cache size: {stats['cache_size']}")
    print(f"   Current model: {stats['current_model']}")
    print(f"   Total models: {stats['total_models']}")
    print(f"   Models: {', '.join(stats['models'])}")
    print(f"   Timeout: {stats['timeout']}s")

if __name__ == "__main__":
    test_fast_ai() 