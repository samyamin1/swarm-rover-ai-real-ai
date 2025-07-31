# System Architecture Design

## High-Level Architecture

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

### Component Relationships

-   **Agents** communicate via **Swarm Agent Packets**
-   **AI Models** provide perception and decision-making capabilities
-   **Simulation Engine** provides physics and visualization
-   **Testing Framework** validates all components
-   **Deployment System** packages everything for production

## Detailed Component Descriptions

### 1. Agent Layer

*   **Alpha Agent:** The designated leader of the swarm, responsible for high-level coordination, task assignment, and formation control. Elected dynamically based on various criteria (e.g., battery level, capabilities, centrality).
*   **Follower Agents:** Execute tasks assigned by the Alpha Agent or self-organize for local objectives. They continuously report their status and sensor data to the swarm.
*   **Agent State Machines:** Each agent operates based on a finite state machine that dictates its behavior (e.g., `IDLE`, `SEARCHING`, `MOVING_TO_TARGET`, `FORMING_UP`, `RESCUING`). Transitions between states are triggered by internal logic or external commands/perceptions.

### 2. AI Intelligence Layer

*   **YOLOv8n (Object Detection):** A lightweight, real-time object detection model used by agents to identify objects of interest (e.g., targets, obstacles, other agents) within their visual range. Provides bounding box coordinates and class labels.
*   **TinyLLaVA (Vision-Language Understanding):** A compact Vision-Language Model that processes visual input (from YOLOv8n detections and raw images) and generates natural language descriptions or answers questions about the scene. This enables agents to understand complex visual contexts.
*   **Phi-2 (Decision Making & Communication):** A small but powerful Language Model used for higher-level reasoning, decision-making, and generating natural language communication. Agents use Phi-2 to interpret VLM outputs, formulate strategies, and compose messages for inter-agent communication.

### 3. Communication Layer

*   **Swarm Agent Packet Protocol:** A custom, lightweight message format for efficient, low-latency communication between agents. Designed for broadcasting status updates, sharing discovered information, and transmitting commands.
*   **ROS2 Message System:** Utilizes ROS2 (Robot Operating System 2) as the underlying middleware for inter-process communication within and between agents. Provides robust, decentralized message passing capabilities.
*   **Decentralized Network Topology:** Agents communicate directly with nearby agents, forming a dynamic, self-healing network. This ensures resilience and scalability, as there is no single point of failure.

### 4. Simulation Layer

*   **2D Physics Engine:** A custom 2D physics engine (e.g., using Pygame) that simulates agent movement, collisions with obstacles, and environmental interactions in real-time.
*   **Real-time Visualization:** A graphical interface that displays the agents, obstacles, targets, and their interactions in the 2D environment. Provides visual feedback on swarm behavior and mission progress.
*   **Mission Scenario Engine:** Allows for the definition and loading of various mission scenarios (e.g., search and rescue, formation flying) with predefined obstacles, targets, and agent starting positions. Supports dynamic scenario generation.

### 5. Testing & Validation Layer

*   **Automated Test Suite:** A comprehensive suite of unit, integration, and system tests to ensure the correctness and robustness of all components. Includes tests for communication, AI integration, coordination algorithms, and simulation physics.
*   **Performance Benchmarking:** Tools and scripts to measure key performance indicators (KPIs) such as mission success rate, formation accuracy, communication efficiency, and computational overhead. Helps in optimizing the system.
*   **Mission Validation Framework:** A framework to validate the swarm's ability to successfully complete various mission scenarios, providing quantitative metrics on success rates and efficiency.

## Data Flow

1.  **Sensor Data:** Simulation environment provides raw sensor data (e.g., image frames, proximity readings) to individual agents.
2.  **Perception (YOLOv8n):** Agents process raw sensor data using YOLOv8n for object detection, identifying objects and their locations.
3.  **Understanding (TinyLLaVA):** Detected objects and visual context are fed to TinyLLaVA, which generates natural language descriptions or answers queries about the scene.
4.  **Reasoning & Decision (Phi-2):** The natural language output from TinyLLaVA is processed by Phi-2, enabling agents to reason about the situation, formulate plans, and make decisions.
5.  **Communication (Swarm Agent Packet Protocol):** Agents broadcast their status, discovered information, and decisions to other agents using the custom packet protocol over ROS2.
6.  **Coordination Algorithms:** The Alpha Agent (or decentralized algorithms) processes incoming communication packets to update swarm state, assign tasks, and issue formation commands.
7.  **Action Execution:** Agents execute their decisions by controlling their movement (velocity, direction) within the simulation environment.
8.  **Feedback Loop:** The simulation environment provides updated sensor data, completing the feedback loop for continuous adaptation and decision-making.
