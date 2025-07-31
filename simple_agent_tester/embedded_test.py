#!/usr/bin/env python3
"""
Embedded Model Test - Optimized for Small Models
"""

import ollama
import time
import signal
import json

def timeout_handler(signum, frame):
    raise TimeoutError("Request timed out")

def test_embedded_model(model_name, prompt, timeout=3):
    """Test model with embedded-optimized settings"""
    print(f"🔍 Testing {model_name} (embedded mode, {timeout}s timeout)...")
    
    try:
        # Set timeout signal
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout)
        
        # Initialize client
        client = ollama.Client(host='http://localhost:11434')
        
        # Make the call with optimized parameters
        start_time = time.time()
        response = client.chat(model=model_name, messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ], options={
            'temperature': 0.1,  # Low temperature for consistent responses
            'top_p': 0.9,        # Conservative sampling
            'num_predict': 10,    # Limit response length
        })
        
        # Cancel alarm
        signal.alarm(0)
        
        response_time = time.time() - start_time
        result = response['message']['content']
        
        print(f"✅ {model_name}: {response_time:.2f}s - '{result[:50]}...'")
        return {
            "model": model_name,
            "success": True,
            "response_time": response_time,
            "response": result,
            "error": None
        }
        
    except TimeoutError:
        print(f"⏰ {model_name}: TIMEOUT after {timeout}s")
        return {
            "model": model_name,
            "success": False,
            "response_time": timeout,
            "response": None,
            "error": "Timeout"
        }
    except Exception as e:
        print(f"❌ {model_name}: ERROR - {e}")
        return {
            "model": model_name,
            "success": False,
            "response_time": None,
            "response": None,
            "error": str(e)
        }

def test_embedded_reasoning():
    """Test reasoning capabilities with embedded constraints"""
    print("🧪 Testing Embedded Model Reasoning")
    print("=" * 50)
    
    # Available models (from our current setup)
    models = ['smollm:135m']  # Start with smallest available
    
    # Simple reasoning tests
    reasoning_tests = [
        "Say 'MOVE_FORWARD' if you see a target ahead.",
        "Say 'TURN_LEFT' if you encounter an obstacle.",
        "Say 'SEARCH' if you need to find something.",
        "Say 'STOP' if you found a target.",
    ]
    
    results = []
    
    for model in models:
        print(f"\n🔍 Testing {model} with reasoning tests...")
        model_results = []
        
        for i, test in enumerate(reasoning_tests):
            print(f"  Test {i+1}: {test}")
            result = test_embedded_model(model, test, timeout=5)
            model_results.append(result)
            
            if result["success"]:
                print(f"    ✅ Response: {result['response'][:30]}...")
            else:
                print(f"    ❌ Failed: {result['error']}")
        
        results.append({
            "model": model,
            "tests": model_results,
            "success_rate": len([r for r in model_results if r["success"]]) / len(model_results)
        })
    
    # Print summary
    print("\n📊 EMBEDDED TEST SUMMARY")
    print("=" * 50)
    
    for result in results:
        print(f"\n🏆 {result['model']}:")
        print(f"   Success Rate: {result['success_rate']*100:.1f}%")
        
        successful_tests = [r for r in result['tests'] if r['success']]
        if successful_tests:
            avg_time = sum(r['response_time'] for r in successful_tests) / len(successful_tests)
            print(f"   Average Response Time: {avg_time:.2f}s")
            print(f"   Fastest Response: {min(r['response_time'] for r in successful_tests):.2f}s")
        
        # Show sample responses
        for i, test in enumerate(result['tests']):
            if test['success']:
                print(f"   Test {i+1}: {test['response'][:50]}...")
    
    return results

def test_command_extraction():
    """Test command extraction from responses"""
    print("\n🔧 Testing Command Extraction")
    print("=" * 30)
    
    def extract_command(response):
        """Extract simple command from response"""
        valid_commands = ['MOVE_FORWARD', 'MOVE_BACKWARD', 'TURN_LEFT', 'TURN_RIGHT', 'STOP', 'SEARCH']
        
        # Look for exact matches
        for cmd in valid_commands:
            if cmd in response.upper():
                return cmd
        
        # Look for partial matches
        for cmd in valid_commands:
            cmd_spaces = cmd.replace('_', ' ')
            if cmd_spaces in response.upper():
                return cmd
        
        return "STOP"  # Default
    
    # Test with sample responses
    test_responses = [
        "I should MOVE_FORWARD to reach the target.",
        "The best action is to TURN_LEFT around the obstacle.",
        "I need to SEARCH the area for targets.",
        "I found the target, so I should STOP.",
        "Here is a Python function: def move_forward(): return 'MOVE_FORWARD'",
    ]
    
    for i, response in enumerate(test_responses):
        extracted = extract_command(response)
        print(f"Response {i+1}: {response[:40]}...")
        print(f"Extracted: {extracted}")
        print()

if __name__ == "__main__":
    # Test embedded reasoning
    results = test_embedded_reasoning()
    
    # Test command extraction
    test_command_extraction()
    
    # Save results
    with open("embedded_test_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n💾 Results saved to embedded_test_results.json") 