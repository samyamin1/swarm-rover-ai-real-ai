#!/usr/bin/env python3
"""
AI Communication Module for Testing Ollama Models
Tests different models and connection issues
"""

import os
import time
import json
import ollama
from typing import Dict, List, Optional, Tuple

class AITester:
    def __init__(self, host: str = "http://localhost:11434"):
        """Initialize AI tester"""
        self.host = host
        self.client = None
        self.available_models = []
        self.test_results = {}
        
        print(f"AI Tester initialized with host: {host}")
        self._connect_to_ollama()
    
    def _connect_to_ollama(self) -> bool:
        """Connect to Ollama server"""
        try:
            self.client = ollama.Client(host=self.host)
            
            # Test connection
            models = self.client.list()
            self.available_models = [model['name'] for model in models['models']]
            
            print(f"✅ Connected to Ollama at {self.host}")
            print(f"📋 Available models: {self.available_models}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to connect to Ollama: {e}")
            self.available_models = []
            return False
    
    def test_model_connection(self, model_name: str) -> Dict:
        """Test connection to specific model"""
        result = {
            "model": model_name,
            "available": False,
            "response_time": None,
            "error": None,
            "response": None
        }
        
        if not self.client:
            result["error"] = "No Ollama client available"
            return result
        
        try:
            # Test simple prompt
            start_time = time.time()
            response = self.client.chat(model=model_name, messages=[
                {
                    'role': 'user',
                    'content': 'Say "Hello" in one word.'
                }
            ])
            response_time = time.time() - start_time
            
            result["available"] = True
            result["response_time"] = response_time
            result["response"] = response['message']['content']
            
            print(f"✅ {model_name}: {response_time:.2f}s - {result['response']}")
            
        except Exception as e:
            result["error"] = str(e)
            print(f"❌ {model_name}: {e}")
        
        return result
    
    def extract_command_from_response(self, response: str) -> str:
        """Extract simple command from verbose response"""
        valid_commands = ['MOVE_FORWARD', 'MOVE_BACKWARD', 'TURN_LEFT', 'TURN_RIGHT', 'STOP', 'SEARCH']
        
        # Look for exact matches first
        for cmd in valid_commands:
            if cmd in response.upper():
                return cmd
        
        # Look for partial matches (with spaces instead of underscores)
        for cmd in valid_commands:
            cmd_with_spaces = cmd.replace('_', ' ')
            if cmd_with_spaces in response.upper():
                return cmd
        
        # Look for partial matches in quotes
        for cmd in valid_commands:
            if f'"{cmd}"' in response or f"'{cmd}'" in response:
                return cmd
        
        # Look for commands in code blocks
        for cmd in valid_commands:
            if f'"{cmd}"' in response or f"'{cmd}'" in response:
                return cmd
        
        return "STOP"  # Default fallback

    def test_decision_making(self, model_name: str, scenario: str) -> Dict:
        """Test AI decision making with specific scenario"""
        result = {
            "model": model_name,
            "scenario": scenario,
            "success": False,
            "response_time": None,
            "decision": None,
            "error": None,
            "is_verbose": False,
            "extracted_command": None
        }
        
        if not self.client:
            result["error"] = "No Ollama client available"
            return result
        
        try:
            # Create strict decision prompt
            prompt = f"""You are a robot agent in a search and rescue mission.

Scenario: {scenario}

IMPORTANT: Respond with ONLY ONE of these exact commands:
- MOVE_FORWARD
- MOVE_BACKWARD  
- TURN_LEFT
- TURN_RIGHT
- STOP
- SEARCH

Do NOT explain, do NOT write code, do NOT add any other text.
Just respond with the single command word."""
            
            start_time = time.time()
            response = self.client.chat(model=model_name, messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ])
            response_time = time.time() - start_time
            
            decision = response['message']['content'].strip()
            
            # Check if response is verbose (contains code, explanations, etc.)
            verbose_indicators = ['def ', 'function', 'python', '```', 'code', 'approach', 'step']
            is_verbose = any(indicator in decision.lower() for indicator in verbose_indicators)
            
            # Extract command from response (even if verbose)
            extracted_command = self.extract_command_from_response(decision)
            
            # Success if we can extract a valid command
            valid_commands = ['MOVE_FORWARD', 'MOVE_BACKWARD', 'TURN_LEFT', 'TURN_RIGHT', 'STOP', 'SEARCH']
            is_valid_command = extracted_command in valid_commands
            
            result["success"] = is_valid_command
            result["response_time"] = response_time
            result["decision"] = decision
            result["is_verbose"] = is_verbose
            result["extracted_command"] = extracted_command
            
            if result["success"]:
                status = "✅"
                print(f"{status} {model_name} decision: {extracted_command} (extracted from verbose response) ({response_time:.2f}s)")
            else:
                status = "❌"
                print(f"{status} {model_name} decision: {decision[:50]}... ({response_time:.2f}s) - no valid command found")
            
        except Exception as e:
            result["error"] = str(e)
            print(f"❌ {model_name} decision test failed: {e}")
        
        return result
    
    def test_memory_usage(self, model_name: str) -> Dict:
        """Test memory usage for model"""
        result = {
            "model": model_name,
            "memory_available": None,
            "memory_required": None,
            "can_load": False,
            "error": None
        }
        
        try:
            # Get model info
            model_info = self.client.show(model_name)
            
            # Extract size information
            if 'size' in model_info and model_info['size'] is not None:
                size_bytes = model_info['size']
                size_gb = size_bytes / (1024**3)
                result["memory_required"] = size_gb
                
                # Estimate if it can load (rough estimate)
                result["can_load"] = size_gb < 4.0  # Assuming 4GB available
                
                print(f"📊 {model_name}: {size_gb:.2f} GB")
            else:
                result["error"] = "Size information not available"
                print(f"❌ {model_name}: Size information not available")
            
        except Exception as e:
            result["error"] = str(e)
            print(f"❌ {model_name} memory test failed: {e}")
        
        return result
    
    def run_comprehensive_test(self) -> Dict:
        """Run comprehensive test on all available models"""
        print("\n🚀 Starting Comprehensive AI Model Test")
        print("=" * 50)
        
        results = {
            "timestamp": time.time(),
            "host": self.host,
            "models_tested": [],
            "summary": {}
        }
        
        # Test each available model
        for model in self.available_models:
            print(f"\n🔍 Testing model: {model}")
            
            model_results = {
                "model": model,
                "connection": self.test_model_connection(model),
                "decision": self.test_decision_making(model, "You see a target ahead"),
                "memory": self.test_memory_usage(model)
            }
            
            results["models_tested"].append(model_results)
        
        # Generate summary
        working_models = []
        fast_models = []
        
        for test in results["models_tested"]:
            if test["connection"]["available"]:
                working_models.append(test["model"])
                
                if test["connection"]["response_time"] and test["connection"]["response_time"] < 2.0:
                    fast_models.append(test["model"])
        
        results["summary"] = {
            "total_models": len(results["models_tested"]),
            "working_models": working_models,
            "fast_models": fast_models,
            "best_model": fast_models[0] if fast_models else None
        }
        
        print(f"\n📊 Test Summary:")
        print(f"   Working models: {working_models}")
        print(f"   Fast models (<2s): {fast_models}")
        print(f"   Best model: {results['summary']['best_model']}")
        
        return results
    
    def save_results(self, results: Dict, filename: str = "ai_test_results.json"):
        """Save test results to file"""
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"💾 Results saved to {filename}")
        except Exception as e:
            print(f"❌ Failed to save results: {e}")

def main():
    """Test AI communication"""
    tester = AITester()
    results = tester.run_comprehensive_test()
    tester.save_results(results)

if __name__ == "__main__":
    main() 