#!/usr/bin/env python3
"""
Comprehensive Testing Framework for Swarm Rover AI
Automated testing, validation, and performance analysis
"""

import unittest
import time
import json
import os
import sys

# Add parent directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from simulation.src.simulation_environment import SwarmSimulation, SimulationAgent
from swarm_agents.swarm_agents.coordination_algorithms import AgentState
from swarm_agents.swarm_agents.coordination_algorithms import AlphaElection, TaskSharing, FormationControl

# Mock PerceptionBridge for testing
from typing import Tuple

class MockPerceptionBridge:
    def __init__(self):
        pass

    def process_perception_input(self, textual_scene_description: str) -> Tuple[str, str]:
        # Simple mock logic: always return a search command
        if "target" in textual_scene_description.lower():
            return "Mock VLM: Target detected.", "MOVE_TO_TARGET 100,100" # Dummy target
        return "Mock VLM: No specific objects.", "SEARCH_AREA"

class TestSwarmSimulation(unittest.TestCase):

    def setUp(self):
        # Pass the mock perception bridge to SwarmSimulation
        self.mock_pb = MockPerceptionBridge()
        self.sim = SwarmSimulation(width=800, height=600, num_agents=5, perception_bridge=self.mock_pb)

    def test_agent_initialization(self):
        self.assertEqual(len(self.sim.agents), 5)
        for agent in self.sim.agents:
            self.assertIsInstance(agent, SimulationAgent)
            self.assertGreaterEqual(agent.battery_level, 0)

    def test_alpha_election(self):
        # Manually trigger election for testing purposes
        self.sim.alpha_election.start_election(self.sim.agents)
        # Simulate some time for votes to be processed
        for _ in range(10):
            self.sim.update_coordination()
            time.sleep(0.1)
        
        alpha_agents = [a for a in self.sim.agents if a.role.value == "alpha"]
        self.assertEqual(len(alpha_agents), 1, "There should be exactly one alpha agent after election")
        print(f"Alpha agent elected: {alpha_agents[0].agent_id}")

    def test_task_announcement_and_bidding(self):
        task_id = self.sim.task_sharing.announce_task("search", (100, 100), required_agents=2)
        self.assertIsNotNone(task_id)
        
        # Simulate agents bidding for the task
        for agent in self.sim.agents:
            self.sim.task_sharing.bid_for_task(agent, task_id)
        
        self.sim.task_sharing.assign_tasks()
        
        assigned_task = self.sim.task_sharing.assigned_tasks.get(task_id)
        self.assertIsNotNone(assigned_task)
        self.assertEqual(assigned_task["status"], "assigned")
        self.assertEqual(len(assigned_task["assigned_agents"]), 2)
        print(f"Task {task_id} assigned to: {assigned_task['assigned_agents']}")

    def test_formation_control(self):
        # Elect an alpha first
        self.sim.alpha_election.start_election(self.sim.agents)
        for _ in range(10):
            self.sim.update_coordination()
            time.sleep(0.1)
        
        alpha_agent = next((a for a in self.sim.agents if a.role.value == "alpha"), None)
        self.assertIsNotNone(alpha_agent)

        # Set a formation
        self.sim.formation_control.set_formation("line", self.sim.agents, spacing=50)
        self.assertEqual(self.sim.formation_control.formation_type, "line")

        # Simulate agents moving into formation
        initial_error = self.sim.formation_control.get_formation_error(self.sim.agents)
        print(f"Initial formation error: {initial_error:.2f}")
        
        for _ in range(100): # Simulate 10 seconds of movement
            self.sim.update()
            time.sleep(0.1)
        
        final_error = self.sim.formation_control.get_formation_error(self.sim.agents)
        print(f"Final formation error: {final_error:.2f}")
        self.assertLess(final_error, initial_error, "Formation error should decrease over time")

    def test_target_discovery(self):
        self.sim.add_targets([(50, 50)])
        initial_found = self.sim.metrics["targets_found"]
        
        # Move an agent close to the target
        self.sim.agents[0].x = 55
        self.sim.agents[0].y = 55
        self.sim.agents[0].state = AgentState.SEARCHING # Set state to enable sensor update
        
        self.sim.update() # Update simulation to trigger sensor detection
        
        self.assertEqual(self.sim.metrics["targets_found"], initial_found + 1, "Agent should discover the target")
        self.assertIn((50, 50), self.sim.discovered_targets)

    def test_scenario_loading(self):
        # Create a dummy scenario file
        dummy_scenario_path = "./simulation/scenarios/test_scenario.json"
        dummy_scenario_content = {
            "name": "Test Scenario",
            "obstacles": [[10, 10, 20, 20]],
            "targets": [[50, 50]],
            "agents": [
                {"id": 1, "x": 100, "y": 100, "role": "alpha"}
            ]
        }
        with open(dummy_scenario_path, 'w') as f:
            json.dump(dummy_scenario_content, f)
        
        self.sim.load_scenario(dummy_scenario_path)
        self.assertEqual(len(self.sim.obstacles), 1)
        self.assertEqual(len(self.sim.targets), 1)
        self.assertEqual(self.sim.agents[0].x, 100)
        self.assertEqual(self.sim.agents[0].role.value, "alpha")
        
        os.remove(dummy_scenario_path) # Clean up

class TestPerformanceAnalyzer(unittest.TestCase):
    def test_performance_metrics_calculation(self):
        # This would involve running a simulation for a set time
        # and then asserting on the calculated metrics.
        # For now, a placeholder.
        print("Performance metrics test placeholder.")
        pass

if __name__ == '__main__':
    # Run all tests
    unittest.main()
