#!/usr/bin/env python3
"""
Very Simple LLM Test
"""

import ollama
import time

def simple_test():
    print("🧪 Very Simple LLM Test")
    print("=" * 30)
    
    try:
        # Initialize client
        client = ollama.Client(host='http://localhost:11434')
        print("✅ Ollama client initialized")
        
        # List available models
        models = client.list()
        print(f"📋 Available models: {[m['name'] for m in models['models']]}")
        
        # Use first available model
        if models['models']:
            model_name = models['models'][0]['name']
            print(f"🔍 Testing with model: {model_name}")
            
            # Very simple prompt
            prompt = "Say 'Hello'"
            
            print(f"📤 Sending prompt: '{prompt}'")
            start_time = time.time()
            
            # Make the call
            response = client.chat(model=model_name, messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ])
            
            response_time = time.time() - start_time
            result = response['message']['content']
            
            print(f"📥 Response: '{result}'")
            print(f"⏱️  Time: {response_time:.2f} seconds")
            
            if "hello" in result.lower():
                print("✅ SUCCESS: Model responded correctly")
            else:
                print("❌ UNEXPECTED: Model responded but not as expected")
                
        else:
            print("❌ No models available")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    simple_test() 