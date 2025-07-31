#!/usr/bin/env python3
"""
Test Scenarios for Simple Agent Communication
Tests different communication patterns between agents
"""

import time
import json
from typing import Dict, List
from simple_agent import SimpleAgent
from ai_communication import AITester

class TestScenario:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.results = {}
    
    def run(self) -> Dict:
        """Run the test scenario"""
        raise NotImplementedError
    
    def get_results(self) -> Dict:
        """Get test results"""
        return {
            "name": self.name,
            "description": self.description,
            "results": self.results
        }

class BasicCommunicationTest(TestScenario):
    def __init__(self):
        super().__init__("Basic Communication", "Test basic message passing between 2 agents")
    
    def run(self) -> Dict:
        print(f"\n🧪 Running: {self.name}")
        print(f"📝 {self.description}")
        
        # Create agents
        agent_a = SimpleAgent(1, "Alice")
        agent_b = SimpleAgent(2, "Bob")
        
        # Test basic communication
        message = "Hello from Alice"
        response = agent_a.send_message(message)
        
        # Simulate agent B receiving
        ack = agent_b.receive_message(message)
        
        # Collect results
        self.results = {
            "agent_a_status": agent_a.get_status(),
            "agent_b_status": agent_b.get_status(),
            "message_sent": message,
            "response": response,
            "acknowledgment": ack,
            "success": True
        }
        
        print(f"✅ {self.name} completed successfully")
        return self.get_results()

class AIDecisionTest(TestScenario):
    def __init__(self, ai_tester: AITester):
        super().__init__("AI Decision Making", "Test AI decision making with agents")
        self.ai_tester = ai_tester
    
    def run(self) -> Dict:
        print(f"\n🧪 Running: {self.name}")
        print(f"📝 {self.description}")
        
        # Create agents
        agent_a = SimpleAgent(1, "AI_Agent")
        agent_b = SimpleAgent(2, "Executor")
        
        # Test scenarios
        scenarios = [
            "You see a target ahead",
            "You encounter an obstacle",
            "You need to search an area",
            "You found a target"
        ]
        
        results = []
        
        for i, scenario in enumerate(scenarios):
            print(f"\n🔍 Testing scenario {i+1}: {scenario}")
            
            # Test with best available model
            if self.ai_tester.available_models:
                best_model = self.ai_tester.available_models[0]  # Use first available
                
                # Get AI decision
                decision_result = self.ai_tester.test_decision_making(best_model, scenario)
                
                # Simulate agent execution
                if decision_result["success"]:
                    execution = agent_b.receive_message(f"Execute: {decision_result['decision']}")
                    status = "✅ Success"
                else:
                    execution = "Failed to parse decision"
                    status = "❌ Failed"
                
                results.append({
                    "scenario": scenario,
                    "model": best_model,
                    "decision": decision_result["decision"],
                    "execution": execution,
                    "status": status,
                    "response_time": decision_result["response_time"]
                })
                
                print(f"   {status}: {decision_result['decision']} ({decision_result['response_time']:.2f}s)")
            else:
                print("   ❌ No AI models available")
                results.append({
                    "scenario": scenario,
                    "status": "No AI models available",
                    "error": "No models found"
                })
        
        self.results = {
            "scenarios_tested": len(scenarios),
            "successful_decisions": len([r for r in results if "Success" in r.get("status", "")]),
            "average_response_time": sum([r.get("response_time", 0) for r in results if r.get("response_time")]) / len([r for r in results if r.get("response_time")]) if any(r.get("response_time") for r in results) else 0,
            "detailed_results": results
        }
        
        print(f"✅ {self.name} completed: {self.results['successful_decisions']}/{self.results['scenarios_tested']} successful")
        return self.get_results()

class MemoryStressTest(TestScenario):
    def __init__(self, ai_tester: AITester):
        super().__init__("Memory Stress Test", "Test memory usage with different models")
        self.ai_tester = ai_tester
    
    def run(self) -> Dict:
        print(f"\n🧪 Running: {self.name}")
        print(f"📝 {self.description}")
        
        # Test memory usage for each model
        memory_results = []
        
        for model in self.ai_tester.available_models:
            print(f"\n🔍 Testing memory for: {model}")
            
            memory_result = self.ai_tester.test_memory_usage(model)
            memory_results.append(memory_result)
            
            if memory_result["can_load"]:
                print(f"   ✅ {model}: {memory_result['memory_required']:.2f} GB - Can load")
            else:
                print(f"   ❌ {model}: {memory_result['memory_required']:.2f} GB - Too large")
        
        # Find best model for memory constraints
        suitable_models = [r for r in memory_results if r.get("can_load", False)]
        best_model = min(suitable_models, key=lambda x: x.get("memory_required", float('inf'))) if suitable_models else None
        
        self.results = {
            "models_tested": len(memory_results),
            "suitable_models": len(suitable_models),
            "best_model": best_model["model"] if best_model else None,
            "best_model_size": best_model["memory_required"] if best_model else None,
            "detailed_results": memory_results
        }
        
        print(f"✅ {self.name} completed: {self.results['suitable_models']} suitable models found")
        if best_model:
            print(f"🏆 Best model: {best_model['model']} ({best_model['memory_required']:.2f} GB)")
        
        return self.get_results()

class CommunicationStressTest(TestScenario):
    def __init__(self):
        super().__init__("Communication Stress Test", "Test high-frequency communication between agents")
    
    def run(self) -> Dict:
        print(f"\n🧪 Running: {self.name}")
        print(f"📝 {self.description}")
        
        # Create agents
        agent_a = SimpleAgent(1, "Sender")
        agent_b = SimpleAgent(2, "Receiver")
        
        # Send multiple messages rapidly
        messages = [
            "Message 1",
            "Message 2", 
            "Message 3",
            "Message 4",
            "Message 5"
        ]
        
        start_time = time.time()
        
        for message in messages:
            agent_a.send_message(message)
            agent_b.receive_message(message)
            time.sleep(0.05)  # Small delay
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # Calculate metrics
        messages_per_second = len(messages) / total_time
        
        self.results = {
            "messages_sent": len(messages),
            "total_time": total_time,
            "messages_per_second": messages_per_second,
            "agent_a_status": agent_a.get_status(),
            "agent_b_status": agent_b.get_status(),
            "success": True
        }
        
        print(f"✅ {self.name} completed: {messages_per_second:.2f} messages/second")
        return self.get_results()

def run_all_tests(ai_tester: AITester = None) -> Dict:
    """Run all test scenarios"""
    print("🚀 Starting Simple Agent Tester")
    print("=" * 50)
    
    # Initialize AI tester if not provided
    if ai_tester is None:
        ai_tester = AITester()
    
    # Create test scenarios
    tests = [
        BasicCommunicationTest(),
        CommunicationStressTest()
    ]
    
    # Add AI-dependent tests if AI is available
    if ai_tester.client and ai_tester.available_models:
        tests.extend([
            AIDecisionTest(ai_tester),
            MemoryStressTest(ai_tester)
        ])
    
    # Run all tests
    all_results = {
        "timestamp": time.time(),
        "tests_run": len(tests),
        "results": []
    }
    
    for test in tests:
        try:
            result = test.run()
            all_results["results"].append(result)
        except Exception as e:
            print(f"❌ Test {test.name} failed: {e}")
            all_results["results"].append({
                "name": test.name,
                "error": str(e),
                "success": False
            })
    
    # Save results
    with open("test_results.json", "w") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n📊 All tests completed. Results saved to test_results.json")
    return all_results

if __name__ == "__main__":
    run_all_tests() 