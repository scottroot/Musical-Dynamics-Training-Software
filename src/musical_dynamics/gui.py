"""
GUI module for the Musical Dynamics Training Software.
"""

import logging
import time
from typing import Optional, Dict, Any
from tkinter import Tk, Canvas, Label, PhotoImage
from .config import config
from .midi_handler import MidiHandler
from .constants import DynamicsMapper, ColorMapper, MidiKeyMapper


class DynamicsVisualizer:
    """Main GUI class for visualizing musical dynamics."""
    
    def __init__(self, midi_handler: MidiHandler):
        """
        Initialize the dynamics visualizer.
        
        Args:
            midi_handler: Configured MIDI handler instance
        """
        self.midi_handler = midi_handler
        self.logger = logging.getLogger(__name__)
        
        # Initialize GUI components
        self.root = None
        self.canvas = None
        self.dynamics_label = None
        self.piano_image = None
        self.piano_image_id = None
        
        # Animation state
        self.active_bars: Dict[int, int] = {}  # piano_key -> canvas_rectangle_id
        
        self._setup_gui()
    
    def _setup_gui(self) -> None:
        """Set up the main GUI window and components."""
        # Create main window
        self.root = Tk()
        self.root.title(config.window_title)
        
        # Center window on screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (config.window_width // 2)
        y = (screen_height // 2) - (config.window_height // 2)
        self.root.geometry(f'{config.window_width}x{config.window_height}+{x}+{y}')
        
        # Create canvas
        self.canvas = Canvas(
            self.root,
            width=config.window_width,
            height=config.window_height,
            bd=0,
            highlightthickness=0,
            bg=config.background_color
        )
        self.canvas.grid(rowspan=30, row=0, column=0)
        
        # Create dynamics label
        self.dynamics_label = Label(
            self.root,
            text="Dynamics",
            font=config.text_font,
            foreground=config.text_color,
            bg=config.background_color
        )
        self.dynamics_label.grid(row=0, column=0)
        
        # Load piano image
        self._load_piano_image()
        
        # Bind close handler
        self.root.bind('<Escape>', self._close_gui)
    
    def _load_piano_image(self) -> None:
        """Load and display the piano background image."""
        if config.piano_image_path and config.piano_image_path.exists():
            try:
                self.piano_image = PhotoImage(file=str(config.piano_image_path))
                self.piano_image_id = self.canvas.create_image(
                    config.window_width,
                    config.window_height,
                    image=self.piano_image
                )
                # Center the image
                self.canvas.move(
                    self.piano_image_id,
                    -config.window_width // 2,
                    -config.window_height // 2
                )
            except Exception as e:
                self.logger.warning(f"Failed to load piano image: {e}")
        else:
            self.logger.warning("Piano image not found, running without background")
    
    def _close_gui(self, event: Optional[Any] = None) -> None:
        """Handle GUI close event."""
        self.logger.info("Closing application")
        self.root.withdraw()
        self.midi_handler.close()
        self.root.quit()
        self.root.destroy()
    
    def _calculate_bar_coordinates(self, piano_key: int, velocity: int) -> tuple:
        """
        Calculate the coordinates for a dynamics bar.
        
        Args:
            piano_key: Piano key number (1-88)
            velocity: MIDI velocity (0-127)
            
        Returns:
            Tuple of (x0, y0, x1, y1) coordinates
        """
        x0 = piano_key * config.x_stretch + piano_key * config.x_width + config.x_gap
        y0 = config.window_height - config.y_gap - velocity * config.y_stretch
        x1 = piano_key * config.x_stretch + piano_key * config.x_width + config.x_gap + config.x_width
        y1 = config.window_height - config.y_gap
        
        return x0, y0, x1, y1
    
    def _handle_note_on(self, data: Dict[str, Any]) -> None:
        """Handle note on event and create/update dynamics bar."""
        piano_key = data['piano_key']
        velocity = data['velocity']
        color = data['color']
        
        # Update dynamics label
        self.dynamics_label.configure(text=data['dynamics'])
        self.dynamics_label.update()
        
        # Calculate bar coordinates
        x0, y0, x1, y1 = self._calculate_bar_coordinates(piano_key, velocity)
        
        # Create initial bar
        bar_id = self.canvas.create_rectangle(
            x0, config.y0_init, x1, y1,
            fill='grey'
        )
        
        # Store active bar
        self.active_bars[piano_key] = bar_id
        
        # Animate bar height
        self._animate_bar_height(bar_id, x0, x1, y1, y0, color)
    
    def _handle_note_off(self, data: Dict[str, Any]) -> None:
        """Handle note off event and animate bar removal."""
        piano_key = data['piano_key']
        
        if piano_key in self.active_bars:
            bar_id = self.active_bars[piano_key]
            
            # Animate bar removal
            self._animate_bar_removal(bar_id, piano_key)
    
    def _animate_bar_height(self, bar_id: int, x0: float, x1: float, y1: float, target_y: float, color: str) -> None:
        """Animate the bar height from initial to target position."""
        current_y = self.canvas.coords(bar_id)[1]
        
        if current_y > target_y:
            new_y = current_y - 0.2
            self.canvas.coords(bar_id, x0, new_y, x1, y1)
            self.canvas.itemconfig(bar_id, fill=color)
            self.root.after(1, lambda: self._animate_bar_height(bar_id, x0, x1, y1, target_y, color))
    
    def _animate_bar_removal(self, bar_id: int, piano_key: int) -> None:
        """Animate the bar removal by sliding it down."""
        coords = self.canvas.coords(bar_id)
        if len(coords) >= 4:
            x0, current_y, x1, y1 = coords
            
            if current_y < config.y0_init:
                new_y = current_y + 0.02
                self.canvas.coords(bar_id, x0, new_y, x1, y1)
                self.root.after(1, lambda: self._animate_bar_removal(bar_id, piano_key))
            else:
                # Remove the bar
                self.canvas.delete(bar_id)
                del self.active_bars[piano_key]
    
    def _process_midi_messages(self) -> None:
        """Process MIDI messages and update visualization."""
        msg = self.midi_handler.get_message()
        
        if msg:
            message, deltatime = msg
            processed_data = self.midi_handler.process_message(message, deltatime)
            
            if processed_data:
                if processed_data['type'] == 'note_on':
                    self._handle_note_on(processed_data)
                elif processed_data['type'] == 'note_off':
                    self._handle_note_off(processed_data)
        
        # Schedule next processing
        self.root.after(1, self._process_midi_messages)
    
    def run(self) -> None:
        """Start the GUI main loop."""
        self.logger.info("Starting dynamics visualizer")
        self.root.after(1, self._process_midi_messages)
        self.root.mainloop() 