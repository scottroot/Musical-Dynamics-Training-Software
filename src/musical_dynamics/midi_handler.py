"""
MIDI input handling for the Musical Dynamics Training Software.
"""

import logging
import sys
from typing import Optional, Tuple, Callable
from rtmidi.midiutil import open_midiinput
from .constants import DynamicsMapper, ColorMapper, MidiKeyMapper


class MidiHandler:
    """Handles MIDI input and processes MIDI messages."""
    
    def __init__(self, port_name: Optional[str] = None):
        """
        Initialize MIDI handler.
        
        Args:
            port_name: MIDI port name or number. If None, will prompt for selection.
        """
        self.port_name = port_name
        self.midiin = None
        self.port_name_actual = None
        self.logger = logging.getLogger(__name__)
        self._setup_midi()
    
    def _setup_midi(self) -> None:
        """Set up MIDI input connection."""
        try:
            self.midiin, self.port_name_actual = open_midiinput(self.port_name)
            self.logger.info(f"Connected to MIDI port: {self.port_name_actual}")
        except (EOFError, KeyboardInterrupt):
            self.logger.error("Failed to open MIDI input")
            sys.exit(1)
        except Exception as e:
            self.logger.error(f"Unexpected error setting up MIDI: {e}")
            sys.exit(1)
    
    def get_message(self) -> Optional[Tuple[list, float]]:
        """
        Get the next MIDI message.
        
        Returns:
            Tuple of (message, deltatime) or None if no message available
        """
        if self.midiin is None:
            return None
        
        return self.midiin.get_message()
    
    def process_message(self, message: list, deltatime: float) -> Optional[dict]:
        """
        Process a MIDI message and extract relevant information.
        
        Args:
            message: MIDI message as list
            deltatime: Time delta since last message
            
        Returns:
            Dictionary with processed message data or None if not a note event
        """
        if len(message) < 3:
            return None
        
        message_type = message[0]
        midi_key = message[1]
        velocity = message[2]
        
        # Note On event (144 = 0x90)
        if message_type == 144 and velocity > 0:
            try:
                piano_key = MidiKeyMapper.midi_to_piano_key(midi_key)
                dynamics = DynamicsMapper.get_dynamics(velocity)
                color = ColorMapper.get_color(velocity)
                
                return {
                    'type': 'note_on',
                    'midi_key': midi_key,
                    'piano_key': piano_key,
                    'velocity': velocity,
                    'dynamics': dynamics,
                    'color': color,
                    'deltatime': deltatime
                }
            except ValueError as e:
                self.logger.warning(f"Invalid MIDI key or velocity: {e}")
                return None
        
        # Note Off event (128 = 0x80) or Note On with velocity 0
        elif message_type == 128 or (message_type == 144 and velocity == 0):
            try:
                piano_key = MidiKeyMapper.midi_to_piano_key(midi_key)
                
                return {
                    'type': 'note_off',
                    'midi_key': midi_key,
                    'piano_key': piano_key,
                    'deltatime': deltatime
                }
            except ValueError as e:
                self.logger.warning(f"Invalid MIDI key: {e}")
                return None
        
        return None
    
    def close(self) -> None:
        """Close MIDI connection and cleanup resources."""
        if self.midiin:
            self.midiin.close_port()
            del self.midiin
            self.logger.info("MIDI connection closed")
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


def setup_midi_input(port_name: Optional[str] = None) -> MidiHandler:
    """
    Convenience function to create a MIDI handler.
    
    Args:
        port_name: MIDI port name or number
        
    Returns:
        Configured MidiHandler instance
    """
    return MidiHandler(port_name) 