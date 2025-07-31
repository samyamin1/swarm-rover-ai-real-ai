#!/usr/bin/env python3
"""
Alpha Agent Implementation
Provides leadership and coordination for the swarm
"""

from .agent_node import BaseAgent, AgentState, AgentRole
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
