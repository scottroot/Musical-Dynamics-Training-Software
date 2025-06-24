"""
Constants and mapping utilities for the Musical Dynamics Training Software.
"""

import numpy as np
from typing import Dict, List, Tuple


class DynamicsMapper:
    """Maps MIDI velocity values to musical dynamics notation."""
    
    # Velocity thresholds for dynamics
    DYNAMICS_THRESHOLDS = {
        8: "pppp",    # pianississimo
        20: "ppp",    # pianissimo
        31: "pp",     # piano
        42: "p",      # mezzo-piano
        53: "mp",     # mezzo-piano
        64: "mf",     # mezzo-forte
        80: "f",      # forte
        96: "ff",     # fortissimo
        112: "fff",   # fortississimo
        127: "ffff",  # fortississimo
    }
    
    # Descriptions for dynamics
    DYNAMICS_DESCRIPTIONS = {
        "pppp": "extremely soft",
        "ppp": "very soft", 
        "pp": "very soft",
        "p": "soft",
        "mp": "moderately soft",
        "mf": "moderately loud",
        "f": "loud",
        "ff": "very loud",
        "fff": "extremely loud",
        "ffff": "extremely loud",
    }
    
    @classmethod
    def get_dynamics(cls, velocity: int) -> str:
        """
        Convert MIDI velocity to standard dynamics notation.
        
        Args:
            velocity: MIDI velocity value (1-127)
            
        Returns:
            Dynamics notation (pp, p, mp, mf, f, ff, etc.)
            
        Raises:
            ValueError: If velocity is outside valid range (1-127)
        """
        if not 1 <= velocity <= 127:
            raise ValueError(f"Velocity must be between 1 and 127, got {velocity}")
        
        # Find the closest threshold
        thresholds = list(cls.DYNAMICS_THRESHOLDS.keys())
        closest_threshold = min(thresholds, key=lambda x: abs(x - velocity))
        return cls.DYNAMICS_THRESHOLDS[closest_threshold]
    
    @classmethod
    def get_dynamics_with_description(cls, velocity: int) -> Tuple[str, str]:
        """
        Convert MIDI velocity to dynamics notation with description.
        
        Args:
            velocity: MIDI velocity value (1-127)
            
        Returns:
            Tuple of (dynamics_notation, description)
        """
        dynamics = cls.get_dynamics(velocity)
        description = cls.DYNAMICS_DESCRIPTIONS.get(dynamics, "")
        return dynamics, description


class ColorMapper:
    """Maps MIDI velocity values to colors for visualization."""
    
    # Color mapping using velocity ranges
    COLOR_RANGES = [
        (0, 8, "#0E0050"),
        (8, 11, "#0E0066"),
        (11, 17, "#14056B"),
        (17, 20, "#1B0B70"),
        (20, 22, "#221175"),
        (22, 28, "#29167B"),
        (28, 31, "#2F1C80"),
        (31, 33, "#362285"),
        (33, 39, "#3D278A"),
        (39, 42, "#442D90"),
        (42, 44, "#4A3395"),
        (44, 50, "#51389A"),
        (50, 53, "#583E9F"),
        (53, 55, "#5F44A5"),
        (55, 61, "#6E44A2"),
        (61, 64, "#7D449F"),
        (64, 68, "#8D449D"),
        (68, 76, "#B34F7D"),
        (76, 80, "#D95A5E"),
        (80, 84, "#FF663F"),
        (84, 92, "#FF5336"),
        (92, 96, "#FF402D"),
        (96, 100, "#FF2D25"),
        (100, 108, "#FF4544"),
        (108, 112, "#FF5D63"),
        (112, 115, "#FF7582"),
        (115, 123, "#FF939A"),
        (123, 127, "#FFB1B3"),
        (127, 128, "#FFD0CC"),
    ]
    
    @classmethod
    def get_color(cls, velocity: int) -> str:
        """
        Get color for a given MIDI velocity value.
        
        Args:
            velocity: MIDI velocity value (0-127)
            
        Returns:
            Hex color code
            
        Raises:
            ValueError: If velocity is outside valid range (0-127)
        """
        if not 0 <= velocity <= 127:
            raise ValueError(f"Velocity must be between 0 and 127, got {velocity}")
        
        for min_vel, max_vel, color in cls.COLOR_RANGES:
            if min_vel <= velocity < max_vel:
                return color
        
        # Fallback for edge case
        return "#FFD0CC"


class MidiKeyMapper:
    """Maps MIDI key numbers to piano key numbers."""
    
    # MIDI key to piano key mapping (MIDI key: piano key)
    MIDI_TO_PIANO = {
        108: 88, 107: 87, 106: 86, 105: 85, 104: 84, 103: 83, 102: 82, 101: 81, 100: 80,
        99: 79, 98: 78, 97: 77, 96: 76, 95: 75, 94: 74, 93: 73, 92: 72, 91: 71, 90: 70,
        89: 69, 88: 68, 87: 67, 86: 66, 85: 65, 84: 64, 83: 63, 82: 62, 81: 61, 80: 60,
        79: 59, 78: 58, 77: 57, 76: 56, 75: 55, 74: 54, 73: 53, 72: 52, 71: 51, 70: 50,
        69: 49, 68: 48, 67: 47, 66: 46, 65: 45, 64: 44, 63: 43, 62: 42, 61: 41, 60: 40,
        59: 39, 58: 38, 57: 37, 56: 36, 55: 35, 54: 34, 53: 33, 52: 32, 51: 31, 50: 30,
        49: 29, 48: 28, 47: 27, 46: 26, 45: 25, 44: 24, 43: 23, 42: 22, 41: 21, 40: 20,
        39: 19, 38: 18, 37: 17, 36: 16, 35: 15, 34: 14, 33: 13, 32: 12, 31: 11, 30: 10,
        29: 9, 28: 8, 27: 7, 26: 6, 25: 5, 24: 4, 23: 3, 22: 2, 21: 1
    }
    
    @classmethod
    def midi_to_piano_key(cls, midi_key: int) -> int:
        """
        Convert MIDI key number to piano key number.
        
        Args:
            midi_key: MIDI key number (21-108)
            
        Returns:
            Piano key number (1-88)
            
        Raises:
            ValueError: If MIDI key is not in valid range
        """
        if midi_key not in cls.MIDI_TO_PIANO:
            raise ValueError(f"MIDI key {midi_key} is not in valid range (21-108)")
        
        return cls.MIDI_TO_PIANO[midi_key]
    
    @classmethod
    def piano_to_midi_key(cls, piano_key: int) -> int:
        """
        Convert piano key number to MIDI key number.
        
        Args:
            piano_key: Piano key number (1-88)
            
        Returns:
            MIDI key number (21-108)
            
        Raises:
            ValueError: If piano key is not in valid range
        """
        if not 1 <= piano_key <= 88:
            raise ValueError(f"Piano key {piano_key} is not in valid range (1-88)")
        
        # Reverse lookup
        for midi_key, p_key in cls.MIDI_TO_PIANO.items():
            if p_key == piano_key:
                return midi_key
        
        raise ValueError(f"Piano key {piano_key} not found in mapping")


# Backward compatibility aliases
dynamicsDict = DynamicsMapper.DYNAMICS_THRESHOLDS
midikeyDict = MidiKeyMapper.MIDI_TO_PIANO

def midi_dynamics(velocity: int) -> str:
    """Backward compatibility function."""
    return DynamicsMapper.get_dynamics(velocity)

def dynamics_color(velocity: int) -> str:
    """Backward compatibility function."""
    return ColorMapper.get_color(velocity) 