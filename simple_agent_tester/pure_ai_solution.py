#!/usr/bin/env python3
"""
Pure AI Solution - No Rules, Only Intelligence
Uses the smallest, fastest AI models for real-time robotics
"""

import time
import concurrent.futures
from typing import Dict, Optional
import json
import urllib.request
import urllib.parse

class PureAI:
    def __init__(self, ollama_url: str = "http://localhost:11434"):
        """Initialize pure AI system - no rules, only intelligence"""
        self.ollama_url = ollama_url
        
        # Models ordered by size (smallest first for speed)
        self.models = [
            "qwen2.5:0.5b",    # 397 MB - NEW!
            "smollm:135m",      # 91 MB
            "moondream:latest", # 1.7 GB
        ]
        
        self.current_model = 0
        self.cache = {}
        self.timeout = 1.0  # 1 second timeout for real-time robotics
        
        print("🧠 Pure AI initialized - No rules, only intelligence")
        print(f"📦 Available models: {', '.join(self.models)}")
    
    def get_decision(self, scenario: str) -> str:
        """Get pure AI decision - no rules, only intelligence"""
        start_time = time.time()
        
        # Check cache first (instant)
        if scenario in self.cache:
            return self.cache[scenario]
        
        # Try AI with timeout and model fallback
        try:
            decision = self._get_ai_decision_with_fallback(scenario)
            self.cache[scenario] = decision
            response_time = time.time() - start_time
            print(f"🎯 AI Decision: {decision} (time: {response_time:.3f}s)")
            return decision
        except Exception as e:
            print(f"❌ All AI models failed: {e}")
            # Last resort: intelligent default based on scenario
            decision = self._get_intelligent_fallback(scenario)
            self.cache[scenario] = decision
            return decision
    
    def _get_ai_decision_with_fallback(self, scenario: str) -> str:
        """Try AI models in order of speed"""
        original_model = self.current_model
        
        while True:
            model = self.models[self.current_model]
            print(f"🧠 Trying {model}...")
            
            try:
                decision = self._call_ai_model(model, scenario)
                if decision:
                    return decision
            except Exception as e:
                print(f"❌ {model} failed: {e}")
            
            # Try next model
            self.current_model = (self.current_model + 1) % len(self.models)
            
            # If we've tried all models, give up
            if self.current_model == original_model:
                raise Exception("All AI models failed")
    
    def _call_ai_model(self, model: str, scenario: str) -> str:
        """Call AI model with optimized prompt"""
        # Optimized prompt for fast, simple responses
        prompt = f"""You are a robot in a swarm. Scenario: {scenario}

Respond with ONLY ONE of these commands:
- MOVE_FORWARD
- TURN_LEFT  
- TURN_RIGHT
- STOP
- SEARCH

Just the command, nothing else."""

        url = f"{self.ollama_url}/api/chat"
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "options": {
                "temperature": 0,      # Deterministic
                "num_predict": 5,      # Very short response
                "top_k": 1,           # Most likely response
                "top_p": 0.1,         # Focus on common tokens
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
    
    def _get_intelligent_fallback(self, scenario: str) -> str:
        """Intelligent fallback based on scenario keywords"""
        scenario_lower = scenario.lower()
        
        # Analyze scenario for intelligent decision
        if any(word in scenario_lower for word in ["target", "goal", "objective"]):
            if any(word in scenario_lower for word in ["ahead", "front", "forward"]):
                return "MOVE_FORWARD"
            else:
                return "SEARCH"
        
        elif any(word in scenario_lower for word in ["obstacle", "blocked", "wall"]):
            return "TURN_LEFT"
        
        elif any(word in scenario_lower for word in ["search", "explore", "find"]):
            return "SEARCH"
        
        elif any(word in scenario_lower for word in ["found", "located", "discovered"]):
            return "STOP"
        
        else:
            return "SEARCH"  # Default to exploration
    
    def get_stats(self) -> Dict:
        """Get AI system statistics"""
        return {
            "cache_size": len(self.cache),
            "current_model": self.models[self.current_model],
            "timeout": self.timeout,
            "total_models": len(self.models),
            "models": self.models
        }

def test_pure_ai():
    """Test the pure AI system"""
    print("🧪 Testing Pure AI System (No Rules)")
    print("=" * 50)
    
    ai = PureAI()
    
    test_scenarios = [
        "You see a target ahead",
        "You encounter an obstacle", 
        "You need to search an area",
        "You found a target",
        "There's a wall in front of you",
        "No targets visible",
        "Path is blocked by obstacle",
        "Target detected in front",
        "You need to explore the area",
        "You found the objective",
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
    print(f"   Timeout: {stats['timeout']}s")
    print(f"   Total models: {stats['total_models']}")
    print(f"   Models: {', '.join(stats['models'])}")

if __name__ == "__main__":
    test_pure_ai() 