#!/usr/bin/env python3
"""
Optimized AI System - Fast AI with Fallbacks
Uses existing models with proper optimizations for real-time robotics
"""

import time
import asyncio
import concurrent.futures
from typing import Dict, Optional
import json
import urllib.request
import urllib.parse

class OptimizedAI:
    def __init__(self, ollama_url: str = "http://localhost:11434"):
        """Initialize optimized AI system"""
        self.ollama_url = ollama_url
        self.models = ["smollm:135m", "moondream:latest"]  # Available models
        self.current_model = 0
        self.cache = {}
        self.timeout = 2.0  # 2 second timeout for robotics
        
        # Simple rules for instant fallback
        self.fallback_rules = {
            "target ahead": "MOVE_FORWARD",
            "target found": "STOP", 
            "obstacle": "TURN_LEFT",
            "wall": "TURN_RIGHT",
            "search": "SEARCH",
            "no target": "SEARCH",
        }
        
        print("🤖 Optimized AI initialized with fast fallbacks")
    
    def get_decision(self, scenario: str) -> str:
        """Get AI decision with optimized approach"""
        start_time = time.time()
        
        # Check cache first (instant)
        if scenario in self.cache:
            return self.cache[scenario]
        
        # Try fallback rules first (instant)
        for key, decision in self.fallback_rules.items():
            if key in scenario.lower():
                self.cache[scenario] = decision
                return decision
        
        # Try AI with timeout
        try:
            decision = self._get_ai_decision_with_timeout(scenario)
            self.cache[scenario] = decision
            return decision
        except Exception as e:
            print(f"❌ AI Error: {e}")
            # Use default fallback
            decision = "SEARCH"
            self.cache[scenario] = decision
            return decision
    
    def _get_ai_decision_with_timeout(self, scenario: str) -> str:
        """Get AI decision with strict timeout"""
        # Optimized prompt for fast response
        prompt = f"Scenario: {scenario}. Reply with ONLY: MOVE_FORWARD, TURN_LEFT, TURN_RIGHT, STOP, or SEARCH"
        
        # Try current model
        model = self.models[self.current_model]
        
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(self._call_ollama, model, prompt)
                response = future.result(timeout=self.timeout)
                
                # Extract command from response
                decision = self._extract_command(response)
                print(f"🎯 AI Decision: {decision} (model: {model}, time: {time.time() - start_time:.3f}s)")
                return decision
                
        except concurrent.futures.TimeoutError:
            print(f"⏰ Timeout on {model}, trying next model...")
            # Try next model
            self.current_model = (self.current_model + 1) % len(self.models)
            if self.current_model == 0:  # Tried all models
                return "SEARCH"  # Final fallback
            return self._get_ai_decision_with_timeout(scenario)
    
    def _call_ollama(self, model: str, prompt: str) -> str:
        """Call Ollama API using urllib"""
        url = f"{self.ollama_url}/api/chat"
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "options": {
                "temperature": 0,  # Deterministic
                "num_predict": 10,  # Limit response length
                "top_k": 1,        # Most likely response
            }
        }
        
        # Convert data to JSON
        json_data = json.dumps(data).encode('utf-8')
        
        # Create request
        req = urllib.request.Request(
            url,
            data=json_data,
            headers={'Content-Type': 'application/json'}
        )
        
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result["message"]["content"]
        except Exception as e:
            raise Exception(f"Ollama error: {e}")
    
    def _extract_command(self, response: str) -> str:
        """Extract simple command from AI response"""
        valid_commands = ["MOVE_FORWARD", "TURN_LEFT", "TURN_RIGHT", "STOP", "SEARCH"]
        
        # Look for exact matches
        for cmd in valid_commands:
            if cmd in response.upper():
                return cmd
        
        # Look for partial matches
        for cmd in valid_commands:
            if cmd.replace("_", " ") in response.upper():
                return cmd
        
        return "SEARCH"  # Default fallback
    
    def get_stats(self) -> Dict:
        """Get AI system statistics"""
        return {
            "cache_size": len(self.cache),
            "current_model": self.models[self.current_model],
            "timeout": self.timeout,
            "fallback_rules": len(self.fallback_rules)
        }

def test_optimized_ai():
    """Test the optimized AI system"""
    print("🧪 Testing Optimized AI System")
    print("=" * 40)
    
    ai = OptimizedAI()
    
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
    print(f"   Timeout: {stats['timeout']}s")
    print(f"   Fallback rules: {stats['fallback_rules']}")

if __name__ == "__main__":
    test_optimized_ai() 