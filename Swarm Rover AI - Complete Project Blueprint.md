# Swarm Rover AI - Complete Project Blueprint

## 🎯 Master Guide for AI Agent Project Recreation

**Purpose:** This document contains EVERYTHING needed for an AI agent to recreate the complete Swarm Rover AI project from scratch.

**Target:** AI Agent capable of code generation, file creation, and system implementation

**Outcome:** Fully functional modular swarm robotics simulation platform with AI-driven autonomous agents

---

## 📋 Project Mission & Objectives

### **Primary Mission**
Build a complete modular swarm robotics simulation platform featuring 6-10 autonomous agents with AI-driven decision making, advanced coordination algorithms, and real-time 2D simulation for search-and-rescue missions.

### **Core Objectives**
1. **Autonomous Agent System** - 6-10 independent agents with AI decision making
2. **Advanced Coordination** - Alpha election, task sharing, formation control
3. **AI Integration** - YOLOv8n, TinyLLaVA, Phi-2 models for perception and reasoning
4. **Real-time Simulation** - 2D physics-based environment with visualization
5. **Mission Scenarios** - Search & rescue, formation flying, obstacle navigation
6. **Professional Quality** - Complete documentation, testing, deployment ready

### **Success Criteria**
- ✅ 100% mission success rate in search & rescue scenarios
- ✅ 95%+ formation accuracy in coordination tasks
- ✅ Real-time performance (50+ FPS simulation)
- ✅ Comprehensive test coverage (95%+)
- ✅ Production-ready deployment (Docker/Kubernetes)
- ✅ Complete documentation and user guides

---

## 🏗️ System Architecture

### **High-Level Architecture**
```
┌─────────────────────────────────────────────────────────────┐
│                    SWARM ROVER AI SYSTEM                   │
├─────────────────────────────────────────────────────────────┤
│  🤖 AGENT LAYER                                            │
│  ├── Alpha Agent (Leadership & Coordination)               │
│  ├── Follower Agents (Task Execution)                      │
│  └── Agent State Machines (Behavior Control)               │
├─────────────────────────────────────────────────────────────┤
│  🧠 AI INTELLIGENCE LAYER                                  │
│  ├── YOLOv8n (Object Detection)                           │
│  ├── TinyLLaVA (Vision-Language Understanding)            │
│  └── Phi-2 (Decision Making & Communication)              │
├─────────────────────────────────────────────────────────────┤
│  📡 COMMUNICATION LAYER                                    │
│  ├── Swarm Agent Packet Protocol                          │
│  ├── ROS2 Message System                                  │
│  └── Decentralized Network Topology                       │
├─────────────────────────────────────────────────────────────┤
│  🎮 SIMULATION LAYER                                       │
│  ├── 2D Physics Engine                                    │
│  ├── Real-time Visualization                              │
│  └── Mission Scenario Engine                              │
├─────────────────────────────────────────────────────────────┤
│  🧪 TESTING & VALIDATION LAYER                            │
│  ├── Automated Test Suite                                 │
│  ├── Performance Benchmarking                             │
│  └── Mission Validation Framework                         │
└─────────────────────────────────────────────────────────────┘
```

### **Component Relationships**
- **Agents** communicate via **Swarm Agent Packets**
- **AI Models** provide perception and decision-making capabilities
- **Simulation Engine** provides physics and visualization
- **Testing Framework** validates all components
- **Deployment System** packages everything for production

---

## 📁 Complete Project Structure

### **Directory Layout**
```
swarm_rover_ai/
├── 📄 README.md                           # Main project documentation
├── 📄 LICENSE                             # MIT License
├── 📄 requirements.txt                    # Python dependencies
├── 📄 Dockerfile                          # Container configuration
├── 📄 docker-compose.yml                  # Multi-container setup
├── 📄 .dockerignore                       # Docker ignore patterns
├── 📄 .gitignore                          # Git ignore patterns
├── 📄 VISUAL_EVIDENCE_REPORT.md           # Demonstration results
├── 📄 TESTING_REPORT.md                   # Test results and metrics
├── 📄 PROJECT_SUMMARY.md                  # Executive summary
├── 📄 todo.md                             # Development progress tracker
│
├── 🤖 swarm_agents/                       # ROS2 Agent Package
│   ├── 📄 package.xml                     # ROS2 package definition
│   ├── 📄 setup.py                        # Python package setup
│   ├── 📄 CMakeLists.txt                  # Build configuration
│   ├── 📁 resource/                       # Package resources
│   ├── 📁 msg/                            # Custom ROS2 messages
│   │   ├── SwarmAgentPacket.msg           # Main communication protocol
│   │   ├── TaskAnnouncement.msg           # Task sharing messages
│   │   ├── AlphaElection.msg              # Leadership election
│   │   └── FormationControl.msg           # Formation commands
│   ├── 📁 swarm_agents/                   # Python modules
│   │   ├── __init__.py
│   │   ├── agent_node.py                  # Base agent implementation
│   │   ├── alpha_agent.py                 # Alpha agent logic
│   │   ├── perception_bridge.py           # AI model integration
│   │   ├── coordination_algorithms.py     # Swarm coordination
│   │   └── behavior_state_machine.py      # Agent behaviors
│   └── 📁 launch/                         # ROS2 launch files
│       └── basic_swarm.launch.py          # Basic swarm launcher
│
├── 🎮 simulation/                         # Simulation Environment
│   ├── 📁 src/                            # Core simulation code
│   │   ├── simulation_environment.py      # Main simulation engine
│   │   └── scenario_generator.py          # Dynamic scenario creation
│   └── 📁 scenarios/                      # Predefined missions
│       ├── basic_search_rescue.json       # Search & rescue scenario
│       └── complex_formation_mission.json # Formation mission
│
├── 🧠 models/                             # AI Models
│   ├── download_models.py                 # Model download script
│   └── optimize_models.py                 # Model optimization
│
├── 🧪 testing/                            # Testing Framework
│   ├── 📁 src/                            # Test implementations
│   │   ├── testing_framework.py           # Main test framework
│   │   └── performance_analyzer.py        # Performance metrics
│   ├── 📁 benchmarks/                     # Benchmark results
│   └── 📁 reports/                        # Test reports
│
├── 🐳 deployment/                         # Deployment Configuration
│   ├── deploy.sh                          # Main deployment script
│   └── kubernetes.yaml                    # Kubernetes configuration
│
├── 📚 docs/                               # Documentation
│   ├── architecture_design.md             # System architecture
│   ├── API_DOCUMENTATION.md               # Complete API reference
│   ├── USER_GUIDE.md                      # User manual
│   └── DEVELOPER_GUIDE.md                 # Developer documentation
│
└── 🔧 scripts/                            # Utility Scripts
    └── setup_environment.sh               # Environment setup
```

---

## 🚀 Implementation Phases

### **Phase 1: Project Setup and Architecture Design**
**Duration:** 1-2 hours  
**Objective:** Establish project foundation and design system architecture

**Tasks:**
1. Create complete directory structure
2. Initialize Git repository with proper .gitignore
3. Create comprehensive README.md with project overview
4. Design system architecture document
5. Define requirements.txt with all dependencies
6. Create MIT license file
7. Set up todo.md for progress tracking

**Deliverables:**
- Complete project skeleton
- Architecture design document
- Initial documentation framework

### **Phase 2: Core ROS2 Infrastructure**
**Duration:** 2-3 hours  
**Objective:** Implement ROS2 communication system and agent framework

**Tasks:**
1. Create ROS2 package structure (package.xml, setup.py, CMakeLists.txt)
2. Define custom message types (SwarmAgentPacket, TaskAnnouncement, etc.)
3. Implement base agent node with ROS2 integration
4. Create alpha agent with leadership capabilities
5. Set up launch files for multi-agent deployment
6. Implement basic communication protocols

**Deliverables:**
- Functional ROS2 package
- Custom message definitions
- Base agent and alpha agent implementations
- Launch configuration

### **Phase 3: AI Models Integration**
**Duration:** 2-3 hours  
**Objective:** Integrate AI models for perception and decision making

**Tasks:**
1. Create model download script for YOLOv8n, TinyLLaVA, Phi-2
2. Implement model optimization (ONNX conversion, quantization)
3. Create perception bridge for AI model integration
4. Implement object detection pipeline
5. Set up vision-language processing
6. Create decision-making interface

**Deliverables:**
- AI model download and optimization scripts
- Perception bridge implementation
- Integrated AI capabilities

### **Phase 4: Swarm Coordination Algorithms**
**Duration:** 3-4 hours  
**Objective:** Implement advanced swarm coordination and behavior systems

**Tasks:**
1. Implement Alpha Agent Election algorithm
2. Create Decentralized Task Sharing system
3. Develop Formation Control algorithms (line, circle, diamond, V-formation)
4. Implement Consensus Decision Making
5. Create Agent Behavior State Machines
6. Develop Fault Tolerance mechanisms

**Deliverables:**
- Complete coordination algorithm suite
- Behavior state machine implementation
- Fault-tolerant communication system

### **Phase 5: 2D Simulation Environment**
**Duration:** 3-4 hours  
**Objective:** Create real-time simulation with physics and visualization

**Tasks:**
1. Implement 2D physics engine with pygame
2. Create real-time visualization system
3. Develop obstacle and target management
4. Implement mission scenario loader
5. Create dynamic scenario generator
6. Add performance monitoring and metrics

**Deliverables:**
- Complete simulation environment
- Mission scenario system
- Real-time visualization

### **Phase 6: Testing Framework**
**Duration:** 2-3 hours  
**Objective:** Comprehensive testing and validation system

**Tasks:**
1. Create automated test framework
2. Implement unit tests for all components
3. Develop integration tests for swarm behaviors
4. Create performance benchmarking system
5. Implement stress testing capabilities
6. Generate comprehensive test reports

**Deliverables:**
- Complete testing framework
- Automated test suite
- Performance benchmarking system

### **Phase 7: Docker Containerization**
**Duration:** 1-2 hours  
**Objective:** Package system for deployment

**Tasks:**
1. Create multi-stage Dockerfile
2. Implement docker-compose configuration
3. Create deployment scripts
4. Set up Kubernetes configuration
5. Implement monitoring and logging

**Deliverables:**
- Docker containerization
- Deployment automation
- Production-ready configuration

### **Phase 8: Documentation**
**Duration:** 2-3 hours  
**Objective:** Complete professional documentation

**Tasks:**
1. Create comprehensive API documentation
2. Write detailed user guide
3. Develop developer documentation
4. Update README with complete instructions
5. Create visual diagrams and examples

**Deliverables:**
- Complete documentation suite
- User and developer guides
- API reference

### **Phase 9: Testing and Validation**
**Duration:** 1-2 hours  
**Objective:** Final validation and quality assurance

**Tasks:**
1. Run comprehensive test suite
2. Validate all mission scenarios
3. Performance benchmarking
4. Create test reports
5. Final system validation

**Deliverables:**
- Validated system
- Performance reports
- Quality assurance documentation

---

## 🔧 Detailed Implementation Specifications

### **1. ROS2 Message Definitions**

#### **SwarmAgentPacket.msg**
```
# Swarm Agent Communication Packet
Header header
uint32 agent_id
string agent_role          # "alpha", "follower", "scout"
string agent_state         # "idle", "searching", "moving_to_target", etc.
geometry_msgs/Point position
geometry_msgs/Vector3 velocity
float32 battery_level
string[] capabilities      # List of agent capabilities
string mission_status      # Current mission status
string[] discovered_targets # List of discovered target IDs
string communication_data  # JSON-encoded additional data
```

#### **TaskAnnouncement.msg**
```
Header header
uint32 announcing_agent_id
string task_type           # "search", "rescue", "patrol", "formation"
string task_priority       # "low", "medium", "high", "critical"
geometry_msgs/Point task_location
float32 estimated_duration
string[] required_capabilities
uint32 max_agents_needed
string task_description
```

#### **AlphaElection.msg**
```
Header header
string election_phase      # "nomination", "voting", "result"
uint32 candidate_agent_id
uint32 voting_agent_id
float32 candidate_score    # Leadership capability score
string vote_reason         # Reason for vote
bool election_complete
uint32 elected_alpha_id
```

#### **FormationControl.msg**
```
Header header
uint32 alpha_agent_id
string formation_type      # "line", "circle", "diamond", "v_formation", "custom"
geometry_msgs/Point[] target_positions
float32 formation_spacing
float32 movement_speed
bool maintain_formation
string formation_objective
```

### **2. Core Agent Implementation**

#### **Base Agent Node (agent_node.py)**
```python
#!/usr/bin/env python3
"""
Base Agent Node Implementation
Provides core functionality for all swarm agents
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point, Vector3
from std_msgs.msg import Header
import json
import time
import math
from enum import Enum

# Import custom messages
from swarm_agents.msg import SwarmAgentPacket, TaskAnnouncement, AlphaElection, FormationControl

class AgentState(Enum):
    IDLE = "idle"
    SEARCHING = "searching"
    MOVING_TO_TARGET = "moving_to_target"
    FORMING_UP = "forming_up"
    FOLLOWING_ALPHA = "following_alpha"
    RESCUING = "rescuing"
    RETURNING_HOME = "returning_home"

class AgentRole(Enum):
    FOLLOWER = "follower"
    ALPHA = "alpha"
    SCOUT = "scout"

class BaseAgent(Node):
    def __init__(self, agent_id, initial_position=(0.0, 0.0)):
        super().__init__(f'agent_{agent_id}')
        
        # Agent properties
        self.agent_id = agent_id
        self.role = AgentRole.FOLLOWER
        self.state = AgentState.IDLE
        self.position = Point(x=initial_position[0], y=initial_position[1], z=0.0)
        self.velocity = Vector3(x=0.0, y=0.0, z=0.0)
        self.battery_level = 100.0
        self.capabilities = ["search", "rescue", "communication"]
        self.mission_status = "ready"
        self.discovered_targets = []
        
        # Communication
        self.communication_range = 150.0
        self.last_heartbeat = time.time()
        self.known_agents = {}
        
        # Publishers
        self.packet_publisher = self.create_publisher(
            SwarmAgentPacket, 'swarm_communication', 10)
        self.task_publisher = self.create_publisher(
            TaskAnnouncement, 'task_announcements', 10)
        
        # Subscribers
        self.packet_subscriber = self.create_subscription(
            SwarmAgentPacket, 'swarm_communication', 
            self.packet_callback, 10)
        self.task_subscriber = self.create_subscription(
            TaskAnnouncement, 'task_announcements',
            self.task_callback, 10)
        
        # Timers
        self.heartbeat_timer = self.create_timer(1.0, self.send_heartbeat)
        self.update_timer = self.create_timer(0.1, self.update_agent)
        
        self.get_logger().info(f'Agent {self.agent_id} initialized')
    
    def send_heartbeat(self):
        """Send regular heartbeat with agent status"""
        packet = SwarmAgentPacket()
        packet.header = Header()
        packet.header.stamp = self.get_clock().now().to_msg()
        packet.agent_id = self.agent_id
        packet.agent_role = self.role.value
        packet.agent_state = self.state.value
        packet.position = self.position
        packet.velocity = self.velocity
        packet.battery_level = self.battery_level
        packet.capabilities = self.capabilities
        packet.mission_status = self.mission_status
        packet.discovered_targets = self.discovered_targets
        packet.communication_data = json.dumps({
            "timestamp": time.time(),
            "agent_type": "base_agent"
        })
        
        self.packet_publisher.publish(packet)
    
    def packet_callback(self, msg):
        """Process incoming swarm communication packets"""
        if msg.agent_id != self.agent_id:
            # Update known agents
            self.known_agents[msg.agent_id] = {
                "role": msg.agent_role,
                "state": msg.agent_state,
                "position": msg.position,
                "velocity": msg.velocity,
                "battery": msg.battery_level,
                "capabilities": msg.capabilities,
                "last_seen": time.time()
            }
            
            # Process based on message content
            self.process_agent_message(msg)
    
    def task_callback(self, msg):
        """Process task announcements"""
        if self.can_handle_task(msg):
            self.consider_task(msg)
    
    def update_agent(self):
        """Main agent update loop"""
        # Update position based on velocity
        dt = 0.1  # 10Hz update rate
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        
        # Update battery (simple drain model)
        self.battery_level -= 0.01  # 1% per 10 seconds
        
        # State-specific behavior
        if self.state == AgentState.IDLE:
            self.idle_behavior()
        elif self.state == AgentState.SEARCHING:
            self.search_behavior()
        elif self.state == AgentState.MOVING_TO_TARGET:
            self.move_to_target_behavior()
        # Add other state behaviors...
    
    def idle_behavior(self):
        """Behavior when agent is idle"""
        # Look for tasks or follow alpha commands
        pass
    
    def search_behavior(self):
        """Behavior when agent is searching"""
        # Implement search pattern
        pass
    
    def move_to_target_behavior(self):
        """Behavior when moving to target"""
        # Implement target approach
        pass
    
    def can_handle_task(self, task_msg):
        """Check if agent can handle the announced task"""
        required_caps = set(task_msg.required_capabilities)
        agent_caps = set(self.capabilities)
        return required_caps.issubset(agent_caps)
    
    def consider_task(self, task_msg):
        """Consider taking on an announced task"""
        # Implement task consideration logic
        pass
    
    def process_agent_message(self, msg):
        """Process messages from other agents"""
        # Implement inter-agent communication processing
        pass
    
    def set_target_position(self, x, y):
        """Set target position for movement"""
        self.target_position = Point(x=x, y=y, z=0.0)
        self.state = AgentState.MOVING_TO_TARGET
    
    def calculate_distance_to(self, position):
        """Calculate distance to given position"""
        dx = position.x - self.position.x
        dy = position.y - self.position.y
        return math.sqrt(dx*dx + dy*dy)

def main(args=None):
    rclpy.init(args=args)
    
    # Create agent with ID from command line or default
    import sys
    agent_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    
    agent = BaseAgent(agent_id)
    
    try:
        rclpy.spin(agent)
    except KeyboardInterrupt:
        pass
    finally:
        agent.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### **3. Alpha Agent Implementation**

#### **Alpha Agent (alpha_agent.py)**
```python
#!/usr/bin/env python3
"""
Alpha Agent Implementation
Provides leadership and coordination for the swarm
"""

from agent_node import BaseAgent, AgentState, AgentRole
from swarm_agents.msg import TaskAnnouncement, AlphaElection, FormationControl
import json
import time
import math

class AlphaAgent(BaseAgent):
    def __init__(self, agent_id, initial_position=(0.0, 0.0)):
        super().__init__(agent_id, initial_position)
        
        self.role = AgentRole.ALPHA
        self.followers = {}
        self.active_tasks = {}
        self.formation_type = "none"
        self.mission_objective = "patrol"
        
        # Alpha-specific publishers
        self.election_publisher = self.create_publisher(
            AlphaElection, 'alpha_election', 10)
        self.formation_publisher = self.create_publisher(
            FormationControl, 'formation_control', 10)
        
        # Alpha-specific subscribers
        self.election_subscriber = self.create_subscription(
            AlphaElection, 'alpha_election',
            self.election_callback, 10)
        self.formation_subscriber = self.create_subscription(
            FormationControl, 'formation_control',
            self.formation_callback, 10)
        
        # Alpha timers
        self.coordination_timer = self.create_timer(2.0, self.coordinate_swarm)
        self.task_assignment_timer = self.create_timer(5.0, self.assign_tasks)
        
        self.get_logger().info(f'Alpha Agent {self.agent_id} initialized')
    
    def coordinate_swarm(self):
        """Main coordination function for the swarm"""
        # Update follower status
        self.update_followers()
        
        # Check mission progress
        self.check_mission_progress()
        
        # Issue formation commands if needed
        if self.formation_type != "none":
            self.maintain_formation()
    
    def update_followers(self):
        """Update status of follower agents"""
        current_time = time.time()
        
        # Remove stale followers
        stale_followers = []
        for agent_id, info in self.followers.items():
            if current_time - info.get("last_seen", 0) > 10.0:
                stale_followers.append(agent_id)
        
        for agent_id in stale_followers:
            del self.followers[agent_id]
            self.get_logger().warn(f'Lost contact with follower {agent_id}')
    
    def assign_tasks(self):
        """Assign tasks to follower agents"""
        available_followers = [
            agent_id for agent_id, info in self.followers.items()
            if info.get("state") == "idle"
        ]
        
        if len(available_followers) >= 2 and self.mission_objective == "search_rescue":
            self.assign_search_rescue_task(available_followers[:2])
    
    def assign_search_rescue_task(self, agent_ids):
        """Assign search and rescue task to specific agents"""
        task = TaskAnnouncement()
        task.header.stamp = self.get_clock().now().to_msg()
        task.announcing_agent_id = self.agent_id
        task.task_type = "search_rescue"
        task.task_priority = "high"
        task.task_location.x = 500.0  # Example coordinates
        task.task_location.y = 300.0
        task.estimated_duration = 300.0  # 5 minutes
        task.required_capabilities = ["search", "rescue"]
        task.max_agents_needed = len(agent_ids)
        task.task_description = f"Search and rescue mission assigned to agents {agent_ids}"
        
        self.task_publisher.publish(task)
        self.get_logger().info(f'Assigned search rescue task to agents {agent_ids}')
    
    def set_formation(self, formation_type, spacing=50.0):
        """Set formation for the swarm"""
        self.formation_type = formation_type
        
        formation_msg = FormationControl()
        formation_msg.header.stamp = self.get_clock().now().to_msg()
        formation_msg.alpha_agent_id = self.agent_id
        formation_msg.formation_type = formation_type
        formation_msg.formation_spacing = spacing
        formation_msg.movement_speed = 2.0
        formation_msg.maintain_formation = True
        formation_msg.formation_objective = "patrol"
        
        # Calculate target positions based on formation type
        target_positions = self.calculate_formation_positions(formation_type, spacing)
        formation_msg.target_positions = target_positions
        
        self.formation_publisher.publish(formation_msg)
        self.get_logger().info(f'Set formation: {formation_type}')
    
    def calculate_formation_positions(self, formation_type, spacing):
        """Calculate target positions for formation"""
        positions = []
        follower_count = len(self.followers)
        
        if formation_type == "line":
            for i in range(follower_count):
                pos = Point()
                pos.x = self.position.x + (i + 1) * spacing
                pos.y = self.position.y
                positions.append(pos)
        
        elif formation_type == "circle":
            for i in range(follower_count):
                angle = 2 * math.pi * i / follower_count
                pos = Point()
                pos.x = self.position.x + spacing * math.cos(angle)
                pos.y = self.position.y + spacing * math.sin(angle)
                positions.append(pos)
        
        elif formation_type == "v_formation":
            for i in range(follower_count):
                pos = Point()
                side = 1 if i % 2 == 0 else -1
                row = (i + 1) // 2
                pos.x = self.position.x - row * spacing * 0.8
                pos.y = self.position.y + side * row * spacing * 0.6
                positions.append(pos)
        
        return positions
    
    def maintain_formation(self):
        """Maintain current formation"""
        if self.formation_type != "none":
            # Recalculate and update formation positions
            self.set_formation(self.formation_type)
    
    def election_callback(self, msg):
        """Handle alpha election messages"""
        if msg.election_phase == "nomination" and msg.candidate_agent_id == self.agent_id:
            # Respond to nomination
            self.respond_to_election(msg)
    
    def formation_callback(self, msg):
        """Handle formation control messages"""
        if msg.alpha_agent_id != self.agent_id:
            # Another alpha is giving formation commands
            self.get_logger().warn(f'Received formation command from agent {msg.alpha_agent_id}')
    
    def respond_to_election(self, election_msg):
        """Respond to alpha election"""
        response = AlphaElection()
        response.header.stamp = self.get_clock().now().to_msg()
        response.election_phase = "voting"
        response.candidate_agent_id = self.agent_id
        response.voting_agent_id = self.agent_id
        response.candidate_score = self.calculate_leadership_score()
        response.vote_reason = "Current alpha agent"
        
        self.election_publisher.publish(response)
    
    def calculate_leadership_score(self):
        """Calculate leadership capability score"""
        score = 0.0
        score += self.battery_level * 0.3  # Battery level
        score += len(self.followers) * 10.0  # Number of followers
        score += (100.0 - self.agent_id) * 0.1  # Lower ID preference
        return score
    
    def check_mission_progress(self):
        """Check overall mission progress"""
        # Implement mission progress monitoring
        pass
    
    def process_agent_message(self, msg):
        """Process messages from other agents"""
        super().process_agent_message(msg)
        
        # Track followers
        if msg.agent_role == "follower":
            self.followers[msg.agent_id] = {
                "state": msg.agent_state,
                "position": msg.position,
                "battery": msg.battery_level,
                "capabilities": msg.capabilities,
                "last_seen": time.time()
            }

def main(args=None):
    import rclpy
    rclpy.init(args=args)
    
    # Create alpha agent
    import sys
    agent_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    
    alpha = AlphaAgent(agent_id)
    
    try:
        rclpy.spin(alpha)
    except KeyboardInterrupt:
        pass
    finally:
        alpha.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### **4. Coordination Algorithms**

#### **Coordination Algorithms (coordination_algorithms.py)**
```python
#!/usr/bin/env python3
"""
Swarm Coordination Algorithms
Advanced algorithms for swarm behavior and coordination
"""

import math
import time
import random
from enum import Enum
from typing import List, Dict, Tuple, Optional
import numpy as np

class AgentRole(Enum):
    FOLLOWER = "follower"
    ALPHA = "alpha"
    SCOUT = "scout"

class AgentState(Enum):
    IDLE = "idle"
    SEARCHING = "searching"
    MOVING_TO_TARGET = "moving_to_target"
    FORMING_UP = "forming_up"
    FOLLOWING_ALPHA = "following_alpha"
    RESCUING = "rescuing"

class TaskType(Enum):
    SEARCH = "search"
    RESCUE = "rescue"
    PATROL = "patrol"
    FORMATION = "formation"
    RECONNAISSANCE = "reconnaissance"

class AgentCapabilities:
    def __init__(self):
        self.search = True
        self.rescue = True
        self.communication = True
        self.formation_flying = True
        self.obstacle_avoidance = True

class AlphaElection:
    """Democratic alpha agent election algorithm"""
    
    def __init__(self):
        self.election_in_progress = False
        self.candidates = {}
        self.votes = {}
        self.election_timeout = 30.0  # 30 seconds
        self.election_start_time = 0.0
    
    def start_election(self, agents):
        """Initiate alpha election process"""
        self.election_in_progress = True
        self.election_start_time = time.time()
        self.candidates = {}
        self.votes = {}
        
        # All agents are potential candidates
        for agent in agents:
            self.candidates[agent.agent_id] = {
                "score": self.calculate_leadership_score(agent),
                "agent": agent
            }
        
        print(f"Alpha election started with {len(self.candidates)} candidates")
        return True
    
    def calculate_leadership_score(self, agent):
        """Calculate leadership capability score for an agent"""
        score = 0.0
        
        # Battery level (30% weight)
        score += agent.battery_level * 0.3
        
        # Experience/uptime (20% weight)
        score += getattr(agent, 'uptime', 100.0) * 0.2
        
        # Communication capability (20% weight)
        if hasattr(agent, 'communication_range'):
            score += (agent.communication_range / 200.0) * 20.0
        
        # Position centrality (15% weight)
        # Agents closer to center of swarm get higher score
        if hasattr(agent, 'centrality_score'):
            score += agent.centrality_score * 0.15
        
        # Agent ID preference (lower IDs preferred) (15% weight)
        score += (100.0 - agent.agent_id) * 0.15
        
        return score
    
    def process_votes(self, agents):
        """Process voting from all agents"""
        if not self.election_in_progress:
            return False
        
        # Each agent votes for the candidate with highest score
        for agent in agents:
            if agent.agent_id in self.candidates:
                best_candidate = max(
                    self.candidates.items(),
                    key=lambda x: x[1]["score"]
                )
                
                if agent.agent_id not in self.votes:
                    self.votes[agent.agent_id] = best_candidate[0]
        
        return len(self.votes) >= len(agents) * 0.6  # 60% participation required
    
    def elect_alpha(self, agents):
        """Complete election and select alpha"""
        if not self.election_in_progress:
            return None
        
        # Count votes
        vote_counts = {}
        for voter_id, candidate_id in self.votes.items():
            vote_counts[candidate_id] = vote_counts.get(candidate_id, 0) + 1
        
        # Select winner
        if vote_counts:
            winner_id = max(vote_counts.items(), key=lambda x: x[1])[0]
            winner_agent = self.candidates[winner_id]["agent"]
            
            # Set roles
            for agent in agents:
                if agent.agent_id == winner_id:
                    agent.role = AgentRole.ALPHA
                else:
                    agent.role = AgentRole.FOLLOWER
            
            self.election_in_progress = False
            print(f"Agent {winner_id} elected as alpha with {vote_counts[winner_id]} votes")
            return winner_agent
        
        return None
    
    def is_election_timeout(self):
        """Check if election has timed out"""
        return (time.time() - self.election_start_time) > self.election_timeout

class TaskSharing:
    """Decentralized task sharing and assignment"""
    
    def __init__(self):
        self.available_tasks = {}
        self.assigned_tasks = {}
        self.task_counter = 0
    
    def announce_task(self, task_type, location, priority="medium", required_agents=1):
        """Announce a new task to the swarm"""
        self.task_counter += 1
        task_id = f"task_{self.task_counter}"
        
        task = {
            "id": task_id,
            "type": task_type,
            "location": location,
            "priority": priority,
            "required_agents": required_agents,
            "assigned_agents": [],
            "status": "available",
            "created_time": time.time()
        }
        
        self.available_tasks[task_id] = task
        print(f"Task {task_id} announced: {task_type} at {location}")
        return task_id
    
    def bid_for_task(self, agent, task_id):
        """Agent bids for a task"""
        if task_id not in self.available_tasks:
            return False
        
        task = self.available_tasks[task_id]
        
        # Calculate bid score based on agent capabilities and distance
        bid_score = self.calculate_bid_score(agent, task)
        
        if "bids" not in task:
            task["bids"] = {}
        
        task["bids"][agent.agent_id] = {
            "agent": agent,
            "score": bid_score,
            "bid_time": time.time()
        }
        
        return True
    
    def calculate_bid_score(self, agent, task):
        """Calculate bid score for agent-task pair"""
        score = 0.0
        
        # Distance factor (closer is better)
        if hasattr(agent, 'position') and 'location' in task:
            distance = math.sqrt(
                (agent.position.x - task["location"][0])**2 +
                (agent.position.y - task["location"][1])**2
            )
            score += max(0, 100 - distance)  # Max 100 points for distance
        
        # Battery level
        score += agent.battery_level * 0.5
        
        # Agent capabilities
        if task["type"] == TaskType.SEARCH and hasattr(agent, 'capabilities'):
            if "search" in agent.capabilities:
                score += 20
        
        if task["type"] == TaskType.RESCUE and hasattr(agent, 'capabilities'):
            if "rescue" in agent.capabilities:
                score += 20
        
        # Current workload (fewer tasks is better)
        current_tasks = len([t for t in self.assigned_tasks.values() 
                           if agent.agent_id in t.get("assigned_agents", [])])
        score -= current_tasks * 10
        
        return score
    
    def assign_tasks(self):
        """Assign tasks based on bids"""
        for task_id, task in list(self.available_tasks.items()):
            if "bids" in task and len(task["bids"]) > 0:
                # Sort bids by score
                sorted_bids = sorted(
                    task["bids"].items(),
                    key=lambda x: x[1]["score"],
                    reverse=True
                )
                
                # Assign to best bidders
                assigned_count = 0
                for agent_id, bid_info in sorted_bids:
                    if assigned_count < task["required_agents"]:
                        task["assigned_agents"].append(agent_id)
                        assigned_count += 1
                
                # Move to assigned tasks
                if len(task["assigned_agents"]) >= task["required_agents"]:
                    task["status"] = "assigned"
                    self.assigned_tasks[task_id] = task
                    del self.available_tasks[task_id]
                    
                    print(f"Task {task_id} assigned to agents {task['assigned_agents']}")
    
    def complete_task(self, task_id, success=True):
        """Mark task as completed"""
        if task_id in self.assigned_tasks:
            task = self.assigned_tasks[task_id]
            task["status"] = "completed" if success else "failed"
            task["completion_time"] = time.time()
            
            print(f"Task {task_id} {'completed' if success else 'failed'}")
            return True
        return False

class FormationControl:
    """Advanced formation control algorithms"""
    
    def __init__(self):
        self.formation_type = "none"
        self.formation_spacing = 50.0
        self.formation_center = (0.0, 0.0)
        self.target_positions = {}
    
    def set_formation(self, formation_type, agents, spacing=50.0, center=None):
        """Set formation for the swarm"""
        self.formation_type = formation_type
        self.formation_spacing = spacing
        
        if center is None:
            # Calculate center of mass
            total_x = sum(agent.position.x for agent in agents)
            total_y = sum(agent.position.y for agent in agents)
            self.formation_center = (total_x / len(agents), total_y / len(agents))
        else:
            self.formation_center = center
        
        # Calculate target positions
        self.target_positions = self.calculate_formation_positions(agents)
        
        print(f"Formation set: {formation_type} with {len(agents)} agents")
        return self.target_positions
    
    def calculate_formation_positions(self, agents):
        """Calculate target positions for current formation"""
        positions = {}
        agent_count = len(agents)
        cx, cy = self.formation_center
        
        if self.formation_type == "line":
            for i, agent in enumerate(agents):
                positions[agent.agent_id] = (
                    cx + (i - agent_count/2) * self.formation_spacing,
                    cy
                )
        
        elif self.formation_type == "circle":
            for i, agent in enumerate(agents):
                angle = 2 * math.pi * i / agent_count
                positions[agent.agent_id] = (
                    cx + self.formation_spacing * math.cos(angle),
                    cy + self.formation_spacing * math.sin(angle)
                )
        
        elif self.formation_type == "diamond":
            # Diamond formation for 4+ agents
            if agent_count >= 4:
                diamond_positions = [
                    (cx, cy - self.formation_spacing),      # Top
                    (cx + self.formation_spacing, cy),      # Right
                    (cx, cy + self.formation_spacing),      # Bottom
                    (cx - self.formation_spacing, cy),      # Left
                ]
                
                # Add additional agents in inner diamond
                if agent_count > 4:
                    for i in range(4, min(agent_count, 8)):
                        angle = 2 * math.pi * (i-4) / 4
                        diamond_positions.append((
                            cx + (self.formation_spacing * 0.5) * math.cos(angle),
                            cy + (self.formation_spacing * 0.5) * math.sin(angle)
                        ))
                
                for i, agent in enumerate(agents):
                    if i < len(diamond_positions):
                        positions[agent.agent_id] = diamond_positions[i]
        
        elif self.formation_type == "v_formation":
            for i, agent in enumerate(agents):
                if i == 0:
                    # Leader at the front
                    positions[agent.agent_id] = (cx, cy)
                else:
                    # Alternating sides
                    side = 1 if i % 2 == 1 else -1
                    row = (i + 1) // 2
                    positions[agent.agent_id] = (
                        cx - row * self.formation_spacing * 0.8,
                        cy + side * row * self.formation_spacing * 0.6
                    )
        
        return positions
    
    def update_formation(self, agents):
        """Update agent positions to maintain formation"""
        if self.formation_type == "none":
            return
        
        for agent in agents:
            if agent.agent_id in self.target_positions:
                target_x, target_y = self.target_positions[agent.agent_id]
                
                # Calculate movement vector
                dx = target_x - agent.position.x
                dy = target_y - agent.position.y
                distance = math.sqrt(dx*dx + dy*dy)
                
                if distance > 5.0:  # Move if not close enough
                    # Normalize and scale movement
                    max_speed = 2.0
                    if distance > 0:
                        agent.velocity.x = (dx / distance) * max_speed
                        agent.velocity.y = (dy / distance) * max_speed
                else:
                    # Slow down when close
                    agent.velocity.x *= 0.8
                    agent.velocity.y *= 0.8
    
    def get_formation_error(self, agents):
        """Calculate formation error (how far agents are from target positions)"""
        total_error = 0.0
        
        for agent in agents:
            if agent.agent_id in self.target_positions:
                target_x, target_y = self.target_positions[agent.agent_id]
                error = math.sqrt(
                    (agent.position.x - target_x)**2 +
                    (agent.position.y - target_y)**2
                )
                total_error += error
        
        return total_error / len(agents) if agents else 0.0

class ConsensusDecisionMaking:
    """Consensus-based decision making for the swarm"""
    
    def __init__(self):
        self.proposals = {}
        self.votes = {}
        self.decisions = {}
        self.consensus_threshold = 0.7  # 70% agreement required
    
    def propose_decision(self, proposer_id, decision_type, options, description=""):
        """Propose a decision to the swarm"""
        proposal_id = f"proposal_{int(time.time())}_{proposer_id}"
        
        proposal = {
            "id": proposal_id,
            "proposer": proposer_id,
            "type": decision_type,
            "options": options,
            "description": description,
            "created_time": time.time(),
            "votes": {},
            "status": "voting"
        }
        
        self.proposals[proposal_id] = proposal
        print(f"Decision proposed: {decision_type} by agent {proposer_id}")
        return proposal_id
    
    def vote_on_proposal(self, proposal_id, voter_id, choice, reasoning=""):
        """Vote on a proposal"""
        if proposal_id not in self.proposals:
            return False
        
        proposal = self.proposals[proposal_id]
        if proposal["status"] != "voting":
            return False
        
        proposal["votes"][voter_id] = {
            "choice": choice,
            "reasoning": reasoning,
            "vote_time": time.time()
        }
        
        return True
    
    def check_consensus(self, proposal_id, total_agents):
        """Check if consensus has been reached"""
        if proposal_id not in self.proposals:
            return False, None
        
        proposal = self.proposals[proposal_id]
        votes = proposal["votes"]
        
        if len(votes) < total_agents * 0.6:  # Need at least 60% participation
            return False, None
        
        # Count votes for each option
        vote_counts = {}
        for vote_info in votes.values():
            choice = vote_info["choice"]
            vote_counts[choice] = vote_counts.get(choice, 0) + 1
        
        # Check if any option has consensus
        for option, count in vote_counts.items():
            if count / len(votes) >= self.consensus_threshold:
                proposal["status"] = "decided"
                proposal["decision"] = option
                proposal["decision_time"] = time.time()
                
                self.decisions[proposal_id] = proposal
                print(f"Consensus reached: {option} for proposal {proposal_id}")
                return True, option
        
        return False, None
    
    def get_active_proposals(self):
        """Get all active proposals"""
        return {pid: p for pid, p in self.proposals.items() 
                if p["status"] == "voting"}

# Utility functions for coordination
def calculate_swarm_center(agents):
    """Calculate the center point of the swarm"""
    if not agents:
        return (0.0, 0.0)
    
    total_x = sum(agent.position.x for agent in agents)
    total_y = sum(agent.position.y for agent in agents)
    return (total_x / len(agents), total_y / len(agents))

def calculate_swarm_spread(agents):
    """Calculate how spread out the swarm is"""
    if len(agents) < 2:
        return 0.0
    
    center_x, center_y = calculate_swarm_center(agents)
    
    total_distance = 0.0
    for agent in agents:
        distance = math.sqrt(
            (agent.position.x - center_x)**2 +
            (agent.position.y - center_y)**2
        )
        total_distance += distance
    
    return total_distance / len(agents)

def find_nearest_agents(agent, all_agents, max_distance=150.0):
    """Find agents within communication range"""
    nearby = []
    
    for other_agent in all_agents:
        if other_agent.agent_id != agent.agent_id:
            distance = math.sqrt(
                (agent.position.x - other_agent.position.x)**2 +
                (agent.position.y - other_agent.position.y)**2
            )
            
            if distance <= max_distance:
                nearby.append((other_agent, distance))
    
    # Sort by distance
    nearby.sort(key=lambda x: x[1])
    return [agent for agent, _ in nearby]
```

### **5. Simulation Environment**

#### **Simulation Environment (simulation_environment.py)**
```python
#!/usr/bin/env python3
"""
2D Simulation Environment for Swarm Rover AI
Real-time physics-based simulation with visualization
"""

import pygame
import math
import random
import json
import time
from enum import Enum
from typing import List, Tuple, Dict, Optional
import numpy as np

# Import coordination algorithms
from coordination_algorithms import AgentRole, AgentState, TaskType, AgentCapabilities
from coordination_algorithms import AlphaElection, TaskSharing, FormationControl, ConsensusDecisionMaking

class SimulationAgent:
    """Agent representation in simulation"""
    
    def __init__(self, agent_id: int, x: float, y: float):
        self.agent_id = agent_id
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.role = AgentRole.FOLLOWER
        self.state = AgentState.IDLE
        self.battery_level = 100.0
        self.capabilities = AgentCapabilities()
        self.target_x = x
        self.target_y = y
        self.communication_range = 150.0
        self.max_speed = 2.0
        self.radius = 15
        self.color = (0, 100, 255)  # Blue for followers
        self.discovered_targets = []
        self.current_task = None
        self.uptime = 0.0
        
        # Physics properties
        self.mass = 1.0
        self.friction = 0.95
        
        # Sensors
        self.sensor_range = 100.0
        self.detected_obstacles = []
        self.detected_agents = []
        
    def update(self, dt: float, obstacles: List, targets: List, other_agents: List):
        """Update agent state and physics"""
        self.uptime += dt
        
        # Update sensors
        self.update_sensors(obstacles, targets, other_agents)
        
        # Update behavior based on state
        if self.state == AgentState.IDLE:
            self.idle_behavior()
        elif self.state == AgentState.SEARCHING:
            self.search_behavior()
        elif self.state == AgentState.MOVING_TO_TARGET:
            self.move_to_target_behavior()
        elif self.state == AgentState.FORMING_UP:
            self.formation_behavior()
        
        # Apply obstacle avoidance
        self.avoid_obstacles()
        
        # Update physics
        self.update_physics(dt)
        
        # Update battery
        self.battery_level -= 0.01 * dt  # Battery drain
        
        # Update visual appearance
        self.update_appearance()
    
    def update_sensors(self, obstacles, targets, other_agents):
        """Update sensor readings"""
        self.detected_obstacles = []
        self.detected_agents = []
        
        # Detect obstacles
        for obstacle in obstacles:
            distance = self.distance_to_rect(obstacle)
            if distance <= self.sensor_range:
                self.detected_obstacles.append(obstacle)
        
        # Detect other agents
        for agent in other_agents:
            if agent.agent_id != self.agent_id:
                distance = math.sqrt((self.x - agent.x)**2 + (self.y - agent.y)**2)
                if distance <= self.communication_range:
                    self.detected_agents.append(agent)
        
        # Detect targets
        for target in targets:
            distance = math.sqrt((self.x - target[0])**2 + (self.y - target[1])**2)
            if distance <= self.sensor_range:
                if target not in self.discovered_targets:
                    self.discovered_targets.append(target)
    
    def idle_behavior(self):
        """Behavior when agent is idle"""
        # Random movement if no specific task
        if random.random() < 0.01:  # 1% chance per frame
            self.target_x = self.x + random.uniform(-100, 100)
            self.target_y = self.y + random.uniform(-100, 100)
    
    def search_behavior(self):
        """Behavior when agent is searching"""
        # Implement search pattern (spiral, grid, random walk)
        if abs(self.x - self.target_x) < 10 and abs(self.y - self.target_y) < 10:
            # Reached current search point, pick new one
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(50, 150)
            self.target_x = self.x + distance * math.cos(angle)
            self.target_y = self.y + distance * math.sin(angle)
    
    def move_to_target_behavior(self):
        """Behavior when moving to specific target"""
        distance = math.sqrt((self.target_x - self.x)**2 + (self.target_y - self.y)**2)
        if distance < 20:
            self.state = AgentState.IDLE
            self.vx *= 0.5
            self.vy *= 0.5
    
    def formation_behavior(self):
        """Behavior when maintaining formation"""
        # Move towards formation position
        self.move_to_target_behavior()
    
    def avoid_obstacles(self):
        """Implement obstacle avoidance"""
        avoidance_force_x = 0.0
        avoidance_force_y = 0.0
        
        for obstacle in self.detected_obstacles:
            # Calculate repulsive force from obstacle
            closest_point = self.closest_point_on_rect(obstacle)
            dx = self.x - closest_point[0]
            dy = self.y - closest_point[1]
            distance = math.sqrt(dx*dx + dy*dy)
            
            if distance < 50:  # Avoidance threshold
                if distance > 0:
                    force_magnitude = (50 - distance) / 50 * 3.0
                    avoidance_force_x += (dx / distance) * force_magnitude
                    avoidance_force_y += (dy / distance) * force_magnitude
        
        # Apply avoidance force to velocity
        self.vx += avoidance_force_x * 0.1
        self.vy += avoidance_force_y * 0.1
    
    def update_physics(self, dt: float):
        """Update physics simulation"""
        # Calculate desired velocity towards target
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > 5:
            desired_vx = (dx / distance) * self.max_speed
            desired_vy = (dy / distance) * self.max_speed
            
            # Apply steering force
            steering_force = 0.1
            self.vx += (desired_vx - self.vx) * steering_force
            self.vy += (desired_vy - self.vy) * steering_force
        
        # Apply friction
        self.vx *= self.friction
        self.vy *= self.friction
        
        # Limit speed
        speed = math.sqrt(self.vx*self.vx + self.vy*self.vy)
        if speed > self.max_speed:
            self.vx = (self.vx / speed) * self.max_speed
            self.vy = (self.vy / speed) * self.max_speed
        
        # Update position
        self.x += self.vx * dt * 60  # 60 FPS normalization
        self.y += self.vy * dt * 60
    
    def update_appearance(self):
        """Update visual appearance based on role and state"""
        if self.role == AgentRole.ALPHA:
            self.color = (255, 215, 0)  # Gold
            self.radius = 20
        elif self.role == AgentRole.SCOUT:
            self.color = (0, 255, 0)  # Green
            self.radius = 12
        else:
            self.color = (0, 100, 255)  # Blue
            self.radius = 15
        
        # Modify color based on state
        if self.state == AgentState.SEARCHING:
            # Add red tint when searching
            r, g, b = self.color
            self.color = (min(255, r + 50), g, b)
    
    def distance_to_rect(self, rect):
        """Calculate distance to rectangle obstacle"""
        x, y, w, h = rect
        closest_point = self.closest_point_on_rect(rect)
        return math.sqrt((self.x - closest_point[0])**2 + (self.y - closest_point[1])**2)
    
    def closest_point_on_rect(self, rect):
        """Find closest point on rectangle to agent"""
        x, y, w, h = rect
        closest_x = max(x, min(self.x, x + w))
        closest_y = max(y, min(self.y, y + h))
        return (closest_x, closest_y)
    
    def draw(self, screen):
        """Draw agent on screen"""
        # Draw communication range (faint circle)
        pygame.draw.circle(screen, (50, 50, 50), 
                         (int(self.x), int(self.y)), 
                         int(self.communication_range), 1)
        
        # Draw sensor range
        if self.state == AgentState.SEARCHING:
            pygame.draw.circle(screen, (100, 100, 0), 
                             (int(self.x), int(self.y)), 
                             int(self.sensor_range), 1)
        
        # Draw agent body
        pygame.draw.circle(screen, self.color, 
                         (int(self.x), int(self.y)), self.radius)
        
        # Draw agent ID
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.agent_id), True, (255, 255, 255))
        text_rect = text.get_rect(center=(int(self.x), int(self.y)))
        screen.blit(text, text_rect)
        
        # Draw role indicator
        if self.role == AgentRole.ALPHA:
            # Draw crown for alpha
            crown_points = [
                (self.x - 10, self.y - 25),
                (self.x - 5, self.y - 35),
                (self.x, self.y - 30),
                (self.x + 5, self.y - 35),
                (self.x + 10, self.y - 25)
            ]
            pygame.draw.polygon(screen, (255, 215, 0), crown_points)
        
        # Draw velocity vector
        if abs(self.vx) > 0.1 or abs(self.vy) > 0.1:
            end_x = self.x + self.vx * 10
            end_y = self.y + self.vy * 10
            pygame.draw.line(screen, (255, 255, 255), 
                           (self.x, self.y), (end_x, end_y), 2)
        
        # Draw battery level
        battery_width = 30
        battery_height = 5
        battery_x = self.x - battery_width // 2
        battery_y = self.y + self.radius + 5
        
        # Battery outline
        pygame.draw.rect(screen, (255, 255, 255), 
                        (battery_x, battery_y, battery_width, battery_height), 1)
        
        # Battery fill
        fill_width = int((self.battery_level / 100.0) * (battery_width - 2))
        if fill_width > 0:
            battery_color = (0, 255, 0) if self.battery_level > 50 else \
                           (255, 255, 0) if self.battery_level > 20 else (255, 0, 0)
            pygame.draw.rect(screen, battery_color,
                           (battery_x + 1, battery_y + 1, fill_width, battery_height - 2))

class SwarmSimulation:
    """Main simulation environment"""
    
    def __init__(self, width=1200, height=800, num_agents=8):
        self.width = width
        self.height = height
        self.num_agents = num_agents
        
        # Initialize pygame
        pygame.init()
        self.screen = None
        self.clock = pygame.time.Clock()
        self.running = False
        
        # Simulation objects
        self.agents = []
        self.obstacles = []
        self.targets = []
        self.discovered_targets = []
        
        # Coordination systems
        self.alpha_election = AlphaElection()
        self.task_sharing = TaskSharing()
        self.formation_control = FormationControl()
        self.consensus_system = ConsensusDecisionMaking()
        
        # Simulation state
        self.simulation_time = 0.0
        self.frame_count = 0
        self.fps = 60
        
        # Performance metrics
        self.metrics = {
            "mission_success_rate": 0.0,
            "formation_accuracy": 0.0,
            "communication_efficiency": 0.0,
            "average_response_time": 0.0,
            "targets_found": 0,
            "total_targets": 0
        }
        
        # Initialize agents
        self.create_agents()
        
        # Start with alpha election
        self.alpha_election.start_election(self.agents)
    
    def create_agents(self):
        """Create initial agent population"""
        self.agents = []
        
        for i in range(self.num_agents):
            # Random initial positions
            x = random.uniform(100, self.width - 100)
            y = random.uniform(100, self.height - 100)
            
            agent = SimulationAgent(i + 1, x, y)
            self.agents.append(agent)
        
        print(f"Created {len(self.agents)} agents")
    
    def setup_display(self):
        """Setup pygame display"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Swarm Rover AI Simulation")
        self.running = True
    
    def add_obstacles(self, obstacle_list):
        """Add obstacles to simulation"""
        self.obstacles = obstacle_list
        print(f"Added {len(obstacle_list)} obstacles")
    
    def add_targets(self, target_list):
        """Add targets to simulation"""
        self.targets = target_list
        self.metrics["total_targets"] = len(target_list)
        print(f"Added {len(target_list)} targets")
    
    def load_scenario(self, scenario_file):
        """Load scenario from JSON file"""
        try:
            with open(scenario_file, 'r') as f:
                scenario = json.load(f)
            
            # Load obstacles
            if "obstacles" in scenario:
                self.add_obstacles(scenario["obstacles"])
            
            # Load targets
            if "targets" in scenario:
                self.add_targets(scenario["targets"])
            
            # Load agent configurations
            if "agents" in scenario:
                agent_configs = scenario["agents"]
                for i, config in enumerate(agent_configs):
                    if i < len(self.agents):
                        agent = self.agents[i]
                        agent.x = config.get("x", agent.x)
                        agent.y = config.get("y", agent.y)
                        agent.role = AgentRole(config.get("role", "follower"))
            
            print(f"Loaded scenario: {scenario.get('name', 'Unknown')}")
            return True
            
        except Exception as e:
            print(f"Error loading scenario: {e}")
            return False
    
    def update(self):
        """Update simulation state"""
        dt = 1.0 / self.fps
        self.simulation_time += dt
        self.frame_count += 1
        
        # Update agents
        for agent in self.agents:
            agent.update(dt, self.obstacles, self.targets, self.agents)
        
        # Update coordination systems
        self.update_coordination()
        
        # Check for target discoveries
        self.check_target_discoveries()
        
        # Update metrics
        self.update_metrics()
        
        # Handle events
        self.handle_events()
    
    def update_coordination(self):
        """Update coordination algorithms"""
        # Process alpha election
        if self.alpha_election.election_in_progress:
            if self.alpha_election.process_votes(self.agents):
                self.alpha_election.elect_alpha(self.agents)
        
        # Process task sharing
        self.task_sharing.assign_tasks()
        
        # Update formation control
        if self.formation_control.formation_type != "none":
            self.formation_control.update_formation(self.agents)
    
    def check_target_discoveries(self):
        """Check if agents have discovered targets"""
        for agent in self.agents:
            for target in self.targets:
                distance = math.sqrt((agent.x - target[0])**2 + (agent.y - target[1])**2)
                if distance < 30 and target not in self.discovered_targets:
                    self.discovered_targets.append(target)
                    self.metrics["targets_found"] += 1
                    print(f"Agent {agent.agent_id} discovered target at {target}")
                    
                    # Remove discovered target
                    if target in self.targets:
                        self.targets.remove(target)
    
    def update_metrics(self):
        """Update performance metrics"""
        if self.metrics["total_targets"] > 0:
            self.metrics["mission_success_rate"] = \
                (self.metrics["targets_found"] / self.metrics["total_targets"]) * 100
        
        # Calculate formation accuracy
        if self.formation_control.formation_type != "none":
            formation_error = self.formation_control.get_formation_error(self.agents)
            self.metrics["formation_accuracy"] = max(0, 100 - formation_error)
        
        # Calculate communication efficiency
        total_agents = len(self.agents)
        connected_agents = 0
        for agent in self.agents:
            if len(agent.detected_agents) > 0:
                connected_agents += 1
        
        if total_agents > 0:
            self.metrics["communication_efficiency"] = \
                (connected_agents / total_agents) * 100
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_keypress(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event.pos, event.button)
    
    def handle_keypress(self, key):
        """Handle keyboard input"""
        if key == pygame.K_SPACE:
            # Pause/unpause simulation
            pass
        elif key == pygame.K_r:
            # Reset simulation
            self.reset_simulation()
        elif key == pygame.K_e:
            # Start alpha election
            self.alpha_election.start_election(self.agents)
        elif key == pygame.K_f:
            # Cycle formation types
            formations = ["none", "line", "circle", "diamond", "v_formation"]
            current_idx = formations.index(self.formation_control.formation_type)
            next_formation = formations[(current_idx + 1) % len(formations)]
            if next_formation != "none":
                self.formation_control.set_formation(next_formation, self.agents)
            else:
                self.formation_control.formation_type = "none"
    
    def handle_mouse_click(self, pos, button):
        """Handle mouse clicks"""
        x, y = pos
        
        if button == 1:  # Left click - add target
            self.targets.append((x, y))
            self.metrics["total_targets"] += 1
            print(f"Added target at ({x}, {y})")
        elif button == 3:  # Right click - add obstacle
            self.obstacles.append((x - 25, y - 25, 50, 50))
            print(f"Added obstacle at ({x}, {y})")
    
    def render(self):
        """Render simulation"""
        if self.screen is None:
            return
        
        # Clear screen
        self.screen.fill((20, 20, 40))  # Dark blue background
        
        # Draw obstacles
        for obstacle in self.obstacles:
            pygame.draw.rect(self.screen, (139, 69, 19), obstacle)  # Brown
            pygame.draw.rect(self.screen, (160, 82, 45), obstacle, 2)  # Outline
        
        # Draw targets
        for i, target in enumerate(self.targets):
            pygame.draw.circle(self.screen, (255, 0, 0), target, 20)  # Red
            pygame.draw.circle(self.screen, (255, 255, 255), target, 20, 2)  # White outline
            
            # Target label
            font = pygame.font.Font(None, 24)
            text = font.render(f"T{i+1}", True, (255, 255, 255))
            text_rect = text.get_rect(center=target)
            self.screen.blit(text, text_rect)
        
        # Draw discovered targets
        for i, target in enumerate(self.discovered_targets):
            pygame.draw.circle(self.screen, (0, 255, 0), target, 25)  # Green
            pygame.draw.circle(self.screen, (255, 255, 255), target, 25, 2)
            
            font = pygame.font.Font(None, 24)
            text = font.render("✓", True, (255, 255, 255))
            text_rect = text.get_rect(center=target)
            self.screen.blit(text, text_rect)
        
        # Draw agents
        for agent in self.agents:
            agent.draw(self.screen)
        
        # Draw UI
        self.draw_ui()
    
    def draw_ui(self):
        """Draw user interface"""
        font_large = pygame.font.Font(None, 36)
        font_medium = pygame.font.Font(None, 28)
        font_small = pygame.font.Font(None, 24)
        
        # Title
        title = font_large.render("Swarm Rover AI Simulation", True, (255, 255, 255))
        self.screen.blit(title, (10, 10))
        
        # Simulation info
        info_y = 50
        info_texts = [
            f"Time: {self.simulation_time:.1f}s",
            f"Agents: {len(self.agents)}",
            f"Targets: {len(self.targets)} remaining, {len(self.discovered_targets)} found",
            f"Formation: {self.formation_control.formation_type}",
        ]
        
        for text in info_texts:
            rendered = font_medium.render(text, True, (255, 255, 255))
            self.screen.blit(rendered, (10, info_y))
            info_y += 25
        
        # Performance metrics
        metrics_y = info_y + 20
        metrics_title = font_medium.render("Performance Metrics:", True, (255, 215, 0))
        self.screen.blit(metrics_title, (10, metrics_y))
        metrics_y += 30
        
        metric_texts = [
            f"Mission Success: {self.metrics['mission_success_rate']:.1f}%",
            f"Formation Accuracy: {self.metrics['formation_accuracy']:.1f}%",
            f"Communication: {self.metrics['communication_efficiency']:.1f}%",
        ]
        
        for text in metric_texts:
            rendered = font_small.render(text, True, (200, 200, 200))
            self.screen.blit(rendered, (10, metrics_y))
            metrics_y += 20
        
        # Alpha agent info
        alpha_agents = [a for a in self.agents if a.role == AgentRole.ALPHA]
        if alpha_agents:
            alpha = alpha_agents[0]
            alpha_text = font_medium.render(f"Alpha: Agent {alpha.agent_id}", True, (255, 215, 0))
            self.screen.blit(alpha_text, (10, metrics_y + 10))
        
        # Controls
        controls_y = self.height - 100
        controls_title = font_small.render("Controls:", True, (255, 255, 255))
        self.screen.blit(controls_title, (10, controls_y))
        
        control_texts = [
            "R - Reset | E - Election | F - Formation",
            "Left Click - Add Target | Right Click - Add Obstacle"
        ]
        
        for i, text in enumerate(control_texts):
            rendered = font_small.render(text, True, (180, 180, 180))
            self.screen.blit(rendered, (10, controls_y + 20 + i * 15))
    
    def reset_simulation(self):
        """Reset simulation to initial state"""
        self.simulation_time = 0.0
        self.frame_count = 0
        self.discovered_targets = []
        self.metrics["targets_found"] = 0
        
        # Reset agents
        for agent in self.agents:
            agent.x = random.uniform(100, self.width - 100)
            agent.y = random.uniform(100, self.height - 100)
            agent.vx = 0.0
            agent.vy = 0.0
            agent.battery_level = 100.0
            agent.state = AgentState.IDLE
            agent.role = AgentRole.FOLLOWER
            agent.discovered_targets = []
        
        # Reset coordination systems
        self.formation_control.formation_type = "none"
        self.alpha_election = AlphaElection()
        self.task_sharing = TaskSharing()
        
        print("Simulation reset")
    
    def run(self):
        """Run simulation loop"""
        if self.screen is None:
            self.setup_display()
        
        while self.running:
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(self.fps)
        
        self.cleanup()
    
    def cleanup(self):
        """Cleanup simulation"""
        pygame.quit()
        print("Simulation ended")

def main():
    """Main function for testing simulation"""
    # Create simulation
    sim = SwarmSimulation(width=1200, height=800, num_agents=8)
    
    # Add some obstacles and targets for testing
    sim.add_obstacles([
        (300, 200, 100, 50),   # Building 1
        (700, 400, 80, 80),    # Building 2
        (500, 600, 120, 40),   # Building 3
    ])
    
    sim.add_targets([
        (150, 150),  # Target 1
        (900, 700),  # Target 2
        (600, 300),  # Target 3
    ])
    
    # Run simulation
    sim.run()

if __name__ == "__main__":
    main()
```

### **6. Testing Framework**

#### **Testing Framework (testing_framework.py)**
```python
#!/usr/bin/env python3
"""
Comprehensive Testing Framework for Swarm Rover AI
Automated testing, validation, and performance analysis
"""

import unittest
import time
import json
import math
import statistics
from typing import List, Dict, Any, Tuple
import numpy as np
import matplotlib.pyplot as plt

# Import system components
from simulation_environment import SwarmSimulation, SimulationAgent
from coordination_algorithms import AlphaElection, TaskSharing, FormationControl
from coordination_algorithms import AgentRole, AgentState, TaskType

class SwarmTestCase(unittest.TestCase):
    """Base test case for swarm testing"""
    
    def setUp(self):
        """Set up test environment"""
        self.simulation = SwarmSimulation(width=800, height=600, num_agents=6)
        self.test_results = {}
        self.performance_metrics = {}
    
    def tearDown(self):
        """Clean up after test"""
        if hasattr(self.simulation, 'cleanup'):
            self.simulation.cleanup()

class TestBasicFunctionality(SwarmTestCase):
    """Test basic system functionality"""
    
    def test_agent_creation(self):
        """Test agent creation and initialization"""
        self.assertEqual(len(self.simulation.agents), 6)
        
        for agent in self.simulation.agents:
            self.assertIsInstance(agent, SimulationAgent)
            self.assertGreater(agent.agent_id, 0)
            self.assertEqual(agent.role, AgentRole.FOLLOWER)
            self.assertEqual(agent.state, AgentState.IDLE)
            self.assertEqual(agent.battery_level, 100.0)
    
    def test_agent_movement(self):
        """Test agent movement and physics"""
        agent = self.simulation.agents[0]
        initial_x, initial_y = agent.x, agent.y
        
        # Set target position
        agent.target_x = initial_x + 100
        agent.target_y = initial_y + 100
        agent.state = AgentState.MOVING_TO_TARGET
        
        # Update for several frames
        for _ in range(100):
            agent.update(1/60, [], [], [])
        
        # Agent should have moved towards target
        self.assertNotEqual(agent.x, initial_x)
        self.assertNotEqual(agent.y, initial_y)
        
        # Should be closer to target
        final_distance = math.sqrt((agent.x - agent.target_x)**2 + (agent.y - agent.target_y)**2)
        initial_distance = math.sqrt((initial_x - agent.target_x)**2 + (initial_y - agent.target_y)**2)
        self.assertLess(final_distance, initial_distance)
    
    def test_obstacle_avoidance(self):
        """Test obstacle avoidance behavior"""
        agent = self.simulation.agents[0]
        agent.x, agent.y = 100, 100
        
        # Place obstacle in path
        obstacle = (120, 100, 50, 50)
        self.simulation.add_obstacles([obstacle])
        
        # Set target beyond obstacle
        agent.target_x = 200
        agent.target_y = 100
        agent.state = AgentState.MOVING_TO_TARGET
        
        # Update and check avoidance
        for _ in range(200):
            agent.update(1/60, [obstacle], [], [])
        
        # Agent should avoid obstacle (not be inside it)
        self.assertFalse(120 <= agent.x <= 170 and 100 <= agent.y <= 150)

class TestCoordinationAlgorithms(SwarmTestCase):
    """Test swarm coordination algorithms"""
    
    def test_alpha_election(self):
        """Test alpha agent election process"""
        election = AlphaElection()
        agents = self.simulation.agents
        
        # Start election
        self.assertTrue(election.start_election(agents))
        self.assertTrue(election.election_in_progress)
        
        # Process votes
        self.assertTrue(election.process_votes(agents))
        
        # Elect alpha
        alpha_agent = election.elect_alpha(agents)
        self.assertIsNotNone(alpha_agent)
        self.assertEqual(alpha_agent.role, AgentRole.ALPHA)
        
        # Check that only one alpha exists
        alpha_count = sum(1 for agent in agents if agent.role == AgentRole.ALPHA)
        self.assertEqual(alpha_count, 1)
    
    def test_formation_control(self):
        """Test formation control algorithms"""
        formation = FormationControl()
        agents = self.simulation.agents
        
        # Test line formation
        positions = formation.set_formation("line", agents, spacing=50)
        self.assertEqual(len(positions), len(agents))
        
        # Update formation
        for _ in range(100):
            formation.update_formation(agents)
            for agent in agents:
                agent.update(1/60, [], [], [])
        
        # Check formation accuracy
        error = formation.get_formation_error(agents)
        self.assertLess(error, 20.0)  # Should be reasonably accurate
    
    def test_task_sharing(self):
        """Test decentralized task sharing"""
        task_system = TaskSharing()
        agents = self.simulation.agents
        
        # Announce task
        task_id = task_system.announce_task(
            TaskType.SEARCH, (400, 300), "high", required_agents=2
        )
        self.assertIsNotNone(task_id)
        
        # Agents bid for task
        for agent in agents[:3]:  # First 3 agents bid
            self.assertTrue(task_system.bid_for_task(agent, task_id))
        
        # Assign tasks
        task_system.assign_tasks()
        
        # Check assignment
        task = task_system.assigned_tasks.get(task_id)
        self.assertIsNotNone(task)
        self.assertEqual(len(task["assigned_agents"]), 2)

class TestMissionScenarios(SwarmTestCase):
    """Test complete mission scenarios"""
    
    def test_search_and_rescue_mission(self):
        """Test search and rescue mission scenario"""
        # Set up scenario
        self.simulation.add_obstacles([
            (200, 150, 80, 60),
            (500, 300, 100, 80)
        ])
        
        targets = [(100, 100), (600, 400), (300, 500)]
        self.simulation.add_targets(targets)
        
        # Set agents to search mode
        for agent in self.simulation.agents:
            agent.state = AgentState.SEARCHING
        
        # Run simulation
        start_time = time.time()
        max_duration = 30.0  # 30 seconds max
        
        while (len(self.simulation.discovered_targets) < len(targets) and 
               time.time() - start_time < max_duration):
            self.simulation.update()
            time.sleep(0.01)  # Small delay for real-time feel
        
        # Evaluate results
        success_rate = len(self.simulation.discovered_targets) / len(targets)
        self.assertGreater(success_rate, 0.5)  # At least 50% success
        
        self.performance_metrics['search_rescue_success_rate'] = success_rate
        self.performance_metrics['search_rescue_time'] = time.time() - start_time
    
    def test_formation_mission(self):
        """Test formation flying mission"""
        formation = FormationControl()
        agents = self.simulation.agents
        
        formations_to_test = ["line", "circle", "diamond", "v_formation"]
        formation_accuracies = []
        
        for formation_type in formations_to_test:
            # Set formation
            formation.set_formation(formation_type, agents, spacing=60)
            
            # Allow time to form up
            for _ in range(200):
                formation.update_formation(agents)
                for agent in agents:
                    agent.update(1/60, [], [], [])
            
            # Measure accuracy
            error = formation.get_formation_error(agents)
            accuracy = max(0, 100 - error)
            formation_accuracies.append(accuracy)
        
        # All formations should achieve reasonable accuracy
        avg_accuracy = statistics.mean(formation_accuracies)
        self.assertGreater(avg_accuracy, 70.0)  # 70% average accuracy
        
        self.performance_metrics['formation_accuracy'] = avg_accuracy

class TestPerformanceMetrics(SwarmTestCase):
    """Test performance and scalability"""
    
    def test_communication_efficiency(self):
        """Test communication system efficiency"""
        agents = self.simulation.agents
        
        # Spread agents across area
        for i, agent in enumerate(agents):
            agent.x = (i % 3) * 200 + 100
            agent.y = (i // 3) * 200 + 100
        
        # Update and measure connectivity
        connected_pairs = 0
        total_pairs = 0
        
        for i, agent1 in enumerate(agents):
            for j, agent2 in enumerate(agents[i+1:], i+1):
                total_pairs += 1
                distance = math.sqrt((agent1.x - agent2.x)**2 + (agent1.y - agent2.y)**2)
                if distance <= agent1.communication_range:
                    connected_pairs += 1
        
        connectivity = connected_pairs / total_pairs if total_pairs > 0 else 0
        self.assertGreater(connectivity, 0.3)  # At least 30% connectivity
        
        self.performance_metrics['communication_efficiency'] = connectivity
    
    def test_scalability(self):
        """Test system scalability with different agent counts"""
        agent_counts = [4, 8, 12, 16]
        performance_times = []
        
        for count in agent_counts:
            # Create simulation with specific agent count
            sim = SwarmSimulation(width=800, height=600, num_agents=count)
            
            # Measure update time
            start_time = time.time()
            for _ in range(100):  # 100 updates
                sim.update()
            update_time = time.time() - start_time
            
            performance_times.append(update_time)
            sim.cleanup()
        
        # Performance should scale reasonably
        # Time per agent should not increase dramatically
        time_per_agent = [t/c for t, c in zip(performance_times, agent_counts)]
        
        # Check that performance doesn't degrade too much
        self.assertLess(max(time_per_agent) / min(time_per_agent), 3.0)
        
        self.performance_metrics['scalability_factor'] = max(time_per_agent) / min(time_per_agent)

class TestRobustness(SwarmTestCase):
    """Test system robustness and fault tolerance"""
    
    def test_agent_failure_recovery(self):
        """Test recovery from agent failures"""
        agents = self.simulation.agents
        
        # Elect alpha
        election = AlphaElection()
        election.start_election(agents)
        election.process_votes(agents)
        alpha = election.elect_alpha(agents)
        
        # Remove alpha agent (simulate failure)
        original_alpha_id = alpha.agent_id
        self.simulation.agents = [a for a in agents if a.agent_id != original_alpha_id]
        
        # Start new election
        election = AlphaElection()
        election.start_election(self.simulation.agents)
        election.process_votes(self.simulation.agents)
        new_alpha = election.elect_alpha(self.simulation.agents)
        
        # Should have new alpha
        self.assertIsNotNone(new_alpha)
        self.assertNotEqual(new_alpha.agent_id, original_alpha_id)
    
    def test_communication_disruption(self):
        """Test behavior under communication disruption"""
        agents = self.simulation.agents
        
        # Reduce communication range to simulate disruption
        original_ranges = [agent.communication_range for agent in agents]
        for agent in agents:
            agent.communication_range = 50.0  # Reduced range
        
        # Test formation under poor communication
        formation = FormationControl()
        formation.set_formation("circle", agents, spacing=80)
        
        # Update formation
        for _ in range(150):
            formation.update_formation(agents)
            for agent in agents:
                agent.update(1/60, [], [], [])
        
        # Should still achieve some formation accuracy
        error = formation.get_formation_error(agents)
        self.assertLess(error, 50.0)  # Relaxed accuracy under disruption
        
        # Restore original ranges
        for agent, original_range in zip(agents, original_ranges):
            agent.communication_range = original_range

class PerformanceAnalyzer:
    """Analyze and report performance metrics"""
    
    def __init__(self):
        self.test_results = {}
        self.benchmark_data = {}
    
    def run_comprehensive_tests(self):
        """Run all test suites and collect results"""
        test_suites = [
            TestBasicFunctionality,
            TestCoordinationAlgorithms,
            TestMissionScenarios,
            TestPerformanceMetrics,
            TestRobustness
        ]
        
        all_results = {}
        
        for suite_class in test_suites:
            suite = unittest.TestLoader().loadTestsFromTestCase(suite_class)
            runner = unittest.TextTestRunner(verbosity=2)
            result = runner.run(suite)
            
            suite_name = suite_class.__name__
            all_results[suite_name] = {
                'tests_run': result.testsRun,
                'failures': len(result.failures),
                'errors': len(result.errors),
                'success_rate': (result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100
            }
        
        self.test_results = all_results
        return all_results
    
    def generate_performance_report(self, output_file="performance_report.json"):
        """Generate comprehensive performance report"""
        report = {
            'timestamp': time.time(),
            'test_results': self.test_results,
            'performance_metrics': self.benchmark_data,
            'summary': self.calculate_summary_metrics()
        }
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"Performance report saved to {output_file}")
        return report
    
    def calculate_summary_metrics(self):
        """Calculate overall summary metrics"""
        if not self.test_results:
            return {}
        
        total_tests = sum(suite['tests_run'] for suite in self.test_results.values())
        total_failures = sum(suite['failures'] for suite in self.test_results.values())
        total_errors = sum(suite['errors'] for suite in self.test_results.values())
        
        overall_success_rate = (total_tests - total_failures - total_errors) / total_tests * 100
        
        return {
            'total_tests': total_tests,
            'total_failures': total_failures,
            'total_errors': total_errors,
            'overall_success_rate': overall_success_rate,
            'test_suites_passed': sum(1 for suite in self.test_results.values() 
                                    if suite['failures'] == 0 and suite['errors'] == 0)
        }
    
    def create_performance_visualizations(self):
        """Create performance visualization charts"""
        if not self.benchmark_data:
            return
        
        # Create performance charts
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Swarm Rover AI Performance Analysis', fontsize=16)
        
        # Test success rates
        suite_names = list(self.test_results.keys())
        success_rates = [suite['success_rate'] for suite in self.test_results.values()]
        
        ax1.bar(range(len(suite_names)), success_rates, color='skyblue')
        ax1.set_xlabel('Test Suites')
        ax1.set_ylabel('Success Rate (%)')
        ax1.set_title('Test Suite Success Rates')
        ax1.set_xticks(range(len(suite_names)))
        ax1.set_xticklabels([name.replace('Test', '') for name in suite_names], rotation=45)
        ax1.set_ylim(0, 100)
        
        # Performance metrics (if available)
        if hasattr(self, 'performance_metrics') and self.performance_metrics:
            metrics = list(self.performance_metrics.keys())
            values = list(self.performance_metrics.values())
            
            ax2.bar(range(len(metrics)), values, color='lightgreen')
            ax2.set_xlabel('Metrics')
            ax2.set_ylabel('Values')
            ax2.set_title('Performance Metrics')
            ax2.set_xticks(range(len(metrics)))
            ax2.set_xticklabels(metrics, rotation=45)
        
        # Test distribution
        test_counts = [suite['tests_run'] for suite in self.test_results.values()]
        ax3.pie(test_counts, labels=[name.replace('Test', '') for name in suite_names], 
                autopct='%1.1f%%', startangle=90)
        ax3.set_title('Test Distribution by Suite')
        
        # Overall summary
        summary = self.calculate_summary_metrics()
        if summary:
            labels = ['Passed', 'Failed', 'Errors']
            sizes = [
                summary['total_tests'] - summary['total_failures'] - summary['total_errors'],
                summary['total_failures'],
                summary['total_errors']
            ]
            colors = ['green', 'red', 'orange']
            
            ax4.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            ax4.set_title('Overall Test Results')
        
        plt.tight_layout()
        plt.savefig('performance_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print("Performance visualization saved as 'performance_analysis.png'")

def main():
    """Main testing function"""
    print("Starting Swarm Rover AI Comprehensive Testing...")
    print("=" * 60)
    
    # Create performance analyzer
    analyzer = PerformanceAnalyzer()
    
    # Run all tests
    results = analyzer.run_comprehensive_tests()
    
    # Generate report
    report = analyzer.generate_performance_report()
    
    # Create visualizations
    analyzer.create_performance_visualizations()
    
    # Print summary
    print("\n" + "=" * 60)
    print("TESTING SUMMARY")
    print("=" * 60)
    
    summary = analyzer.calculate_summary_metrics()
    print(f"Total Tests: {summary['total_tests']}")
    print(f"Passed: {summary['total_tests'] - summary['total_failures'] - summary['total_errors']}")
    print(f"Failed: {summary['total_failures']}")
    print(f"Errors: {summary['total_errors']}")
    print(f"Overall Success Rate: {summary['overall_success_rate']:.1f}%")
    print(f"Test Suites Passed: {summary['test_suites_passed']}/{len(results)}")
    
    if summary['overall_success_rate'] >= 90:
        print("\n🎉 EXCELLENT: System ready for deployment!")
    elif summary['overall_success_rate'] >= 75:
        print("\n✅ GOOD: System functional with minor issues")
    else:
        print("\n⚠️ NEEDS WORK: System requires fixes before deployment")

if __name__ == "__main__":
    main()
```

---

## 📚 Complete API Documentation

### **ROS2 Topics**

| Topic Name | Message Type | Description |
|------------|--------------|-------------|
| `/swarm_communication` | `SwarmAgentPacket` | Main inter-agent communication |
| `/task_announcements` | `TaskAnnouncement` | Task sharing and assignment |
| `/alpha_election` | `AlphaElection` | Leadership election process |
| `/formation_control` | `FormationControl` | Formation commands and updates |

### **ROS2 Services**

| Service Name | Service Type | Description |
|--------------|--------------|-------------|
| `/assign_mission` | `AssignMission` | Assign mission to swarm |
| `/get_swarm_status` | `GetSwarmStatus` | Get current swarm status |
| `/emergency_stop` | `EmergencyStop` | Emergency stop all agents |

### **Python API Classes**

#### **SimulationAgent**
```python
class SimulationAgent:
    def __init__(self, agent_id: int, x: float, y: float)
    def update(self, dt: float, obstacles: List, targets: List, other_agents: List)
    def set_target(self, x: float, y: float)
    def set_state(self, state: AgentState)
    def set_role(self, role: AgentRole)
    def draw(self, screen)
```

#### **SwarmSimulation**
```python
class SwarmSimulation:
    def __init__(self, width: int, height: int, num_agents: int)
    def add_obstacles(self, obstacle_list: List[Tuple])
    def add_targets(self, target_list: List[Tuple])
    def load_scenario(self, scenario_file: str) -> bool
    def update()
    def render()
    def run()
```

#### **AlphaElection**
```python
class AlphaElection:
    def start_election(self, agents: List) -> bool
    def process_votes(self, agents: List) -> bool
    def elect_alpha(self, agents: List) -> Optional[Agent]
    def calculate_leadership_score(self, agent) -> float
```

#### **FormationControl**
```python
class FormationControl:
    def set_formation(self, formation_type: str, agents: List, spacing: float)
    def update_formation(self, agents: List)
    def get_formation_error(self, agents: List) -> float
    def calculate_formation_positions(self, agents: List) -> Dict
```

---

## 🐳 Deployment Instructions

### **Docker Deployment**

#### **Build and Run**
```bash
# Build the container
docker build -t swarm-rover-ai .

# Run simulation
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  swarm-rover-ai

# Run with docker-compose
docker-compose up --build
```

#### **Kubernetes Deployment**
```bash
# Deploy to Kubernetes
kubectl apply -f deployment/kubernetes.yaml

# Check status
kubectl get pods -l app=swarm-rover-ai

# View logs
kubectl logs -l app=swarm-rover-ai
```

### **Native Installation**

#### **Ubuntu/Debian**
```bash
# Install ROS2 Humble
sudo apt update
sudo apt install ros-humble-desktop

# Install Python dependencies
pip3 install -r requirements.txt

# Build ROS2 package
source /opt/ros/humble/setup.bash
colcon build

# Run simulation
source install/setup.bash
ros2 launch swarm_agents basic_swarm.launch.py
```

#### **macOS**
```bash
# Install ROS2 via Homebrew
brew install ros/humble/ros-humble-desktop

# Install Python dependencies
pip3 install -r requirements.txt

# Build and run
source /opt/homebrew/opt/ros-humble/setup.bash
colcon build
source install/setup.bash
ros2 launch swarm_agents basic_swarm.launch.py
```

---

## 📊 Performance Benchmarks

### **Expected Performance Metrics**

| Metric | Target | Excellent | Good | Needs Improvement |
|--------|--------|-----------|------|-------------------|
| Mission Success Rate | >95% | >98% | 90-95% | <90% |
| Formation Accuracy | >90% | >95% | 85-90% | <85% |
| Communication Efficiency | >95% | >98% | 90-95% | <90% |
| Real-time Performance | 50+ FPS | 60+ FPS | 30-50 FPS | <30 FPS |
| Test Coverage | >95% | >98% | 90-95% | <90% |

### **Scalability Targets**

| Agent Count | Expected FPS | Memory Usage | CPU Usage |
|-------------|--------------|--------------|-----------|
| 6-10 agents | 60 FPS | <500 MB | <50% |
| 10-20 agents | 45 FPS | <800 MB | <70% |
| 20-50 agents | 30 FPS | <1.5 GB | <90% |

---

## 🎯 Implementation Checklist

### **Phase 1: Foundation ✅**
- [ ] Create project structure
- [ ] Initialize Git repository
- [ ] Create README and documentation
- [ ] Set up requirements.txt
- [ ] Create license file

### **Phase 2: ROS2 Infrastructure ✅**
- [ ] Create ROS2 package structure
- [ ] Define custom message types
- [ ] Implement base agent node
- [ ] Create alpha agent implementation
- [ ] Set up launch files

### **Phase 3: AI Integration ✅**
- [ ] Create model download scripts
- [ ] Implement model optimization
- [ ] Create perception bridge
- [ ] Integrate YOLOv8n for object detection
- [ ] Integrate TinyLLaVA for vision-language
- [ ] Integrate Phi-2 for decision making

### **Phase 4: Coordination Algorithms ✅**
- [ ] Implement Alpha Agent Election
- [ ] Create Decentralized Task Sharing
- [ ] Develop Formation Control
- [ ] Implement Consensus Decision Making
- [ ] Create Behavior State Machines

### **Phase 5: Simulation Environment ✅**
- [ ] Create 2D physics engine
- [ ] Implement real-time visualization
- [ ] Create obstacle and target management
- [ ] Implement scenario loading system
- [ ] Add performance monitoring

### **Phase 6: Testing Framework ✅**
- [ ] Create automated test suite
- [ ] Implement performance benchmarking
- [ ] Create stress testing capabilities
- [ ] Generate comprehensive reports
- [ ] Add visualization tools

### **Phase 7: Deployment ✅**
- [ ] Create Dockerfile
- [ ] Implement docker-compose setup
- [ ] Create Kubernetes configuration
- [ ] Set up deployment scripts
- [ ] Add monitoring and logging

### **Phase 8: Documentation ✅**
- [ ] Complete API documentation
- [ ] Write user guide
- [ ] Create developer documentation
- [ ] Update README with examples
- [ ] Create visual diagrams

### **Phase 9: Validation ✅**
- [ ] Run comprehensive test suite
- [ ] Validate mission scenarios
- [ ] Performance benchmarking
- [ ] Create test reports
- [ ] Final system validation

---

## 🚀 Quick Start Commands

### **For AI Agent Implementation**

```bash
# 1. Create project structure
mkdir -p swarm_rover_ai/{swarm_agents,simulation,models,testing,deployment,docs}

# 2. Initialize Git
cd swarm_rover_ai
git init
echo "*.pyc\n__pycache__/\n.vscode/\n*.log" > .gitignore

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install dependencies
pip install pygame numpy matplotlib seaborn rclpy

# 5. Create and run basic simulation
python3 standalone_demo.py

# 6. Build ROS2 package
source /opt/ros/humble/setup.bash
colcon build

# 7. Run full system
source install/setup.bash
ros2 launch swarm_agents basic_swarm.launch.py

# 8. Run tests
python3 -m pytest testing/

# 9. Deploy with Docker
docker-compose up --build
```

---

## 📝 Final Notes for AI Agent

### **Critical Implementation Points**

1. **File Structure**: Follow the exact directory structure specified
2. **Dependencies**: Install all required packages from requirements.txt
3. **ROS2 Integration**: Ensure proper ROS2 message definitions and node implementations
4. **Testing**: Implement comprehensive test suite with >95% coverage
5. **Documentation**: Create complete API documentation and user guides
6. **Performance**: Target 50+ FPS for real-time simulation
7. **Scalability**: Support 6-50 agents with graceful performance degradation

### **Success Validation**

The implementation is successful when:
- All tests pass (>95% success rate)
- Real-time simulation runs smoothly
- Formation control achieves >90% accuracy
- Search & rescue missions have >95% success rate
- Complete documentation is generated
- Docker deployment works correctly

### **Extension Opportunities**

After basic implementation:
- Add 3D visualization
- Implement hardware integration
- Add machine learning training capabilities
- Create web-based control interface
- Add multi-swarm coordination
- Implement advanced AI models

---

**This blueprint contains everything needed to recreate the complete Swarm Rover AI project. Follow the phases sequentially, implement all specified components, and validate with the testing framework to ensure a fully functional system.**

