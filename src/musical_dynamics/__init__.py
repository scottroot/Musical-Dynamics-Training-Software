"""
Musical Dynamics Training Software

A Python application for training and visualizing musical dynamics on digital pianos.
"""

__version__ = "0.1.0"
__author__ = "Scott Hendrix"
__email__ = "scott@example.com"

from .config import Config
from .constants import DynamicsMapper, ColorMapper, MidiKeyMapper
from .midi_handler import MidiHandler
from .gui import DynamicsVisualizer

__all__ = [
    "Config",
    "DynamicsMapper",
    "ColorMapper",
    "MidiKeyMapper",
    "MidiHandler",
    "DynamicsVisualizer",
]