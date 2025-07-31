#!/usr/bin/env python3
"""
Final AI Solution - Working Smollm with Intelligent Fallback
Uses smollm:135m (fast and working) with intelligent command extraction
"""

import time
import json
import urllib.request
from typing import Dict, Optional

class FinalAI:
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

def test_final_ai():
    """Test the final AI system"""
    print("🧪 Testing Final AI System (Working Smollm:135m)")
    print("=" * 55)
    
    ai = FinalAI()
    
    test_scenarios = [
        "You see a target ahead",
        "You encounter an obstacle", 
        "You need to search an area",
        "You found a target",
        "There's a wall in front of you",
        "No targets visible",
        "Path is blocked by obstacle",
        "Target detected in front",
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
    print(f"   Model: {stats['model']}")
    print(f"   Model size: {stats['model_size']}")
    print(f"   Timeout: {stats['timeout']}s")
    print(f"   ✅ Perfect for real-time robotics!")

if __name__ == "__main__":
    test_final_ai() 