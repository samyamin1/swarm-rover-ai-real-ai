#!/usr/bin/env python3
"""
Scenario Generator for Swarm Rover AI Simulation
Generates dynamic mission scenarios for testing and simulation
"""

import json
import random

class ScenarioGenerator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def generate_random_scenario(self, num_obstacles: int = 5, num_targets: int = 3, num_agents: int = 8) -> dict:
        """Generates a random mission scenario."""
        scenario = {
            "name": f"Random Scenario {random.randint(1000, 9999)}",
            "description": "A randomly generated search and rescue mission.",
            "obstacles": self._generate_random_obstacles(num_obstacles),
            "targets": self._generate_random_targets(num_targets),
            "agents": self._generate_random_agent_configs(num_agents)
        }
        return scenario

    def _generate_random_obstacles(self, count: int) -> list:
        obstacles = []
        for _ in range(count):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            w = random.randint(30, 150)
            h = random.randint(30, 150)
            obstacles.append([x, y, w, h])
        return obstacles

    def _generate_random_targets(self, count: int) -> list:
        targets = []
        for _ in range(count):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            targets.append([x, y])
        return targets

    def _generate_random_agent_configs(self, count: int) -> list:
        agent_configs = []
        for i in range(count):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            role = "follower"
            if i == 0: # Assign first agent as potential alpha
                role = "alpha"
            agent_configs.append({"id": i + 1, "x": x, "y": y, "role": role})
        return agent_configs

    def save_scenario_to_file(self, scenario: dict, filename: str):
        """Saves a scenario to a JSON file."""
        filepath = f"./simulation/scenarios/{filename}"
        with open(filepath, 'w') as f:
            json.dump(scenario, f, indent=4)
        print(f"Scenario saved to {filepath}")

    def load_scenario_from_file(self, filename: str) -> dict:
        """Loads a scenario from a JSON file."""
        filepath = f"./simulation/scenarios/{filename}"
        with open(filepath, 'r') as f:
            scenario = json.load(f)
        print(f"Scenario loaded from {filepath}")
        return scenario

if __name__ == "__main__":
    generator = ScenarioGenerator(width=1200, height=800)

    # Generate and save a basic search and rescue scenario
    basic_sr_scenario = generator.generate_random_scenario(num_obstacles=3, num_targets=5, num_agents=6)
    generator.save_scenario_to_file(basic_sr_scenario, "basic_search_rescue.json")

    # Generate and save a complex formation mission scenario
    complex_fm_scenario = generator.generate_random_scenario(num_obstacles=0, num_targets=0, num_agents=10)
    complex_fm_scenario["name"] = "Complex Formation Mission"
    complex_fm_scenario["description"] = "A mission focused on maintaining complex formations."
    generator.save_scenario_to_file(complex_fm_scenario, "complex_formation_mission.json")

    print("Sample scenarios generated.")
