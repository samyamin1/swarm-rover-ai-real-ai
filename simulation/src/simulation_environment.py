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
from datetime import datetime
import os
from enum import Enum
from typing import List, Tuple, Dict, Optional
import numpy as np

# Import coordination algorithms
from swarm_agents.coordination_algorithms import AgentRole, AgentState, TaskType, AgentCapabilities
from swarm_agents.coordination_algorithms import AlphaElection, TaskSharing, FormationControl, ConsensusDecisionMaking
from swarm_agents.perception_bridge import PerceptionBridge

class SimulationAgent:
    """Agent representation in simulation"""
    
    def __init__(self, agent_id: int, x: float, y: float, perception_bridge):
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
        self.perception_bridge = perception_bridge # New: AI bridge
        self.last_ai_decision_time = time.time()
        self.ai_decision_interval = 5.0 # Make AI decisions every 5 seconds
        
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
        
        # AI-driven decision making
        if time.time() - self.last_ai_decision_time > self.ai_decision_interval:
            self.last_ai_decision_time = time.time()
            scene_description = self._get_local_scene_description(obstacles, targets, other_agents)
            vlm_output, ai_decision = self.perception_bridge.process_perception_input(scene_description)
            self._apply_ai_decision(ai_decision)

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

    def _get_local_scene_description(self, obstacles: List, targets: List, other_agents: List) -> str:
        """Generates a textual description of the agent's local environment."""
        description = f"Agent {self.agent_id} at ({self.x:.1f}, {self.y:.1f}). "
        
        if self.detected_obstacles:
            description += "Detected obstacles: "
            for obs in self.detected_obstacles:
                description += f"a rectangle at ({obs[0]:.1f}, {obs[1]:.1f}) with size {obs[2]}x{obs[3]}; "
        
        if self.discovered_targets:
            description += "Discovered targets: "
            for target in self.discovered_targets:
                description += f"a target at ({target[0]:.1f}, {target[1]:.1f}); "
        
        if self.detected_agents:
            description += "Detected other agents: "
            for agent in self.detected_agents:
                description += f"Agent {agent.agent_id} ({agent.role.value}) at ({agent.x:.1f}, {agent.y:.1f}); "
        
        if not self.detected_obstacles and not self.discovered_targets and not self.detected_agents:
            description += "No significant objects or agents detected in immediate vicinity."
            
        return description

    def _apply_ai_decision(self, decision: str):
        """Applies the AI's decision to the agent's state and target."""
        decision = decision.strip().upper()
        print(f"Agent {self.agent_id} applying AI decision: {decision}")

        if decision.startswith("MOVE_TO_TARGET"):
            try:
                parts = decision.split(" ")
                coords = parts[1].split(",")
                target_x = float(coords[0])
                target_y = float(coords[1])
                self.target_x = target_x
                self.target_y = target_y
                self.state = AgentState.MOVING_TO_TARGET
            except (IndexError, ValueError):
                print(f"Agent {self.agent_id}: Invalid MOVE_TO_TARGET command: {decision}")
                self.state = AgentState.IDLE
        elif decision == "SEARCH_AREA":
            self.state = AgentState.SEARCHING
            # Randomly pick a new search target if current one is reached or invalid
            if abs(self.x - self.target_x) < 10 and abs(self.y - self.target_y) < 10:
                angle = random.uniform(0, 2 * math.pi)
                distance = random.uniform(50, 150)
                self.target_x = self.x + distance * math.cos(angle)
                self.target_y = self.y + distance * math.sin(angle)
        elif decision == "REPORT_FINDING":
            # This would typically involve publishing a ROS2 message
            print(f"Agent {self.agent_id}: Reporting finding (placeholder).")
            self.state = AgentState.IDLE
        elif decision == "IDLE":
            self.state = AgentState.IDLE
        else:
            print(f"Agent {self.agent_id}: Unknown AI decision: {decision}. Defaulting to IDLE.")
            self.state = AgentState.IDLE

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
    
    def __init__(self, width=1200, height=800, num_agents=8, perception_bridge=None):
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
        
        # AI Integration
        if perception_bridge is None:
            self.perception_bridge = PerceptionBridge()
        else:
            self.perception_bridge = perception_bridge

        # Simulation state
        self.simulation_time = 0.0
        self.frame_count = 0
        self.fps = 60
        self.max_simulation_time = 120  # Default 2 minutes timeout
        
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

        # Setup logging for this simulation run
        self._setup_logger()
    
    def _setup_logger(self):
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file_path = os.path.join(log_dir, f"simulation_log_{timestamp}.txt")
        with open(self.log_file_path, "w") as f:
            f.write("Simulation Log - {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            f.write("----------------------------------------\n")

    def _log_simulation_end(self):
        with open(self.log_file_path, "a") as f:
            f.write("\nSimulation Ended at: {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            f.write(f"Final Metrics:\n")
            for key, value in self.metrics.items():
                f.write(f"  {key}: {value}\n")

    def create_agents(self):
        """Create initial agent population"""
        self.agents = []
        
        for i in range(self.num_agents):
            # Random initial positions
            x = random.uniform(100, self.width - 100)
            y = random.uniform(100, self.height - 100)
            
            agent = SimulationAgent(i + 1, x, y, self.perception_bridge)
            self.agents.append(agent)
        
        print(f"Created {len(self.agents)} agents")
    
    def setup_display(self):
        """Setup pygame display"""
        try:
            # Try to set up display normally
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption("Swarm Rover AI Simulation")
            self.running = True
            self.headless = False
            print("Simulation running with display")
        except pygame.error:
            # If no display available, run in headless mode
            os.environ['SDL_VIDEODRIVER'] = 'dummy'
            pygame.display.set_mode((1, 1))
            self.screen = None
            self.running = True
            self.headless = True
            print("Simulation running in headless mode")
    
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
        if self.screen is None or self.headless:
            # In headless mode, just print status
            if self.frame_count % 60 == 0:  # Print every 60 frames (1 second)
                print(f"Simulation running - Time: {self.simulation_time:.1f}s, Targets: {len(self.targets)} remaining, Found: {len(self.discovered_targets)}")
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
        
        print("Starting simulation...")
        max_frames = 7200  # 2 minutes at 60 FPS
        frame_count = 0
        
        while self.running:
            self.update()
            self.render()
            
            if not self.headless and self.screen is not None:
                pygame.display.flip()
            
            self.clock.tick(self.fps)
            frame_count += 1
            
            # Stop criteria to prevent infinite loops
            if self.simulation_time > self.max_simulation_time:
                print(f"Simulation timeout reached ({self.max_simulation_time} seconds)")
                break
                
            if frame_count > max_frames:
                print(f"Frame limit reached ({max_frames} frames)")
                break
                
            # Stop if all targets are found
            if len(self.discovered_targets) >= len(self.targets) and len(self.targets) > 0:
                print("All targets discovered! Ending simulation.")
                break
                
            # Stop if no progress for 30 seconds
            if self.simulation_time > 30 and len(self.discovered_targets) == 0:
                print("No targets found in 30 seconds. Ending simulation.")
                break
        
        print(f"Simulation ended after {self.simulation_time:.1f} seconds and {frame_count} frames")
        self.cleanup()
        self._log_simulation_end()
    
    def cleanup(self):
        """Cleanup simulation"""
        pygame.quit()
        print("Simulation ended")

def main():
    """Main function for testing simulation"""
    import sys
    
    # Parse command line arguments
    max_time = 120  # Default 2 minutes
    if len(sys.argv) > 1:
        try:
            max_time = int(sys.argv[1])
        except ValueError:
            print("Usage: python simulation_environment.py [max_time_seconds]")
            print("Default: 120 seconds")
    
    print(f"Starting simulation with {max_time} second timeout...")
    
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
    
    # Set custom timeout
    sim.max_simulation_time = max_time
    
    # Run simulation
    sim.run()

if __name__ == "__main__":
    main()
