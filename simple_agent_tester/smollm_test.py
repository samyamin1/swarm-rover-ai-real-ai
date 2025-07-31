#!/usr/bin/env python3
"""
Simple Smollm Test - Sidekick
Tests smollm:135m with basic prompt to verify it works
"""

import time
import subprocess

def test_smollm():
    """Test smollm:135m with simple prompt"""
    print("🧪 Testing Smollm:135m Sidekick")
    print("=" * 35)
    
    prompt = "Hello"
    model = "smollm:135m"
    
    print(f"📝 Prompt: '{prompt}'")
    print(f"🤖 Model: {model}")
    print()
    
    start_time = time.time()
    
    try:
        print("🚀 Starting smollm test...")
        
        # Call smollm directly
        result = subprocess.run([
            "docker", "exec", "swarm_rover_ai_real_ai-ollama-1",
            "ollama", "run", model, prompt
        ], capture_output=True, text=True, timeout=30)
        
        end_time = time.time()
        response_time = end_time - start_time
        
        if result.returncode == 0:
            response = result.stdout.strip()
            print(f"✅ SUCCESS!")
            print(f"⏱️  Response time: {response_time:.3f}s")
            print(f"💬 Response: '{response}'")
            print(f"📊 Return code: {result.returncode}")
        else:
            print(f"❌ FAILED!")
            print(f"⏱️  Time taken: {response_time:.3f}s")
            print(f"🚫 Error: {result.stderr}")
            print(f"📊 Return code: {result.returncode}")
            
    except subprocess.TimeoutExpired:
        print(f"⏰ TIMEOUT after 30 seconds")
        print(f"⏱️  Time taken: {time.time() - start_time:.3f}s")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        print(f"⏱️  Time taken: {time.time() - start_time:.3f}s")

if __name__ == "__main__":
    test_smollm() 