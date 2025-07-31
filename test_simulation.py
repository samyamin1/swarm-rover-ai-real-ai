#!/usr/bin/env python3
"""
Simple test script to debug simulation startup
"""

import os
import sys

print("Starting test script...")

try:
    print("Importing pygame...")
    import pygame
    print("Pygame imported successfully")
    
    print("Setting up display...")
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    pygame.init()
    pygame.display.set_mode((1, 1))
    print("Display setup successful")
    
    print("Importing simulation modules...")
    from swarm_agents.perception_bridge import PerceptionBridge
    print("PerceptionBridge imported successfully")
    
    print("Creating perception bridge...")
    pb = PerceptionBridge()
    print("PerceptionBridge created successfully")
    
    print("Test completed successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1) 