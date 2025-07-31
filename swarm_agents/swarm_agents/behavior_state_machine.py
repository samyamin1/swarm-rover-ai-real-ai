#!/usr/bin/env python3
"""
Agent Behavior State Machine
Defines the states and transitions for agent behavior
"""

from enum import Enum, auto

class AgentState(Enum):
    IDLE = auto()
    SEARCHING = auto()
    MOVING_TO_TARGET = auto()
    FORMING_UP = auto()
    FOLLOWING_ALPHA = auto()
    RESCUING = auto()
    RETURNING_HOME = auto()
    AVOIDING_OBSTACLE = auto()
    TASK_BIDDING = auto()
    AWAITING_INSTRUCTIONS = auto()

class BehaviorStateMachine:
    def __init__(self, agent):
        self.agent = agent
        self.state = AgentState.IDLE
        self.transitions = {
            AgentState.IDLE: [AgentState.SEARCHING, AgentState.AWAITING_INSTRUCTIONS, AgentState.TASK_BIDDING],
            AgentState.SEARCHING: [AgentState.MOVING_TO_TARGET, AgentState.AVOIDING_OBSTACLE, AgentState.IDLE],
            AgentState.MOVING_TO_TARGET: [AgentState.RESCUING, AgentState.FORMING_UP, AgentState.IDLE],
            AgentState.FORMING_UP: [AgentState.FOLLOWING_ALPHA, AgentState.IDLE],
            AgentState.FOLLOWING_ALPHA: [AgentState.SEARCHING, AgentState.MOVING_TO_TARGET, AgentState.IDLE],
            AgentState.RESCUING: [AgentState.RETURNING_HOME, AgentState.IDLE],
            AgentState.RETURNING_HOME: [AgentState.IDLE],
            AgentState.AVOIDING_OBSTACLE: [AgentState.SEARCHING, AgentState.MOVING_TO_TARGET],
            AgentState.TASK_BIDDING: [AgentState.AWAITING_INSTRUCTIONS, AgentState.IDLE],
            AgentState.AWAITING_INSTRUCTIONS: [AgentState.SEARCHING, AgentState.MOVING_TO_TARGET, AgentState.FORMING_UP]
        }

    def transition_to(self, new_state):
        if new_state in self.transitions.get(self.state, []):
            self.agent.get_logger().info(f'Agent {self.agent.agent_id} transitioning from {self.state.name} to {new_state.name}')
            self.state = new_state
            self.agent.state = self.state # Update agent's state
            return True
        else:
            self.agent.get_logger().warn(f'Agent {self.agent.agent_id} invalid transition from {self.state.name} to {new_state.name}')
            return False

    def run(self):
        # This method would be called in the agent's update loop
        # to execute the behavior associated with the current state.
        state_method = getattr(self.agent, f'{self.state.name.lower()}_behavior', None)
        if state_method:
            state_method()
