#!/usr/bin/env python3
"""
Simple Agent for AI Communication Testing
No pygame, no physics, just AI communication
"""

import time
import json
from enum import Enum
from typing import Dict, List, Optional

class AgentState(Enum):
    IDLE = "idle"
    SEND = "send"
    RECEIVE = "receive"
    PROCESSING = "processing"

class SimpleAgent:
    def __init__(self, agent_id: int, name: str):
        """Initialize simple agent"""
        self.agent_id = agent_id
        self.name = name
        self.state = AgentState.IDLE
        self.messages_sent = 0
        self.messages_received = 0
        self.last_message = None
        self.last_response = None
        self.start_time = time.time()
        
        print(f"SimpleAgent {self.name} (ID: {self.agent_id}) initialized")
    
    def send_message(self, message: str) -> str:
        """Send a message and return response"""
        self.state = AgentState.SEND
        self.messages_sent += 1
        self.last_message = message
        
        print(f"[{self.name}] Sending: {message}")
        
        # Simulate processing time
        time.sleep(0.1)
        
        self.state = AgentState.IDLE
        return f"Message sent: {message}"
    
    def receive_message(self, message: str) -> str:
        """Receive a message and return acknowledgment"""
        self.state = AgentState.RECEIVE
        self.messages_received += 1
        self.last_message = message
        
        print(f"[{self.name}] Received: {message}")
        
        # Simulate processing time
        time.sleep(0.1)
        
        self.state = AgentState.IDLE
        return f"Message received: {message}"
    
    def get_status(self) -> Dict:
        """Get agent status"""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "messages_sent": self.messages_sent,
            "messages_received": self.messages_received,
            "uptime": time.time() - self.start_time,
            "last_message": self.last_message
        }
    
    def reset(self):
        """Reset agent state"""
        self.state = AgentState.IDLE
        self.messages_sent = 0
        self.messages_received = 0
        self.last_message = None
        self.last_response = None
        print(f"[{self.name}] Reset completed") 