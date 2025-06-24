"""
Tests for the constants module.
"""

import pytest
from musical_dynamics.constants import (
    DynamicsMapper,
    ColorMapper,
    MidiKeyMapper,
    midi_dynamics,
    dynamics_color
)


class TestDynamicsMapper:
    """Test the DynamicsMapper class."""
    
    def test_get_dynamics_valid_velocities(self):
        """Test dynamics mapping for valid velocity values."""
        test_cases = [
            (8, "pppp"),
            (20, "ppp"),
            (31, "pp"),
            (42, "p"),
            (53, "mp"),
            (64, "mf"),
            (80, "f"),
            (96, "ff"),
            (112, "fff"),
            (127, "ffff"),
        ]
        
        for velocity, expected in test_cases:
            assert DynamicsMapper.get_dynamics(velocity) == expected
    
    def test_get_dynamics_intermediate_velocities(self):
        """Test dynamics mapping for intermediate velocity values."""
        test_cases = [
            (15, "ppp"),   # Closer to 20 than 8
            (35, "pp"),    # Closer to 31 than 42
            (58, "mp"),    # Closer to 53 than 64
            (72, "mf"),    # Closer to 64 than 80
            (88, "f"),     # Closer to 80 than 96
            (104, "ff"),   # Closer to 96 than 112
            (120, "fff"),  # Closer to 112 than 127
        ]
        
        for velocity, expected in test_cases:
            assert DynamicsMapper.get_dynamics(velocity) == expected
    
    def test_get_dynamics_invalid_velocities(self):
        """Test that invalid velocities raise ValueError."""
        invalid_velocities = [0, -1, 128, 200]
        
        for velocity in invalid_velocities:
            with pytest.raises(ValueError):
                DynamicsMapper.get_dynamics(velocity)
    
    def test_get_dynamics_with_description(self):
        """Test getting dynamics with description."""
        dynamics, description = DynamicsMapper.get_dynamics_with_description(31)
        assert dynamics == "pp"
        assert description == "very soft"


class TestColorMapper:
    """Test the ColorMapper class."""
    
    def test_get_color_valid_velocities(self):
        """Test color mapping for valid velocity values."""
        test_cases = [
            (0, "#0E0050"),
            (8, "#0E0066"),
            (31, "#2F1C80"),
            (64, "#8D449D"),
            (80, "#FF663F"),
            (96, "#FF2D25"),
            (127, "#FFD0CC"),
        ]
        
        for velocity, expected in test_cases:
            assert ColorMapper.get_color(velocity) == expected
    
    def test_get_color_invalid_velocities(self):
        """Test that invalid velocities raise ValueError."""
        invalid_velocities = [-1, 128, 200]
        
        for velocity in invalid_velocities:
            with pytest.raises(ValueError):
                ColorMapper.get_color(velocity)


class TestMidiKeyMapper:
    """Test the MidiKeyMapper class."""
    
    def test_midi_to_piano_key_valid_keys(self):
        """Test MIDI to piano key conversion for valid keys."""
        test_cases = [
            (21, 1),   # A0
            (60, 40),  # Middle C
            (88, 68),  # E6
            (108, 88), # C8
        ]
        
        for midi_key, expected in test_cases:
            assert MidiKeyMapper.midi_to_piano_key(midi_key) == expected
    
    def test_midi_to_piano_key_invalid_keys(self):
        """Test that invalid MIDI keys raise ValueError."""
        invalid_keys = [20, 109, 200]
        
        for midi_key in invalid_keys:
            with pytest.raises(ValueError):
                MidiKeyMapper.midi_to_piano_key(midi_key)
    
    def test_piano_to_midi_key_valid_keys(self):
        """Test piano to MIDI key conversion for valid keys."""
        test_cases = [
            (1, 21),   # A0
            (40, 60),  # Middle C
            (68, 88),  # E6
            (88, 108), # C8
        ]
        
        for piano_key, expected in test_cases:
            assert MidiKeyMapper.piano_to_midi_key(piano_key) == expected
    
    def test_piano_to_midi_key_invalid_keys(self):
        """Test that invalid piano keys raise ValueError."""
        invalid_keys = [0, 89, 200]
        
        for piano_key in invalid_keys:
            with pytest.raises(ValueError):
                MidiKeyMapper.piano_to_midi_key(piano_key)
    
    def test_bidirectional_mapping(self):
        """Test that MIDI to piano and back gives the same result."""
        for midi_key in range(21, 109):
            piano_key = MidiKeyMapper.midi_to_piano_key(midi_key)
            back_to_midi = MidiKeyMapper.piano_to_midi_key(piano_key)
            assert back_to_midi == midi_key


class TestBackwardCompatibility:
    """Test backward compatibility functions."""
    
    def test_midi_dynamics_function(self):
        """Test the backward compatibility midi_dynamics function."""
        assert midi_dynamics(31) == "pp"
        assert midi_dynamics(64) == "mf"
        assert midi_dynamics(127) == "ffff"
    
    def test_dynamics_color_function(self):
        """Test the backward compatibility dynamics_color function."""
        assert dynamics_color(31) == "#2F1C80"
        assert dynamics_color(64) == "#8D449D"
        assert dynamics_color(127) == "#FFD0CC" 