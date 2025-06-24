"""
Configuration settings for the Musical Dynamics Training Software.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Config:
    """Configuration settings for the application."""
    
    # Window settings
    window_width: int = 1300
    window_height: int = 624
    window_title: str = "Musical Dynamics Trainer"
    
    # Canvas settings
    y_gap: int = 182  # Gap between lower canvas edge and x axis
    y_stretch: int = 3  # Highest y = max_data_value * y_stretch
    y0_init: int = 439  # Height of bars when not active (624 - 182 - 3)
    x_gap: int = 80  # Gap between left canvas edge and y axis
    x_stretch: float = 1.25  # Stretch x wide enough to fit the variables
    x_width: float = 11.5  # Width of the x-axis
    
    # Colors
    background_color: str = "#161616"
    text_color: str = "#efcf83"
    text_font: str = "Georgia 20 bold"
    
    # MIDI settings
    default_midi_port: str = "0"
    
    # File paths
    piano_image_path: Optional[Path] = None
    
    def __post_init__(self) -> None:
        """Set default piano image path if not provided."""
        if self.piano_image_path is None:
            # Try to find the piano image relative to this package
            package_dir = Path(__file__).parent.parent.parent
            possible_paths = [
                package_dir / "img" / "piano_3.png",
                package_dir / "app" / "img" / "piano_3.png",
                Path("img") / "piano_3.png",
            ]
            
            for path in possible_paths:
                if path.exists():
                    self.piano_image_path = path
                    break
            else:
                # If no image found, set to None and handle gracefully
                self.piano_image_path = None


# Global configuration instance
config = Config() 