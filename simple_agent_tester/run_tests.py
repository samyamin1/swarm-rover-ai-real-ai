#!/usr/bin/env python3
"""
Main Test Runner for Simple Agent Tester
Orchestrates all tests and provides comprehensive results
"""

import os
import sys
import time
import json
import argparse
from typing import Dict, List

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from simple_agent import SimpleAgent
from ai_communication import AITester
from test_scenarios import run_all_tests

def print_banner():
    """Print test banner"""
    print("=" * 60)
    print("🤖 SIMPLE AGENT TESTER")
    print("=" * 60)
    print("Testing AI model integration for swarm robotics")
    print("=" * 60)

def print_summary(results: Dict):
    """Print test summary"""
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    total_tests = len(results.get("results", []))
    successful_tests = len([r for r in results.get("results", []) if r.get("success", False)])
    
    print(f"Total tests run: {total_tests}")
    print(f"Successful tests: {successful_tests}")
    print(f"Success rate: {(successful_tests/total_tests)*100:.1f}%" if total_tests > 0 else "N/A")
    
    # Print individual test results
    for result in results.get("results", []):
        status = "✅ PASS" if result.get("success", False) else "❌ FAIL"
        print(f"{status}: {result.get('name', 'Unknown')}")
        
        if "error" in result:
            print(f"   Error: {result['error']}")
    
    print("=" * 60)

def save_detailed_results(results: Dict, filename: str = "detailed_test_results.json"):
    """Save detailed results to file"""
    try:
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"💾 Detailed results saved to {filename}")
    except Exception as e:
        print(f"❌ Failed to save detailed results: {e}")

def run_quick_test():
    """Run a quick connectivity test"""
    print("\n🔍 Running Quick Connectivity Test...")
    
    # Test basic agent communication
    agent_a = SimpleAgent(1, "QuickTest_A")
    agent_b = SimpleAgent(2, "QuickTest_B")
    
    message = "Quick test message"
    agent_a.send_message(message)
    agent_b.receive_message(message)
    
    print("✅ Basic agent communication: PASS")
    
    # Test AI connection
    try:
        ai_tester = AITester()
        if ai_tester.client and ai_tester.available_models:
            print(f"✅ AI connection: PASS (Found {len(ai_tester.available_models)} models)")
            return True
        else:
            print("❌ AI connection: FAIL (No models available)")
            return False
    except Exception as e:
        print(f"❌ AI connection: FAIL ({e})")
        return False

def main():
    """Main test runner"""
    parser = argparse.ArgumentParser(description="Simple Agent Tester")
    parser.add_argument("--quick", action="store_true", help="Run quick connectivity test only")
    parser.add_argument("--ai-only", action="store_true", help="Test AI models only")
    parser.add_argument("--agent-only", action="store_true", help="Test agent communication only")
    parser.add_argument("--output", default="test_results.json", help="Output file for results")
    
    args = parser.parse_args()
    
    print_banner()
    
    if args.quick:
        # Quick connectivity test
        success = run_quick_test()
        if success:
            print("\n✅ Quick test passed! Ready for full testing.")
        else:
            print("\n❌ Quick test failed! Check Ollama connection.")
        return
    
    # Run comprehensive tests
    print("\n🚀 Starting comprehensive tests...")
    start_time = time.time()
    
    try:
        results = run_all_tests()
        
        # Add timing information
        results["total_time"] = time.time() - start_time
        results["timestamp"] = time.time()
        
        # Print summary
        print_summary(results)
        
        # Save results
        save_detailed_results(results, args.output)
        
        # Print recommendations
        print("\n🎯 RECOMMENDATIONS:")
        
        # Check AI models
        ai_results = [r for r in results.get("results", []) if "AI" in r.get("name", "")]
        if ai_results:
            working_ai = [r for r in ai_results if r.get("success", False)]
            if working_ai:
                print("✅ AI models are working - ready for swarm integration")
            else:
                print("❌ AI models need attention - check Ollama connection")
        
        # Check agent communication
        comm_results = [r for r in results.get("results", []) if "Communication" in r.get("name", "")]
        if comm_results:
            working_comm = [r for r in comm_results if r.get("success", False)]
            if working_comm:
                print("✅ Agent communication is working")
            else:
                print("❌ Agent communication needs attention")
        
        print(f"\n⏱️  Total test time: {results['total_time']:.2f} seconds")
        
    except Exception as e:
        print(f"\n❌ Test runner failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 