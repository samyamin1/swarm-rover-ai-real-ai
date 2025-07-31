# Developer Guide

This guide is intended for developers who wish to understand, modify, or extend the Swarm Rover AI project. It covers the project structure, development workflow, and key areas for contribution.

## 1. Project Structure

The project follows a modular structure to facilitate development and maintenance. Here's a breakdown of the main directories:

```
swarm_rover_ai/
├── 📄 README.md
├── 📄 LICENSE
├── 📄 requirements.txt
├── 📄 Dockerfile
├── 📄 docker-compose.yml
├── 📄 .dockerignore
├── 📄 .gitignore
├── 🤖 swarm_agents/                       # ROS2 Agent Package
│   ├── 📄 package.xml
│   ├── 📄 setup.py
│   ├── 📄 CMakeLists.txt
│   ├── 📁 resource/
│   ├── 📁 msg/                            # Custom ROS2 messages
│   │   ├── SwarmAgentPacket.msg
│   │   ├── TaskAnnouncement.msg
│   │   ├── AlphaElection.msg
│   │   └── FormationControl.msg
│   ├── 📁 swarm_agents/                   # Python modules
│   │   ├── __init__.py
│   │   ├── agent_node.py                  # Base agent implementation
│   │   ├── alpha_agent.py                 # Alpha agent logic
│   │   ├── perception_bridge.py           # AI model integration
│   │   ├── coordination_algorithms.py     # Swarm coordination
│   │   └── behavior_state_machine.py      # Agent behaviors
│   └── 📁 launch/                         # ROS2 launch files
│       └── basic_swarm.launch.py
│
├── 🎮 simulation/                         # Simulation Environment
│   ├── 📁 src/                            # Core simulation code
│   │   ├── simulation_environment.py      # Main simulation engine
│   │   └── scenario_generator.py          # Dynamic scenario creation
│   └── 📁 scenarios/                      # Predefined missions
│
├── 🧠 models/                             # AI Models
│   ├── download_models.py                 # Model download script
│   └── optimize_models.py                 # Model optimization
│
├── 🧪 testing/                            # Testing Framework
│   ├── 📁 src/                            # Test implementations
│   │   ├── testing_framework.py           # Main test framework
│   │   └── performance_analyzer.py        # Performance metrics
│   ├── 📁 benchmarks/
│   └── 📁 reports/
│
├── 🐳 deployment/                         # Deployment Configuration
│   ├── deploy.sh
│   └── kubernetes.yaml
│
├── 📚 docs/                               # Documentation
│   ├── architecture_design.md
│   ├── API_DOCUMENTATION.md
│   ├── USER_GUIDE.md
│   └── DEVELOPER_GUIDE.md
│
└── 🔧 scripts/                            # Utility Scripts
    └── setup_environment.sh
```

## 2. Development Workflow

### Setting up Your Development Environment

It is recommended to use Docker for development to ensure a consistent environment. After cloning the repository:

1.  **Build the Development Image:**
    ```bash
    docker-compose build
    ```

2.  **Run a Development Container:**
    You can run a shell inside the container to work on the code:
    ```bash
    docker-compose run --rm simulation bash
    ```
    This will give you a bash shell inside the container with all dependencies installed and the project files mounted.

### Code Modifications

*   **Python Code:** Most of the project is written in Python. Adhere to PEP 8 style guidelines.
*   **ROS2 Messages:** If you need to add new communication messages, define them in `.msg` files within `swarm_agents/msg/` and update `package.xml` and `CMakeLists.txt` accordingly.
*   **AI Models:** The `models/` directory contains scripts for downloading and optimizing AI models. If you integrate new models, ensure they are compatible and optimized for deployment.

### Running Tests

Tests are crucial for ensuring code quality and correctness. The testing framework is located in `testing/src/testing_framework.py`.

To run all tests:

```bash
python3 testing/src/testing_framework.py
```

It is recommended to run tests frequently during development.

### Linting and Formatting

Maintain code quality by running linters and formatters. (Specify tools like `flake8`, `black`, `isort` if used in the project).

## 3. Key Areas for Contribution

### Agent Behaviors

*   **`swarm_agents/swarm_agents/behavior_state_machine.py`:** Extend the state machine with more complex behaviors and transitions.
*   **`swarm_agents/swarm_agents/agent_node.py`:** Implement detailed logic for `idle_behavior`, `search_behavior`, `move_to_target_behavior`, etc.

### AI Integration

*   **`swarm_agents/swarm_agents/perception_bridge.py`:** Replace placeholder AI model calls with actual integrations of YOLOv8n, TinyLLaVA, and Phi-2. This will involve using their respective Python APIs.
*   **`models/download_models.py` and `models/optimize_models.py`:** Implement the actual download and optimization logic for the AI models.

### Swarm Coordination

*   **`swarm_agents/swarm_agents/coordination_algorithms.py`:** Enhance existing algorithms or add new ones for:
    *   More sophisticated alpha election criteria.
    *   Dynamic task allocation based on agent capabilities and real-time conditions.
    *   Advanced formation control algorithms (e.g., obstacle avoidance within formation).
    *   Robust consensus mechanisms for distributed decision-making.

### Simulation Environment

*   **`simulation/src/simulation_environment.py`:** Improve physics realism, add new environmental elements (e.g., wind, uneven terrain), or enhance visualization.
*   **`simulation/src/scenario_generator.py`:** Develop more complex and varied scenario generation capabilities.

### Testing and Validation

*   **`testing/src/testing_framework.py`:** Add more comprehensive unit and integration tests for new features.
*   **`testing/src/performance_analyzer.py`:** Develop more advanced performance metrics and visualization tools.

## 4. Adding New Features

When adding a new feature, consider the following:

1.  **Design:** Outline the changes in the `docs/architecture_design.md` if it impacts the overall system.
2.  **Implementation:** Write clean, modular code following existing patterns.
3.  **Testing:** Write unit and integration tests for your new feature.
4.  **Documentation:** Update relevant documentation (API, User Guide, Developer Guide).

## 5. Contributing

(Placeholder for contribution guidelines, e.g., pull request process, code review, issue tracking.)
