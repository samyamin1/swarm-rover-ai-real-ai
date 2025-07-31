#!/usr/bin/env python3
"""
Timeout Test with Model Rotation
"""

import ollama
import time
import concurrent.futures
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Request timed out")

def test_model_with_timeout(model_name, prompt, timeout=10):
    """Test a model with timeout"""
    print(f"🔍 Testing {model_name} with {timeout}s timeout...")
    
    try:
        # Set timeout signal
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout)
        
        # Initialize client
        client = ollama.Client(host='http://localhost:11434')
        
        # Make the call
        start_time = time.time()
        response = client.chat(model=model_name, messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ])
        
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

def test_all_models():
    """Test all available models with timeout"""
    print("🧪 Testing All Models with Timeout")
    print("=" * 40)
    
    try:
        # Initialize client
        client = ollama.Client(host='http://localhost:11434')
        print("✅ Ollama client initialized")
        
        # List available models
        models = client.list()
        model_names = [m['name'] for m in models['models']]
        print(f"📋 Available models: {model_names}")
        
        if not model_names:
            print("❌ No models available")
            return
        
        # Test each model
        results = []
        prompt = "Say 'Hello'"
        
        print(f"\n📤 Testing prompt: '{prompt}'")
        print("-" * 40)
        
        for model_name in model_names:
            result = test_model_with_timeout(model_name, prompt, timeout=15)
            results.append(result)
            time.sleep(1)  # Small delay between tests
        
        # Print summary
        print("\n📊 RESULTS SUMMARY")
        print("=" * 40)
        
        working_models = []
        fast_models = []
        
        for result in results:
            if result["success"]:
                working_models.append(result["model"])
                if result["response_time"] < 5.0:
                    fast_models.append(result["model"])
                print(f"✅ {result['model']}: {result['response_time']:.2f}s")
            else:
                print(f"❌ {result['model']}: {result['error']}")
        
        print(f"\n🏆 Best models:")
        if fast_models:
            print(f"   Fast (<5s): {fast_models}")
        if working_models:
            print(f"   Working: {working_models}")
        
        if not working_models:
            print("   ❌ No working models found!")
        
        return results
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    test_all_models() 