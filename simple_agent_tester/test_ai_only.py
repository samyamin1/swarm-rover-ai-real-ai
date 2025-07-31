#!/usr/bin/env python3
"""
Test AI Decision Making Only
"""

from ai_communication import AITester

def test_ai_decisions():
    print("🧪 Testing AI Decision Making with Stricter Parsing")
    print("=" * 50)
    
    ai_tester = AITester()
    
    # Test scenarios
    scenarios = [
        "You see a target ahead",
        "You encounter an obstacle", 
        "You need to search an area",
        "You found a target"
    ]
    
    for i, scenario in enumerate(scenarios):
        print(f"\n🔍 Testing scenario {i+1}: {scenario}")
        
        if ai_tester.available_models:
            best_model = ai_tester.available_models[0]  # Use first available
            result = ai_tester.test_decision_making(best_model, scenario)
            
            if result["success"]:
                print(f"   ✅ SUCCESS: {result['decision']} ({result['response_time']:.2f}s)")
            else:
                reason = "verbose" if result.get("is_verbose") else "invalid command"
                print(f"   ❌ FAILED: {reason} - {result['decision'][:50]}...")
        else:
            print("   ❌ No AI models available")

if __name__ == "__main__":
    test_ai_decisions() 