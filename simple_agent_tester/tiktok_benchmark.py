#!/usr/bin/env python3
"""
TikTok-Style Model Benchmark
Measures first word and complete sentence response times
"""

import time
import subprocess
import threading
from typing import Dict, List, Tuple
import json

class TikTokBenchmark:
    def __init__(self):
        """Initialize TikTok-style benchmark"""
        self.models = [
            "qwen2.5:0.5b",    # 397 MB
            "smollm:135m",      # 91 MB  
            "moondream:latest", # 1.7 GB
        ]
        self.prompt = "Hello"
        self.results = {}
        
        print("⏱️  TikTok-Style Model Benchmark")
        print("=" * 40)
        print(f"📝 Prompt: '{self.prompt}'")
        print(f"🤖 Models: {', '.join(self.models)}")
        print()
    
    def benchmark_model(self, model: str) -> Dict:
        """Benchmark a single model with TikTok-style timing"""
        print(f"🧪 Testing {model}...")
        
        start_time = time.time()
        first_word_time = None
        complete_time = None
        response = ""
        
        try:
            # Start the ollama process
            process = subprocess.Popen([
                "docker", "exec", "swarm_rover_ai_real_ai-ollama-1",
                "ollama", "run", model, self.prompt
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Monitor output in real-time
            while True:
                char = process.stdout.read(1)
                if not char:
                    break
                
                response += char
                current_time = time.time() - start_time
                
                # Check for first word
                if first_word_time is None and len(response.strip()) > 0:
                    first_word_time = current_time
                    print(f"   🎯 First word: {current_time:.3f}s")
                
                # Check for complete sentence (period, exclamation, question mark)
                if complete_time is None and any(punct in response for punct in ['.', '!', '?', '\n']):
                    complete_time = current_time
                    print(f"   ✅ Complete: {current_time:.3f}s")
                    break
            
            # Wait for process to finish
            process.wait()
            
            # If no complete sentence detected, use full response time
            if complete_time is None:
                complete_time = time.time() - start_time
                print(f"   ✅ Complete: {complete_time:.3f}s")
            
            # If no first word detected, use first character time
            if first_word_time is None:
                first_word_time = complete_time
                print(f"   🎯 First word: {first_word_time:.3f}s")
            
            return {
                "model": model,
                "first_word_time": first_word_time,
                "complete_time": complete_time,
                "response": response.strip(),
                "success": True
            }
            
        except Exception as e:
            return {
                "model": model,
                "first_word_time": None,
                "complete_time": None,
                "response": "",
                "error": str(e),
                "success": False
            }
    
    def run_benchmark(self) -> Dict:
        """Run benchmark for all models"""
        print("🚀 Starting TikTok-Style Benchmark...")
        print()
        
        for model in self.models:
            result = self.benchmark_model(model)
            self.results[model] = result
            print()
        
        return self.results
    
    def print_results(self):
        """Print benchmark results in TikTok style"""
        print("📊 BENCHMARK RESULTS")
        print("=" * 50)
        
        # Sort by first word time (fastest first)
        sorted_results = sorted(
            self.results.items(),
            key=lambda x: x[1].get('first_word_time', float('inf')) if x[1].get('success') else float('inf')
        )
        
        for i, (model, result) in enumerate(sorted_results):
            if result['success']:
                print(f"{i+1}. 🏆 {model}")
                print(f"   ⚡ First word: {result['first_word_time']:.3f}s")
                print(f"   📝 Complete: {result['complete_time']:.3f}s")
                print(f"   💬 Response: '{result['response'][:100]}...'")
            else:
                print(f"{i+1}. ❌ {model}")
                print(f"   🚫 Failed: {result.get('error', 'Unknown error')}")
            print()
        
        # Summary statistics
        successful_results = [r for r in self.results.values() if r['success']]
        if successful_results:
            fastest_first = min(r['first_word_time'] for r in successful_results)
            fastest_complete = min(r['complete_time'] for r in successful_results)
            slowest_first = max(r['first_word_time'] for r in successful_results)
            slowest_complete = max(r['complete_time'] for r in successful_results)
            
            print("📈 SUMMARY STATISTICS")
            print("=" * 30)
            print(f"⚡ Fastest first word: {fastest_first:.3f}s")
            print(f"📝 Fastest complete: {fastest_complete:.3f}s")
            print(f"🐌 Slowest first word: {slowest_first:.3f}s")
            print(f"🐌 Slowest complete: {slowest_complete:.3f}s")
            print(f"✅ Successful models: {len(successful_results)}/{len(self.models)}")
    
    def save_results(self, filename: str = "tiktok_benchmark_results.json"):
        """Save benchmark results to file"""
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"💾 Results saved to {filename}")

def main():
    """Run the TikTok-style benchmark"""
    benchmark = TikTokBenchmark()
    results = benchmark.run_benchmark()
    benchmark.print_results()
    benchmark.save_results()

if __name__ == "__main__":
    main() 