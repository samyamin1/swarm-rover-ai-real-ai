#!/usr/bin/env python3
"""
Embedded AI System - Rule-Based Decision Making
Provides instant responses for real-time robotics
"""

import time
import json
from typing import Dict, List, Optional

class EmbeddedAI:
    def __init__(self):
        """Initialize embedded AI with rule-based decision making"""
        self.rules = {
            # Target-related rules
            "target_ahead": "MOVE_FORWARD",
            "target_found": "STOP",
            "target_visible": "MOVE_FORWARD",
            "target_detected": "MOVE_FORWARD",
            
            # Obstacle-related rules
            "obstacle_detected": "TURN_LEFT",
            "obstacle_ahead": "TURN_LEFT",
            "wall_detected": "TURN_RIGHT",
            "blocked_path": "TURN_LEFT",
            
            # Search-related rules
            "search_mode": "SEARCH",
            "search_area": "SEARCH",
            "no_target": "SEARCH",
            "explore": "SEARCH",
            
            # Movement rules
            "move_forward": "MOVE_FORWARD",
            "turn_left": "TURN_LEFT",
            "turn_right": "TURN_RIGHT",
            "stop": "STOP",
            
            # Default actions
            "default": "SEARCH",
            "unknown": "SEARCH",
        }
        
        # Decision history for learning
        self.decision_history = []
        
        print("🤖 Embedded AI initialized with rule-based decision making")
    
    def get_decision(self, scenario: str) -> str:
        """Get instant decision based on scenario"""
        start_time = time.time()
        
        # Convert scenario to lowercase for matching
        scenario_lower = scenario.lower()
        print(f"🔍 Debug: scenario_lower = '{scenario_lower}'")
        
        # Check each rule (excluding default rules)
        for key, command in self.rules.items():
            if key not in ["default", "unknown"]:
                # Try different variations of the key
                key_variations = [
                    key,  # original: "target_ahead"
                    key.replace("_", " "),  # "target ahead"
                    key.replace("_", ""),   # "targetahead"
                ]
                
                for variation in key_variations:
                    print(f"🔍 Debug: checking rule '{key}' (variation: '{variation}') in '{scenario_lower}' -> {variation in scenario_lower}")
                    if variation in scenario_lower:
                        decision = command
                        response_time = time.time() - start_time
                        
                        # Log decision
                        self.decision_history.append({
                            "scenario": scenario,
                            "decision": decision,
                            "rule_used": key,
                            "response_time": response_time,
                            "timestamp": time.time()
                        })
                        
                        print(f"🎯 Decision: {decision} (rule: {key}, time: {response_time:.4f}s)")
                        return decision
        
        # Default decision if no rule matches
        default_decision = self.rules["default"]
        response_time = time.time() - start_time
        
        self.decision_history.append({
            "scenario": scenario,
            "decision": default_decision,
            "rule_used": "default",
            "response_time": response_time,
            "timestamp": time.time()
        })
        
        print(f"🎯 Decision: {default_decision} (default, time: {response_time:.4f}s)")
        return default_decision
    
    def add_rule(self, key: str, command: str):
        """Add a new rule to the AI system"""
        self.rules[key] = command
        print(f"📝 Added rule: '{key}' -> '{command}'")
    
    def get_statistics(self) -> Dict:
        """Get AI system statistics"""
        if not self.decision_history:
            return {"total_decisions": 0}
        
        total_decisions = len(self.decision_history)
        avg_response_time = sum(d["response_time"] for d in self.decision_history) / total_decisions
        fastest_response = min(d["response_time"] for d in self.decision_history)
        
        # Count rule usage
        rule_usage = {}
        for decision in self.decision_history:
            rule = decision["rule_used"]
            rule_usage[rule] = rule_usage.get(rule, 0) + 1
        
        return {
            "total_decisions": total_decisions,
            "average_response_time": avg_response_time,
            "fastest_response": fastest_response,
            "rule_usage": rule_usage
        }
    
    def save_history(self, filename: str = "ai_decisions.json"):
        """Save decision history to file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.decision_history, f, indent=2)
            print(f"💾 Decision history saved to {filename}")
        except Exception as e:
            print(f"❌ Failed to save history: {e}")

class HybridAI:
    def __init__(self, enable_ai: bool = False):
        """Initialize hybrid AI system"""
        self.embedded_ai = EmbeddedAI()
        self.enable_ai = enable_ai  # Disable AI for now
        self.cache = {}
        self.cache_hits = 0
        self.cache_misses = 0
        
        print("🤖 Hybrid AI initialized (AI disabled for speed)")
    
    def get_decision(self, scenario: str) -> str:
        """Get decision with caching and optional AI fallback"""
        # Check cache first
        if scenario in self.cache:
            self.cache_hits += 1
            return self.cache[scenario]
        
        self.cache_misses += 1
        
        # Use embedded AI (instant)
        decision = self.embedded_ai.get_decision(scenario)
        
        # Cache the result
        self.cache[scenario] = decision
        
        return decision
    
    def get_cache_stats(self) -> Dict:
        """Get cache statistics"""
        total_requests = self.cache_hits + self.cache_misses
        hit_rate = self.cache_hits / total_requests if total_requests > 0 else 0
        
        return {
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses,
            "hit_rate": hit_rate,
            "cache_size": len(self.cache)
        }

def test_embedded_ai():
    """Test the embedded AI system"""
    print("🧪 Testing Embedded AI System")
    print("=" * 40)
    
    # Create AI system
    ai = EmbeddedAI()
    
    # Test scenarios
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
        print(f"\n{i+1}. Scenario: {scenario}")
        decision = ai.get_decision(scenario)
        print(f"   Decision: {decision}")
    
    # Print statistics
    stats = ai.get_statistics()
    print(f"\n📊 Statistics:")
    print(f"   Total decisions: {stats['total_decisions']}")
    print(f"   Average response time: {stats['average_response_time']:.4f}s")
    print(f"   Fastest response: {stats['fastest_response']:.4f}s")
    print(f"   Rule usage: {stats['rule_usage']}")
    
    # Save history
    ai.save_history()
    
    return ai

def test_hybrid_ai():
    """Test the hybrid AI system"""
    print("\n🧪 Testing Hybrid AI System")
    print("=" * 40)
    
    # Create hybrid AI
    hybrid = HybridAI(enable_ai=False)
    
    # Test scenarios
    scenarios = [
        "You see a target ahead",
        "You encounter an obstacle",
        "You need to search an area",
    ]
    
    print("\n📋 Testing with caching:")
    for scenario in scenarios:
        # First call (cache miss)
        decision1 = hybrid.get_decision(scenario)
        print(f"   {scenario}: {decision1}")
        
        # Second call (cache hit)
        decision2 = hybrid.get_decision(scenario)
        print(f"   {scenario}: {decision2} (cached)")
    
    # Print cache stats
    cache_stats = hybrid.get_cache_stats()
    print(f"\n📊 Cache Statistics:")
    print(f"   Cache hits: {cache_stats['cache_hits']}")
    print(f"   Cache misses: {cache_stats['cache_misses']}")
    print(f"   Hit rate: {cache_stats['hit_rate']:.2%}")
    print(f"   Cache size: {cache_stats['cache_size']}")

if __name__ == "__main__":
    # Test embedded AI
    ai = test_embedded_ai()
    
    # Test hybrid AI
    test_hybrid_ai()
    
    print("\n✅ All tests completed!") 