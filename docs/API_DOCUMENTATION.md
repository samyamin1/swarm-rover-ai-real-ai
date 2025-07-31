# API Documentation

This document provides a comprehensive API reference for the Swarm Rover AI project, detailing the ROS2 message types, agent interfaces, and key functions within the simulation and coordination modules.

## ROS2 Message Definitions

### `SwarmAgentPacket.msg`

Used for general communication and status updates between swarm agents.

```
# Swarm Agent Communication Packet
std_msgs/Header header
uint32 agent_id
string agent_role          # "alpha", "follower", "scout"
string agent_state         # "idle", "searching", "moving_to_target", etc.
geometry_msgs/Point position
geometry_msgs/Vector3 velocity
float32 battery_level
string[] capabilities      # List of agent capabilities (e.g., "search", "rescue")
string mission_status      # Current mission status (e.g., "ready", "executing", "completed")
string[] discovered_targets # List of discovered target IDs or coordinates (JSON string)
string communication_data  # JSON-encoded additional data (e.g., LLM output, VLM insights)
```

### `TaskAnnouncement.msg`

Used by agents (typically the Alpha) to announce new tasks to the swarm.

```
std_msgs/Header header
uint32 announcing_agent_id
string task_type           # "search", "rescue", "patrol", "formation"
string task_priority       # "low", "medium", "high", "critical"
geometry_msgs/Point task_location
float32 estimated_duration
string[] required_capabilities
uint32 max_agents_needed
string task_description
```

### `AlphaElection.msg`

Used for the democratic alpha agent election process.

```
std_msgs/Header header
string election_phase      # "nomination", "voting", "result"
uint32 candidate_agent_id
uint32 voting_agent_id
float32 candidate_score    # Leadership capability score
string vote_reason         # Reason for vote (e.g., "highest battery", "central position")
bool election_complete
uint32 elected_alpha_id
```

### `FormationControl.msg`

Used by the Alpha Agent to command and maintain swarm formations.

```
std_msgs/Header header
uint32 alpha_agent_id
string formation_type      # "line", "circle", "diamond", "v_formation", "custom"
geometry_msgs/Point[] target_positions # Target positions for each agent in the formation
float32 formation_spacing
float32 movement_speed
bool maintain_formation
string formation_objective
```

## Agent Interfaces

### `BaseAgent` (in `swarm_agents/swarm_agents/agent_node.py`)

Base class for all swarm agents, providing core ROS2 integration and common functionalities.

**Methods:**

*   `__init__(self, agent_id, initial_position=(0.0, 0.0))`: Initializes the base agent with a unique ID and starting position.
*   `send_heartbeat(self)`: Publishes a `SwarmAgentPacket` with the agent's current status.
*   `packet_callback(self, msg)`: Callback for incoming `SwarmAgentPacket` messages, updates `known_agents`.
*   `task_callback(self, msg)`: Callback for incoming `TaskAnnouncement` messages, triggers task consideration.
*   `update_agent(self)`: Main agent update loop, handles movement, battery drain, and state-specific behaviors.
*   `can_handle_task(self, task_msg)`: Checks if the agent has the required capabilities for a given task.
*   `consider_task(self, task_msg)`: Logic for an agent to decide whether to accept a task.
*   `process_agent_message(self, msg)`: Abstract method for processing messages from other agents.
*   `set_target_position(self, x, y)`: Sets a new target position for the agent to move towards.
*   `calculate_distance_to(self, position)`: Calculates the Euclidean distance to a given point.

### `AlphaAgent` (in `swarm_agents/swarm_agents/alpha_agent.py`)

Extends `BaseAgent` with leadership and coordination capabilities.

**Methods:**

*   `__init__(self, agent_id, initial_position=(0.0, 0.0))`: Initializes the Alpha Agent.
*   `coordinate_swarm(self)`: Main coordination function, updates followers, checks mission progress, and issues formation commands.
*   `update_followers(self)`: Manages the list of known follower agents, removing stale entries.
*   `assign_tasks(self)`: Assigns tasks to available follower agents based on mission objectives.
*   `assign_search_rescue_task(self, agent_ids)`: Example method to assign a specific search and rescue task.
*   `set_formation(self, formation_type, spacing=50.0)`: Commands the swarm to adopt a specific formation.
*   `calculate_formation_positions(self, formation_type, spacing)`: Calculates target positions for agents within a given formation.
*   `maintain_formation(self)`: Periodically updates formation commands to ensure agents stay in formation.
*   `election_callback(self, msg)`: Handles incoming `AlphaElection` messages.
*   `formation_callback(self, msg)`: Handles incoming `FormationControl` messages.
*   `respond_to_election(self, election_msg)`: Responds to an alpha election nomination.
*   `calculate_leadership_score(self)`: Calculates the agent's score for alpha election based on various factors.
*   `check_mission_progress(self)`: Monitors and updates the overall mission progress.

### `PerceptionBridge` (in `swarm_agents/swarm_agents/perception_bridge.py`)

Manages the integration of AI models for perception and decision-making.

**Methods:**

*   `__init__(self)`: Initializes the bridge and AI model placeholders.
*   `image_callback(self, msg)`: Processes incoming `sensor_msgs/Image` messages, triggering AI model inference.
*   `run_object_detection(self, image)`: Placeholder for YOLOv8n inference.
*   `publish_object_detections(self, detections)`: Publishes detected objects as a `std_msgs/String` (JSON).
*   `run_vision_language_model(self, image, detections)`: Placeholder for TinyLLaVA inference.
*   `publish_vision_language_output(self, vlm_output)`: Publishes VLM output as a `std_msgs/String`.
*   `run_decision_making_model(self, vlm_output)`: Placeholder for Phi-2 inference.
*   `publish_decision_output(self, decision)`: Publishes decision output as a `std_msgs/String`.

## Coordination Algorithms (in `swarm_agents/swarm_agents/coordination_algorithms.py`)

This module contains classes implementing various swarm coordination algorithms.

### `AlphaElection`

Handles the democratic election of an alpha agent.

**Methods:**

*   `start_election(self, agents)`: Initiates an election.
*   `calculate_leadership_score(self, agent)`: Computes a score for an agent's leadership capability.
*   `process_votes(self, agents)`: Collects and processes votes from agents.
*   `elect_alpha(self, agents)`: Determines and sets the elected alpha agent.
*   `is_election_timeout(self)`: Checks if the election has timed out.

### `TaskSharing`

Manages decentralized task announcement, bidding, and assignment.

**Methods:**

*   `announce_task(self, task_type, location, priority="medium", required_agents=1)`: Announces a new task.
*   `bid_for_task(self, agent, task_id)`: Allows an agent to bid on a task.
*   `calculate_bid_score(self, agent, task)`: Calculates an agent's suitability score for a task.
*   `assign_tasks(self)`: Assigns tasks to agents based on bids.
*   `complete_task(self, task_id, success=True)`: Marks a task as completed.

### `FormationControl`

Provides algorithms for maintaining swarm formations.

**Methods:**

*   `set_formation(self, formation_type, agents, spacing=50.0, center=None)`: Defines and sets a new formation.
*   `calculate_formation_positions(self, agents)`: Calculates target positions for agents in the current formation.
*   `update_formation(self, agents)`: Adjusts agent velocities to maintain the formation.
*   `get_formation_error(self, agents)`: Calculates the average deviation from target formation positions.

### `ConsensusDecisionMaking`

Facilitates consensus-based decision making within the swarm.

**Methods:**

*   `propose_decision(self, proposer_id, decision_type, options, description="")`: Proposes a new decision.
*   `vote_on_proposal(self, proposal_id, voter_id, choice, reasoning="")`: Records an agent's vote on a proposal.
*   `check_consensus(self, proposal_id, total_agents)`: Determines if consensus has been reached for a proposal.
*   `get_active_proposals(self)`: Returns a list of currently active proposals.

## Simulation Environment (in `simulation/src/simulation_environment.py`)

### `SwarmSimulation`

Main class for the 2D physics-based simulation environment.

**Methods:**

*   `__init__(self, width=1200, height=800, num_agents=8)`: Initializes the simulation, Pygame, and core components.
*   `create_agents(self)`: Populates the simulation with initial agents.
*   `setup_display(self)`: Configures the Pygame display window.
*   `add_obstacles(self, obstacle_list)`: Adds rectangular obstacles to the simulation.
*   `add_targets(self, target_list)`: Adds target points for agents to discover.
*   `load_scenario(self, scenario_file)`: Loads simulation configurations from a JSON scenario file.
*   `update(self)`: Advances the simulation by one time step, updating agents, coordination, and metrics.
*   `update_coordination(self)`: Triggers updates for alpha election, task sharing, and formation control.
*   `check_target_discoveries(self)`: Detects if agents have discovered targets.
*   `update_metrics(self)`: Recalculates and updates performance metrics.
*   `handle_events(self)`: Processes Pygame user input events (keyboard, mouse).
*   `handle_keypress(self, key)`: Handles specific keyboard inputs (e.g., reset, election, formation change).
*   `handle_mouse_click(self, pos, button)`: Handles mouse clicks for adding targets/obstacles.
*   `render(self)`: Draws all simulation elements on the screen.
*   `draw_ui(self)`: Renders the user interface elements (info, metrics, controls).
*   `reset_simulation(self)`: Resets the simulation to its initial state.
*   `run(self)`: Starts the main simulation loop.
*   `cleanup(self)`: Cleans up Pygame resources.

### `SimulationAgent`

Represents an individual agent within the simulation environment.

**Methods:**

*   `__init__(self, agent_id: int, x: float, y: float)`: Initializes a simulation agent.
*   `update(self, dt: float, obstacles: List, targets: List, other_agents: List)`: Updates the agent's state, sensors, and physics.
*   `update_sensors(self, obstacles, targets, other_agents)`: Detects nearby obstacles, targets, and other agents.
*   `idle_behavior(self)`: Defines behavior when the agent is idle.
*   `search_behavior(self)`: Defines behavior when the agent is searching.
*   `move_to_target_behavior(self)`: Defines behavior when the agent is moving to a target.
*   `formation_behavior(self)`: Defines behavior when the agent is maintaining formation.
*   `avoid_obstacles(self)`: Implements obstacle avoidance logic.
*   `update_physics(self, dt: float)`: Applies physics updates (movement, friction, speed limits).
*   `update_appearance(self)`: Adjusts the agent's visual representation based on its role and state.
*   `distance_to_rect(self, rect)`: Calculates distance to a rectangular obstacle.
*   `closest_point_on_rect(self, rect)`: Finds the closest point on a rectangle to the agent.
*   `draw(self, screen)`: Renders the agent on the Pygame screen.

## Scenario Generator (in `simulation/src/scenario_generator.py`)

### `ScenarioGenerator`

Utility for creating and managing simulation scenarios.

**Methods:**

*   `__init__(self, width: int, height: int)`: Initializes the generator with simulation dimensions.
*   `generate_random_scenario(self, num_obstacles: int = 5, num_targets: int = 3, num_agents: int = 8)`: Creates a new random scenario.
*   `_generate_random_obstacles(self, count: int)`: Generates random obstacle configurations.
*   `_generate_random_targets(self, count: int)`: Generates random target locations.
*   `_generate_random_agent_configs(self, count: int)`: Generates random initial agent configurations.
*   `save_scenario_to_file(self, scenario: dict, filename: str)`: Saves a scenario to a JSON file.
*   `load_scenario_from_file(self, filename: str)`: Loads a scenario from a JSON file.

## Testing Framework (in `testing/src/testing_framework.py`)

### `TestSwarmSimulation`

Unit tests for the `SwarmSimulation` and agent behaviors.

**Methods:**

*   `setUp(self)`: Initializes a `SwarmSimulation` instance before each test.
*   `test_agent_initialization(self)`: Verifies correct agent creation.
*   `test_alpha_election(self)`: Tests the alpha election process.
*   `test_task_announcement_and_bidding(self)`: Tests task sharing and assignment.
*   `test_formation_control(self)`: Tests the swarm's ability to maintain formations.
*   `test_target_discovery(self)`: Tests agent target detection capabilities.
*   `test_scenario_loading(self)`: Tests loading scenarios from JSON files.

### `TestPerformanceAnalyzer`

Unit tests for the `PerformanceAnalyzer`.

**Methods:**

*   `test_performance_metrics_calculation(self)`: Placeholder for testing performance metric calculations.

## Performance Analyzer (in `testing/src/performance_analyzer.py`)

### `PerformanceAnalyzer`

Analyzes and reports on simulation performance metrics.

**Methods:**

*   `__init__(self, report_dir="./testing/reports/")`: Initializes the analyzer and report directory.
*   `record_metrics(self, metrics: dict)`: Records a snapshot of current simulation metrics.
*   `generate_report(self, scenario_name: str = "default_scenario")`: Generates a JSON report and plots of performance metrics.
*   `_plot_metrics(self, scenario_name: str)`: Internal method to generate and save plots of metrics.
