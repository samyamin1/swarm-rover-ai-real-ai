#!/usr/bin/env python3
"""
Swarm Coordination Algorithms
Advanced algorithms for swarm behavior and coordination
"""

import math
import time
import random
from enum import Enum
from typing import List, Dict, Tuple, Optional
import numpy as np

class AgentRole(Enum):
    FOLLOWER = "follower"
    ALPHA = "alpha"
    SCOUT = "scout"

class AgentState(Enum):
    IDLE = "idle"
    SEARCHING = "searching"
    MOVING_TO_TARGET = "moving_to_target"
    FORMING_UP = "forming_up"
    FOLLOWING_ALPHA = "following_alpha"
    RESCUING = "rescuing"

class TaskType(Enum):
    SEARCH = "search"
    RESCUE = "rescue"
    PATROL = "patrol"
    FORMATION = "formation"
    RECONNAISSANCE = "reconnaissance"

class AgentCapabilities:
    def __init__(self):
        self.search = True
        self.rescue = True
        self.communication = True
        self.formation_flying = True
        self.obstacle_avoidance = True

class AlphaElection:
    """Democratic alpha agent election algorithm"""
    
    def __init__(self):
        self.election_in_progress = False
        self.candidates = {}
        self.votes = {}
        self.election_timeout = 30.0  # 30 seconds
        self.election_start_time = 0.0
    
    def start_election(self, agents):
        """Initiate alpha election process"""
        self.election_in_progress = True
        self.election_start_time = time.time()
        self.candidates = {}
        self.votes = {}
        
        # All agents are potential candidates
        for agent in agents:
            self.candidates[agent.agent_id] = {
                "score": self.calculate_leadership_score(agent),
                "agent": agent
            }
        
        print(f"Alpha election started with {len(self.candidates)} candidates")
        return True
    
    def calculate_leadership_score(self, agent):
        """Calculate leadership capability score for an agent"""
        score = 0.0
        
        # Battery level (30% weight)
        score += agent.battery_level * 0.3
        
        # Experience/uptime (20% weight)
        score += getattr(agent, 'uptime', 100.0) * 0.2
        
        # Communication capability (20% weight)
        if hasattr(agent, 'communication_range'):
            score += (agent.communication_range / 200.0) * 20.0
        
        # Position centrality (15% weight)
        # Agents closer to center of swarm get higher score
        if hasattr(agent, 'centrality_score'):
            score += agent.centrality_score * 0.15
        
        # Agent ID preference (lower IDs preferred) (15% weight)
        score += (100.0 - agent.agent_id) * 0.15
        
        return score
    
    def process_votes(self, agents):
        """Process voting from all agents"""
        if not self.election_in_progress:
            return False
        
        # Each agent votes for the candidate with highest score
        for agent in agents:
            if agent.agent_id in self.candidates:
                best_candidate = max(
                    self.candidates.items(),
                    key=lambda x: x[1]["score"]
                )
                
                if agent.agent_id not in self.votes:
                    self.votes[agent.agent_id] = best_candidate[0]
        
        return len(self.votes) >= len(agents) * 0.6  # 60% participation required
    
    def elect_alpha(self, agents):
        """Complete election and select alpha"""
        if not self.election_in_progress:
            return None
        
        # Count votes
        vote_counts = {}
        for voter_id, candidate_id in self.votes.items():
            vote_counts[candidate_id] = vote_counts.get(candidate_id, 0) + 1
        
        # Select winner
        if vote_counts:
            winner_id = max(vote_counts.items(), key=lambda x: x[1])[0]
            winner_agent = self.candidates[winner_id]["agent"]
            
            # Set roles
            for agent in agents:
                if agent.agent_id == winner_id:
                    agent.role = AgentRole.ALPHA
                else:
                    agent.role = AgentRole.FOLLOWER
            
            self.election_in_progress = False
            print(f"Agent {winner_id} elected as alpha with {vote_counts[winner_id]} votes")
            return winner_agent
        
        return None
    
    def is_election_timeout(self):
        """Check if election has timed out"""
        return (time.time() - self.election_start_time) > self.election_timeout

class TaskSharing:
    """Decentralized task sharing and assignment"""
    
    def __init__(self):
        self.available_tasks = {}
        self.assigned_tasks = {}
        self.task_counter = 0
    
    def announce_task(self, task_type, location, priority="medium", required_agents=1):
        """Announce a new task to the swarm"""
        self.task_counter += 1
        task_id = f"task_{self.task_counter}"
        
        task = {
            "id": task_id,
            "type": task_type,
            "location": location,
            "priority": priority,
            "required_agents": required_agents,
            "assigned_agents": [],
            "status": "available",
            "created_time": time.time()
        }
        
        self.available_tasks[task_id] = task
        print(f"Task {task_id} announced: {task_type} at {location}")
        return task_id
    
    def bid_for_task(self, agent, task_id):
        """Agent bids for a task"""
        if task_id not in self.available_tasks:
            return False
        
        task = self.available_tasks[task_id]
        
        # Calculate bid score based on agent capabilities and distance
        bid_score = self.calculate_bid_score(agent, task)
        
        if "bids" not in task:
            task["bids"] = {}
        
        task["bids"][agent.agent_id] = {
            "agent": agent,
            "score": bid_score,
            "bid_time": time.time()
        }
        
        return True
    
    def calculate_bid_score(self, agent, task):
        """Calculate bid score for agent-task pair"""
        score = 0.0
        
        # Distance factor (closer is better)
        if hasattr(agent, 'position') and 'location' in task:
            distance = math.sqrt(
                (agent.position.x - task["location"][0])**2 +
                (agent.position.y - task["location"][1])**2
            )
            score += max(0, 100 - distance)  # Max 100 points for distance
        
        # Battery level
        score += agent.battery_level * 0.5
        
        # Agent capabilities
        if task["type"] == TaskType.SEARCH and hasattr(agent, 'capabilities'):
            if "search" in agent.capabilities:
                score += 20
        
        if task["type"] == TaskType.RESCUE and hasattr(agent, 'capabilities'):
            if "rescue" in agent.capabilities:
                score += 20
        
        # Current workload (fewer tasks is better)
        current_tasks = len([t for t in self.assigned_tasks.values() 
                           if agent.agent_id in t.get("assigned_agents", [])])
        score -= current_tasks * 10
        
        return score
    
    def assign_tasks(self):
        """Assign tasks based on bids"""
        for task_id, task in list(self.available_tasks.items()):
            if "bids" in task and len(task["bids"]) > 0:
                # Sort bids by score
                sorted_bids = sorted(
                    task["bids"].items(),
                    key=lambda x: x[1]["score"],
                    reverse=True
                )
                
                # Assign to best bidders
                assigned_count = 0
                for agent_id, bid_info in sorted_bids:
                    if assigned_count < task["required_agents"]:
                        task["assigned_agents"].append(agent_id)
                        assigned_count += 1
                
                # Move to assigned tasks
                if len(task["assigned_agents"]) >= task["required_agents"]:
                    task["status"] = "assigned"
                    self.assigned_tasks[task_id] = task
                    del self.available_tasks[task_id]
                    
                    print(f"Task {task_id} assigned to agents {task['assigned_agents']}")
    
    def complete_task(self, task_id, success=True):
        """Mark task as completed"""
        if task_id in self.assigned_tasks:
            task = self.assigned_tasks[task_id]
            task["status"] = "completed" if success else "failed"
            task["completion_time"] = time.time()
            
            print(f"Task {task_id} {'completed' if success else 'failed'}")
            return True
        return False

class FormationControl:
    """Advanced formation control algorithms"""
    
    def __init__(self):
        self.formation_type = "none"
        self.formation_spacing = 50.0
        self.formation_center = (0.0, 0.0)
        self.target_positions = {}
    
    def set_formation(self, formation_type, agents, spacing=50.0, center=None):
        """Set formation for the swarm"""
        self.formation_type = formation_type
        self.formation_spacing = spacing
        
        if center is None:
            # Calculate center of mass
            total_x = sum(agent.x for agent in agents)
            total_y = sum(agent.y for agent in agents)
            self.formation_center = (total_x / len(agents), total_y / len(agents))
        else:
            self.formation_center = center
        
        # Calculate target positions
        self.target_positions = self.calculate_formation_positions(agents)
        
        print(f"Formation set: {formation_type} with {len(agents)} agents")
        return self.target_positions
    
    def calculate_formation_positions(self, agents):
        """Calculate target positions for current formation"""
        positions = {}
        agent_count = len(agents)
        cx, cy = self.formation_center
        
        if self.formation_type == "line":
            for i, agent in enumerate(agents):
                positions[agent.agent_id] = (
                    cx + (i - agent_count/2) * self.formation_spacing,
                    cy
                )
        
        elif self.formation_type == "circle":
            for i, agent in enumerate(agents):
                angle = 2 * math.pi * i / agent_count
                positions[agent.agent_id] = (
                    cx + self.formation_spacing * math.cos(angle),
                    cy + self.formation_spacing * math.sin(angle)
                )
        
        elif self.formation_type == "diamond":
            # Diamond formation for 4+ agents
            if agent_count >= 4:
                diamond_positions = [
                    (cx, cy - self.formation_spacing),      # Top
                    (cx + self.formation_spacing, cy),      # Right
                    (cx, cy + self.formation_spacing),      # Bottom
                    (cx - self.formation_spacing, cy),      # Left
                ]
                
                # Add additional agents in inner diamond
                if agent_count > 4:
                    for i in range(4, min(agent_count, 8)):
                        angle = 2 * math.pi * (i-4) / 4
                        diamond_positions.append((
                            cx + (self.formation_spacing * 0.5) * math.cos(angle),
                            cy + (self.formation_spacing * 0.5) * math.sin(angle)
                        ))
                
                for i, agent in enumerate(agents):
                    if i < len(diamond_positions):
                        positions[agent.agent_id] = diamond_positions[i]
        
        elif self.formation_type == "v_formation":
            for i, agent in enumerate(agents):
                if i == 0:
                    # Leader at the front
                    positions[agent.agent_id] = (cx, cy)
                else:
                    # Alternating sides
                    side = 1 if i % 2 == 1 else -1
                    row = (i + 1) // 2
                    positions[agent.agent_id] = (
                        cx - row * self.formation_spacing * 0.8,
                        cy + side * row * self.formation_spacing * 0.6
                    )
        
        return positions
    
    def update_formation(self, agents):
        """Update agent positions to maintain formation"""
        if self.formation_type == "none":
            return
        
        for agent in agents:
            if agent.agent_id in self.target_positions:
                target_x, target_y = self.target_positions[agent.agent_id]
                
                # Calculate movement vector
                dx = target_x - agent.x
                dy = target_y - agent.y
                distance = math.sqrt(dx*dx + dy*dy)
                
                if distance > 5.0:  # Move if not close enough
                    # Normalize and scale movement
                    max_speed = 2.0
                    if distance > 0:
                        agent.vx = (dx / distance) * max_speed
                        agent.vy = (dy / distance) * max_speed
                else:
                    # Slow down when close
                    agent.vx *= 0.8
                    agent.vy *= 0.8
    
    def get_formation_error(self, agents):
        """Calculate formation error (how far agents are from target positions)"""
        total_error = 0.0
        
        for agent in agents:
            if agent.agent_id in self.target_positions:
                target_x, target_y = self.target_positions[agent.agent_id]
                error = math.sqrt(
                    (agent.x - target_x)**2 +
                    (agent.y - target_y)**2
                )
                total_error += error
        
        return total_error / len(agents) if agents else 0.0

class ConsensusDecisionMaking:
    """Consensus-based decision making for the swarm"""
    
    def __init__(self):
        self.proposals = {}
        self.votes = {}
        self.decisions = {}
        self.consensus_threshold = 0.7  # 70% agreement required
    
    def propose_decision(self, proposer_id, decision_type, options, description=""):
        """Propose a decision to the swarm"""
        proposal_id = f"proposal_{int(time.time())}_{proposer_id}"
        
        proposal = {
            "id": proposal_id,
            "proposer": proposer_id,
            "type": decision_type,
            "options": options,
            "description": description,
            "created_time": time.time(),
            "votes": {},
            "status": "voting"
        }
        
        self.proposals[proposal_id] = proposal
        print(f"Decision proposed: {decision_type} by agent {proposer_id}")
        return proposal_id
    
    def vote_on_proposal(self, proposal_id, voter_id, choice, reasoning=""):
        """Vote on a proposal"""
        if proposal_id not in self.proposals:
            return False
        
        proposal = self.proposals[proposal_id]
        if proposal["status"] != "voting":
            return False
        
        proposal["votes"][voter_id] = {
            "choice": choice,
            "reasoning": reasoning,
            "vote_time": time.time()
        }
        
        return True
    
    def check_consensus(self, proposal_id, total_agents):
        """Check if consensus has been reached"""
        if proposal_id not in self.proposals:
            return False, None
        
        proposal = self.proposals[proposal_id]
        votes = proposal["votes"]
        
        if len(votes) < total_agents * 0.6:  # Need at least 60% participation
            return False, None
        
        # Count votes for each option
        vote_counts = {}
        for vote_info in votes.values():
            choice = vote_info["choice"]
            vote_counts[choice] = vote_counts.get(choice, 0) + 1
        
        # Check if any option has consensus
        for option, count in vote_counts.items():
            if count / len(votes) >= self.consensus_threshold:
                proposal["status"] = "decided"
                proposal["decision"] = option
                proposal["decision_time"] = time.time()
                
                self.decisions[proposal_id] = proposal
                print(f"Consensus reached: {option} for proposal {proposal_id}")
                return True, option
        
        return False, None
    
    def get_active_proposals(self):
        """Get all active proposals"""
        return {pid: p for pid, p in self.proposals.items() 
                if p["status"] == "voting"}

# Utility functions for coordination
def calculate_swarm_center(agents):
    """Calculate the center point of the swarm"""
    if not agents:
        return (0.0, 0.0)
    
    total_x = sum(agent.position.x for agent in agents)
    total_y = sum(agent.position.y for agent in agents)
    return (total_x / len(agents), total_y / len(agents))

def calculate_swarm_spread(agents):
    """Calculate how spread out the swarm is"""
    if len(agents) < 2:
        return 0.0
    
    center_x, center_y = calculate_swarm_center(agents)
    
    total_distance = 0.0
    for agent in agents:
        distance = math.sqrt(
            (agent.position.x - center_x)**2 +
            (agent.position.y - center_y)**2
        )
        total_distance += distance
    
    return total_distance / len(agents)

def find_nearest_agents(agent, all_agents, max_distance=150.0):
    """Find agents within communication range"""
    nearby = []
    
    for other_agent in all_agents:
        if other_agent.agent_id != agent.agent_id:
            distance = math.sqrt(
                (agent.position.x - other_agent.position.x)**2 +
                (agent.position.y - other_agent.position.y)**2
            )
            
            if distance <= max_distance:
                nearby.append((other_agent, distance))
    
    # Sort by distance
    nearby.sort(key=lambda x: x[1])
    return [agent for agent, _ in nearby]
