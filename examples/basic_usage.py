#!/usr/bin/env python3
"""
Basic usage example for the Musical Dynamics Training Software.

This example demonstrates how to use the package programmatically
to process MIDI events and visualize dynamics.
"""

import sys
import time
from pathlib import Path

# Add the src directory to the path so we can import the package
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from musical_dynamics import MidiHandler, DynamicsMapper, ColorMapper, MidiKeyMapper


def main():
    """Demonstrate basic usage of the musical dynamics package."""
    
    print("🎹 Musical Dynamics Training Software - Basic Usage Example")
    print("=" * 60)
    
    # Example 1: Dynamics mapping
    print("\n1. Dynamics Mapping Examples:")
    velocities = [20, 42, 64, 80, 96, 127]
    for velocity in velocities:
        dynamics = DynamicsMapper.get_dynamics(velocity)
        color = ColorMapper.get_color(velocity)
        print(f"   Velocity {velocity:3d} → {dynamics:4s} ({color})")
    
    # Example 2: MIDI key mapping
    print("\n2. MIDI Key Mapping Examples:")
    midi_keys = [21, 60, 88, 108]  # A0, Middle C, E6, C8
    for midi_key in midi_keys:
        piano_key = MidiKeyMapper.midi_to_piano_key(midi_key)
        print(f"   MIDI key {midi_key:3d} → Piano key {piano_key:2d}")
    
    # Example 3: Color mapping for different dynamics
    print("\n3. Color Mapping for Dynamics:")
    dynamics_colors = {
        "pppp": ColorMapper.get_color(8),
        "pp": ColorMapper.get_color(31),
        "p": ColorMapper.get_color(42),
        "mp": ColorMapper.get_color(53),
        "mf": ColorMapper.get_color(64),
        "f": ColorMapper.get_color(80),
        "ff": ColorMapper.get_color(96),
        "fff": ColorMapper.get_color(112),
        "ffff": ColorMapper.get_color(127),
    }
    
    for dynamics, color in dynamics_colors.items():
        print(f"   {dynamics:4s} → {color}")
    
    # Example 4: Simulate MIDI message processing
    print("\n4. Simulated MIDI Message Processing:")
    
    # Simulate some MIDI messages
    midi_messages = [
        # (message_type, midi_key, velocity, description)
        (144, 60, 31, "Middle C - pp (very soft)"),
        (144, 64, 64, "E4 - mf (moderately loud)"),
        (144, 67, 96, "G4 - ff (very loud)"),
        (128, 60, 0, "Middle C - note off"),
    ]
    
    for msg_type, midi_key, velocity, description in midi_messages:
        if msg_type == 144 and velocity > 0:  # Note On
            piano_key = MidiKeyMapper.midi_to_piano_key(midi_key)
            dynamics = DynamicsMapper.get_dynamics(velocity)
            color = ColorMapper.get_color(velocity)
            print(f"   Note On:  {description}")
            print(f"            Piano key: {piano_key}, Dynamics: {dynamics}, Color: {color}")
        elif msg_type == 128 or (msg_type == 144 and velocity == 0):  # Note Off
            piano_key = MidiKeyMapper.midi_to_piano_key(midi_key)
            print(f"   Note Off: Piano key {piano_key}")
        print()
    
    print("✅ Example completed successfully!")
    print("\nTo run the full application with GUI:")
    print("   musical-dynamics-trainer")


if __name__ == "__main__":
    main() 