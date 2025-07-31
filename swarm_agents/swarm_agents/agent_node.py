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
