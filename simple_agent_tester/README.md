# Simple Agent Tester

A minimal testing framework to isolate and debug AI model integration issues for the Swarm Rover AI project.

## 🎯 Purpose

This tester helps identify and solve AI integration problems before dealing with the complex swarm simulation. It focuses on:

- **AI Model Connection**: Test Ollama connectivity
- **Memory Constraints**: Test different model sizes
- **Decision Parsing**: Validate AI response parsing
- **Agent Communication**: Test basic message passing

## 📁 Structure

```
simple_agent_tester/
├── simple_agent.py          # Basic agent class (no pygame/physics)
├── ai_communication.py      # AI model testing and communication
├── test_scenarios.py        # Test scenarios and patterns
├── run_tests.py            # Main test runner
└── README.md               # This file
```

## 🚀 Quick Start

### 1. Quick Connectivity Test
```bash
cd simple_agent_tester
python run_tests.py --quick
```

### 2. Full Test Suite
```bash
python run_tests.py
```

### 3. AI Models Only
```bash
python run_tests.py --ai-only
```

### 4. Agent Communication Only
```bash
python run_tests.py --agent-only
```

## 🧪 Test Scenarios

### Basic Communication Test
- Tests message passing between 2 agents
- No AI models required
- Validates basic agent functionality

### AI Decision Making Test
- Tests AI model decision making
- Validates response parsing
- Tests different scenarios (target detection, obstacle avoidance)

### Memory Stress Test
- Tests memory usage for different models
- Identifies suitable models for 4GB constraint
- Finds optimal model size

### Communication Stress Test
- Tests high-frequency communication
- Measures performance metrics
- Validates system stability

## 📊 Expected Results

### Success Criteria
- [ ] 2 agents can communicate through AI models
- [ ] AI models respond within 5 seconds
- [ ] Decision parsing works correctly
- [ ] Memory usage stays under 4 GiB
- [ ] No connection errors to Ollama

### Output Files
- `test_results.json` - Basic test results
- `detailed_test_results.json` - Comprehensive results
- `ai_test_results.json` - AI-specific results

## 🔧 Troubleshooting

### Common Issues

1. **Ollama Connection Failed**
   ```
   ❌ Failed to connect to Ollama: 'name'
   ```
   **Solution**: Check if Ollama is running and accessible

2. **No Models Available**
   ```
   ❌ AI connection: FAIL (No models available)
   ```
   **Solution**: Download models with `ollama pull smollm:135m`

3. **Memory Constraint**
   ```
   ❌ model: 6.1 GiB - Too large
   ```
   **Solution**: Use smaller models like `smollm:135m`

### Model Priority
1. `smollm:135m` (smallest, fastest)
2. `phi-2` (medium size)
3. `llava:7b` (if memory allows)

## 🎯 Integration with Main Project

Once the simple agent tester passes all tests:

1. **Copy working AI configuration** to main simulation
2. **Use validated models** in PerceptionBridge
3. **Apply decision parsing logic** to agent nodes
4. **Integrate memory management** strategies

## 📝 Usage Examples

### Test Specific Model
```python
from ai_communication import AITester

tester = AITester()
result = tester.test_model_connection("smollm:135m")
print(f"Model available: {result['available']}")
```

### Test Agent Communication
```python
from simple_agent import SimpleAgent

agent_a = SimpleAgent(1, "Alice")
agent_b = SimpleAgent(2, "Bob")

response = agent_a.send_message("Hello")
ack = agent_b.receive_message("Hello")
```

### Run Custom Test
```python
from test_scenarios import AIDecisionTest
from ai_communication import AITester

ai_tester = AITester()
test = AIDecisionTest(ai_tester)
results = test.run()
```

## 🔍 Debugging

### Enable Verbose Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Ollama Status
```bash
curl http://localhost:11434/api/tags
```

### Monitor Memory Usage
```bash
docker stats swarm_rover_ai_real_ai-ollama-1
```

## 📈 Performance Metrics

The tester measures:
- **Response Time**: AI model response latency
- **Memory Usage**: Model memory requirements
- **Success Rate**: Decision parsing accuracy
- **Throughput**: Messages per second

## 🎯 Next Steps

After successful testing:
1. **Document working configuration**
2. **Update main simulation** with working AI setup
3. **Test in swarm environment**
4. **Optimize for production**

---

**Note**: This tester is designed to be independent of the main swarm simulation. It won't interfere with existing code and provides a clean testing environment. 