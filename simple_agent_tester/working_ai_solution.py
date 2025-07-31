#!/usr/bin/env python3
"""
Working AI Solution - Optimized API Calls
Uses smollm:135m with optimized API parameters for fast, simple responses
"""

import time
import json
import urllib.request
from typing import Dict, Optional

class WorkingAI:
    def __init__(self, ollama_url: str = "http://localhost:11434"):
        """Initialize working AI system with optimized API calls"""
        self.ollama_url = ollama_url
        self.model = "smollm:135m"  # Our working model
        self.cache = {}
        self.timeout = 5.0  # 5 second timeout
        
        print("🚀 Working AI initialized - Optimized API calls")
        print(f"🤖 Model: {self.model}")
        print(f"⏱️  Timeout: {self.timeout}s")
    
    def get_decision(self, scenario: str) -> str:
        """Get AI decision using optimized API calls"""
        start_time = time.time()
        
        # Check cache first (instant)
        if scenario in self.cache:
            return self.cache[scenario]
        
        # Try AI with optimized API call
        try:
            decision = self._call_ai_api(scenario)
            self.cache[scenario] = decision
            response_time = time.time() - start_time
            print(f"🎯 AI Decision: {decision} (time: {response_time:.3f}s)")
            return decision
        except Exception as e:
            print(f"❌ AI Error: {e}")
            # Use intelligent fallback
            decision = self._get_intelligent_fallback(scenario)
            self.cache[scenario] = decision
            return decision
    
    def _call_ai_api(self, scenario: str) -> str:
        """Call AI with optimized API parameters"""
        # Optimized prompt for simple responses
        prompt = f"Scenario: {scenario}. Reply with ONLY: MOVE_FORWARD, TURN_LEFT, TURN_RIGHT, STOP, or SEARCH"
        
        url = f"{self.ollama_url}/api/chat"
        data = {
            "model": self.model,
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
            response_text = result["message"]["content"].strip()
            
            # Extract command from response
            command = self._extract_command(response_text)
            print(f"   📝 Raw response: '{response_text[:50]}...'")
            print(f"   🎯 Extracted command: {command}")
            
            return command
    
    def _extract_command(self, response: str) -> str:
        """Extract command from AI response"""
        valid_commands = ["MOVE_FORWARD", "TURN_LEFT", "TURN_RIGHT", "STOP", "SEARCH"]
        
        # Look for exact matches first
        for cmd in valid_commands:
            if cmd in response.upper():
                return cmd
        
        # Look for partial matches (without underscore)
        for cmd in valid_commands:
            cmd_no_underscore = cmd.replace("_", " ")
            if cmd_no_underscore in response.upper():
                return cmd
        
        # Look for partial matches (without spaces)
        for cmd in valid_commands:
            cmd_no_spaces = cmd.replace("_", "")
            if cmd_no_spaces in response.upper():
                return cmd
        
        # Look for individual words
        response_words = response.upper().split()
        for cmd in valid_commands:
            cmd_words = cmd.replace("_", " ").split()
            if all(word in response_words for word in cmd_words):
                return cmd
        
        # If no command found, use intelligent fallback based on response content
        if any(word in response.upper() for word in ["FORWARD", "AHEAD", "MOVE"]):
            return "MOVE_FORWARD"
        elif any(word in response.upper() for word in ["LEFT", "TURN"]):
            return "TURN_LEFT"
        elif any(word in response.upper() for word in ["RIGHT"]):
            return "TURN_RIGHT"
        elif any(word in response.upper() for word in ["STOP", "HALT", "END"]):
            return "STOP"
        else:
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
            "model": self.model,
            "timeout": self.timeout
        }

def test_working_ai():
    """Test the working AI system"""
    print("🧪 Testing Working AI System (Optimized API)")
    print("=" * 50)
    
    ai = WorkingAI()
    
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
    print(f"   Model: {stats['model']}")
    print(f"   Timeout: {stats['timeout']}s")

if __name__ == "__main__":
    test_working_ai() 