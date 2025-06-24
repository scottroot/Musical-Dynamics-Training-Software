import random
import time
from .constants import DynamicsMapper, ColorMapper, MidiKeyMapper

class MockMidiHandler:
    """
    Mock MIDI handler that simulates MIDI input for testing purposes.
    """
    def __init__(self, *args, **kwargs):
        self.counter = 0
        self.last_note = 60  # Start with Middle C
        self.last_velocity = 64
        self.active = True

    def get_message(self):
        # Simulate a note on every 1 second, then a note off
        time.sleep(1)
        self.counter += 1
        if self.counter % 2 == 1:
            # Note On: [144, midi_key, velocity]
            self.last_note = random.randint(60, 72)
            self.last_velocity = random.randint(30, 127)
            return [[144, self.last_note, self.last_velocity], 0.1]
        else:
            # Note Off: [128, midi_key, 0]
            return [[128, self.last_note, 0], 0.1]

    def process_message(self, message, deltatime):
        if len(message) < 3:
            return None
        message_type = message[0]
        midi_key = message[1]
        velocity = message[2]
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
            except Exception:
                return None
        elif message_type == 128 or (message_type == 144 and velocity == 0):
            try:
                piano_key = MidiKeyMapper.midi_to_piano_key(midi_key)
                return {
                    'type': 'note_off',
                    'midi_key': midi_key,
                    'piano_key': piano_key,
                    'deltatime': deltatime
                }
            except Exception:
                return None
        return None

    def close(self):
        self.active = False