# User Guide

Welcome to the Swarm Rover AI Simulation! This guide will help you get started with running and interacting with the simulation.

## 1. Overview

The Swarm Rover AI Simulation provides a 2D environment where autonomous rover agents operate as a swarm. These agents are equipped with AI capabilities for perception, decision-making, and coordination to perform various missions, such as search and rescue.

## 2. Getting Started

### Prerequisites

Before you can run the simulation, ensure you have the following installed on your system:

*   **Docker:** The simulation is containerized using Docker for easy setup and portability. You can download Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop).

### Installation and Setup

1.  **Clone the Repository:**
    First, clone the project repository to your local machine:
    ```bash
    git clone https://github.com/your-username/swarm_rover_ai.git
    cd swarm_rover_ai
    ```

2.  **Build the Docker Images:**
    Navigate to the root directory of the cloned repository (where `docker-compose.yml` is located) and build the Docker images. This might take some time on the first run as it downloads necessary dependencies.
    ```bash
    docker-compose build
    ```

3.  **Run the Simulation:**
    Once the images are built, you can start the simulation using Docker Compose:
    ```bash
    docker-compose up
    ```
    This command will start the simulation in your terminal. A Pygame window will open, displaying the 2D simulation environment.

## 3. Interacting with the Simulation

Once the simulation window is open, you can interact with it using your keyboard and mouse:

### Keyboard Controls

*   **`R` - Reset Simulation:** Resets all agents to their initial positions, clears discovered targets, and resets performance metrics.
*   **`E` - Start Alpha Election:** Initiates a new alpha agent election process within the swarm. Observe how agents vote and a new leader is chosen.
*   **`F` - Cycle Formation Types:** Cycles through different swarm formation types (e.g., line, circle, diamond, V-formation). The alpha agent will attempt to guide the followers into the selected formation.
*   **`SPACE` - Pause/Unpause Simulation:** Toggles the simulation's running state.

### Mouse Controls

*   **Left Click - Add Target:** Click anywhere on the simulation screen to add a new target for the agents to discover. Agents will attempt to find and report these targets.
*   **Right Click - Add Obstacle:** Click and drag to define a rectangular obstacle. Agents will detect and attempt to avoid these obstacles.

## 4. Understanding the Display

The simulation window displays several elements:

*   **Agents (Circles):** Each circle represents a rover agent.
    *   **Blue Agents:** Follower agents.
    *   **Gold Agent (with Crown):** The Alpha agent, responsible for leadership.
    *   **Green Agents:** Scout agents (if implemented and assigned).
    *   **Agent ID:** A number displayed inside each agent for identification.
    *   **Battery Level:** A small bar below each agent indicating its battery status (Green: High, Yellow: Medium, Red: Low).
    *   **Velocity Vector:** A white line extending from the agent indicating its current direction and speed.
    *   **Communication Range:** A faint grey circle around each agent showing its communication radius.
    *   **Sensor Range:** A faint yellow circle around searching agents indicating their sensor detection range.
*   **Obstacles (Brown Rectangles):** Static objects that agents must navigate around.
*   **Targets (Red Circles):** Objects that agents are tasked to find. Once discovered, they turn green and display a checkmark.
*   **UI Panel (Top Left):** Displays real-time simulation information and performance metrics:
    *   **Time:** Elapsed simulation time.
    *   **Agents:** Number of active agents.
    *   **Targets:** Number of remaining and found targets.
    *   **Formation:** Current formation type being attempted by the swarm.
    *   **Performance Metrics:** Mission Success Rate, Formation Accuracy, Communication Efficiency.
    *   **Alpha Agent:** ID of the current alpha agent.
    *   **Controls:** A quick reminder of the keyboard and mouse controls.

## 5. Scenarios

The simulation can load predefined scenarios. You can find example scenario files in the `simulation/scenarios/` directory:

*   `basic_search_rescue.json`
*   `complex_formation_mission.json`

You can modify these files or create your own to design custom missions. To load a specific scenario, you would typically modify the `main` function in `simulation/src/simulation_environment.py` or pass it as an argument if the entrypoint is configured to accept it.

## 6. Troubleshooting

*   **Simulation Window Not Appearing:** Ensure Docker is running and the `docker-compose up` command completed without errors. Check your terminal for any Python or Pygame-related error messages.
*   **Performance Issues:** If the simulation runs slowly, your system might be under heavy load, or the number of agents/complexity of the scenario might be too high for your hardware. Try reducing the `num_agents` in `simulation/src/simulation_environment.py`.
*   **Docker Errors:** If you encounter Docker-related errors, try rebuilding the images (`docker-compose build --no-cache`) or restarting your Docker daemon.

## 7. Shutting Down the Simulation

To stop the simulation and the Docker containers, press `Ctrl+C` in the terminal where `docker-compose up` is running. Then, to stop and remove the containers:

```bash
docker-compose down
```

This will clean up the running containers and networks created by Docker Compose.
