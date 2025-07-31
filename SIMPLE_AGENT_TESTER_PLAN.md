# SIMPLE AGENT TESTER PLAN

## 🎯 OBJECTIVE
Create a minimal 2-agent communication test to isolate AI model integration issues before tackling the complex swarm simulation.

## 📋 CURRENT ISSUES IDENTIFIED
1. **AI Model Connection**: `Could not connect to Ollama server or list models: 'name'`
2. **Memory Constraints**: Models requiring 6.1 GiB vs 4.1 GiB available
3. **Decision Parsing**: AI returning verbose responses instead of simple commands
4. **Model Loading**: `AttributeError: 'PerceptionBridge' object has no attribute 'llava_model'`

## 🚀 SIMPLE AGENT TESTER DESIGN

### **Phase 1: Minimal 2-Agent Communication Test**
```
Agent A (Sender) ←→ VLM/LLM ←→ Agent B (Receiver)
```

**Components:**
- 2 simple agents (no physics, no pygame)
- Direct Ollama communication test
- Simple message passing
- Clear success/failure metrics

### **Phase 2: Test Scenarios**
1. **Basic Communication**: Agent A sends message, Agent B receives
2. **AI Decision Making**: Agent A asks AI for decision, Agent B executes
3. **Visual Recognition**: Agent A describes scene, Agent B interprets
4. **Memory Test**: Test different model sizes (smollm:135m, phi-2, etc.)

### **Phase 3: Integration Validation**
- Test each AI model individually
- Validate decision parsing
- Measure response times
- Check memory usage

## 📁 FILE STRUCTURE
```
simple_agent_tester/
├── simple_agent.py          # Basic agent class
├── ai_communication.py      # AI model communication
├── test_scenarios.py        # Test scenarios
├── results_logger.py        # Results tracking
└── run_tests.py            # Main test runner
```

## 🎯 SUCCESS CRITERIA
- [ ] 2 agents can communicate through AI models
- [ ] AI models respond within 5 seconds
- [ ] Decision parsing works correctly
- [ ] Memory usage stays under 4 GiB
- [ ] No connection errors to Ollama

## ⚡ IMPLEMENTATION PLAN

### **Step 1: Create Simple Agent Class**
- Remove all pygame/physics dependencies
- Focus only on AI communication
- Simple state machine (IDLE, SEND, RECEIVE)

### **Step 2: AI Communication Module**
- Test Ollama connection
- Try different models (smollm:135m first)
- Simple prompt/response testing
- Error handling and logging

### **Step 3: Test Scenarios**
- Basic message passing
- AI decision making
- Visual scene interpretation
- Memory usage monitoring

### **Step 4: Results Analysis**
- Compare different models
- Identify bottlenecks
- Document working configurations

## 🔧 TECHNICAL APPROACH

### **Model Priority Order:**
1. `smollm:135m` (smallest, fastest)
2. `phi-2` (medium size)
3. `llava:7b` (if memory allows)

### **Testing Strategy:**
- Start with simplest possible communication
- Gradually increase complexity
- Monitor memory usage in real-time
- Log all errors and responses

## 🎯 BENEFITS OF THIS APPROACH

### **Advantages:**
- ✅ Isolates AI integration issues
- ✅ Faster debugging cycles
- ✅ No pygame/display dependencies
- ✅ Clear success metrics
- ✅ Easy to extend and modify

### **Risk Assessment:**
- ⚠️ **Low Risk**: Simple test environment
- ⚠️ **Quick to Implement**: ~2-3 hours
- ⚠️ **Easy to Debug**: Clear logging
- ⚠️ **Won't Break Main Code**: Separate module

## 🚀 RECOMMENDATION: PROCEED WITH SIMPLE TESTER

**Why this is the best approach:**
1. **Isolation**: We can test AI models without swarm complexity
2. **Speed**: Much faster to debug AI issues
3. **Clarity**: Clear success/failure criteria
4. **Foundation**: Once working, easy to integrate into main simulation

**Estimated Time:** 2-3 hours to create and test
**Risk Level:** Very Low
**Impact:** High (will solve core AI integration issues)

## 📝 NEXT STEPS

1. **Create simple_agent_tester directory**
2. **Implement basic agent communication**
3. **Test Ollama connection with different models**
4. **Validate decision parsing**
5. **Document working configuration**
6. **Integrate findings into main simulation**

**Should we proceed with this plan?** 