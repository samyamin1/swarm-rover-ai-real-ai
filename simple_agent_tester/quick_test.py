#!/usr/bin/env python3
"""
Quick Test with Short Timeout
"""

import ollama
import time
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Request timed out")

def quick_test_model(model_name, timeout=5):
    """Quick test with short timeout"""
    print(f"⚡ Quick test {model_name} ({timeout}s timeout)...")
    
    try:
        # Set timeout signal
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout)
        
        # Initialize client
        client = ollama.Client(host='http://localhost:11434')
        
        # Very simple prompt
        prompt = "Hi"
        
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
        
        print(f"✅ {model_name}: {response_time:.2f}s - '{result}'")
        return True, response_time, result
        
    except TimeoutError:
        print(f"⏰ {model_name}: TIMEOUT")
        return False, timeout, None
    except Exception as e:
        print(f"❌ {model_name}: {e}")
        return False, None, None

def main():
    print("⚡ Quick Model Test")
    print("=" * 30)
    
    # Test each model with short timeout
    models = ['smollm:135m', 'llava:7b', 'moondream:latest']
    
    for model in models:
        success, time_taken, response = quick_test_model(model, timeout=3)
        if success:
            print(f"🎉 {model} works! Response time: {time_taken:.2f}s")
            break
        time.sleep(0.5)  # Small delay
    
    print("\n📊 Test completed")

if __name__ == "__main__":
    main() 