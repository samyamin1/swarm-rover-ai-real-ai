# Swarm Rover AI

This project implements a modular swarm robotics simulation platform featuring autonomous agents with AI-driven decision making, advanced coordination algorithms, and a real-time 2D simulation environment.

## Features

*   **Autonomous Agents:** 6-10 independent agents with AI-driven decision making.
*   **Advanced Coordination:** Alpha agent election, task sharing, and formation control.
*   **AI Integration:** YOLOv8n for object detection, TinyLLaVA for vision-language understanding, and Phi-2 for decision making.
*   **Real-time Simulation:** 2D physics-based environment with visualization.
*   **Mission Scenarios:** Search & rescue, formation flying, and obstacle navigation.

## Getting Started

### Prerequisites

*   Docker
*   Python 3.8+

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/swarm_rover_ai.git
    ```
2.  Build the Docker container:
    ```bash
    docker-compose build
    ```
3.  Run the simulation:
    ```bash
    docker-compose up
    ```

## Usage

To run the simulation, execute the following command:

```bash
docker-compose up
```

This will start the simulation with the default scenario. To run a different scenario, you can modify the `docker-compose.yml` file.

## Documentation

*   [Architecture Design](docs/architecture_design.md)
*   [API Documentation](docs/API_DOCUMENTATION.md)
*   [User Guide](docs/USER_GUIDE.md)
*   [Developer Guide](docs/DEVELOPER_GUIDE.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
