"""
Tests for the config module.
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from musical_dynamics.config import Config


class TestConfig:
    """Test the Config class."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = Config()
        
        assert config.window_width == 1300
        assert config.window_height == 624
        assert config.window_title == "Musical Dynamics Trainer"
        assert config.y_gap == 182
        assert config.y_stretch == 3
        assert config.y0_init == 439
        assert config.x_gap == 80
        assert config.x_stretch == 1.25
        assert config.x_width == 11.5
        assert config.background_color == "#161616"
        assert config.text_color == "#efcf83"
        assert config.text_font == "Georgia 20 bold"
        assert config.default_midi_port == "0"
    
    def test_custom_config(self):
        """Test custom configuration values."""
        config = Config(
            window_width=800,
            window_height=600,
            window_title="Custom Title",
            y_gap=100,
            x_gap=50
        )
        
        assert config.window_width == 800
        assert config.window_height == 600
        assert config.window_title == "Custom Title"
        assert config.y_gap == 100
        assert config.x_gap == 50
    
    @patch('musical_dynamics.config.Path')
    def test_piano_image_path_auto_detection(self, mock_path):
        """Test automatic piano image path detection."""
        # Mock the package directory structure
        mock_package_dir = MagicMock()
        mock_package_dir.__truediv__ = MagicMock(return_value=mock_package_dir)
        
        # Mock the first path to exist
        mock_path1 = MagicMock()
        mock_path1.exists.return_value = True
        
        # Mock the second and third paths to not exist
        mock_path2 = MagicMock()
        mock_path2.exists.return_value = False
        mock_path3 = MagicMock()
        mock_path3.exists.return_value = False
        
        # Set up the mock to return different paths
        mock_path.side_effect = lambda x: {
            'img': mock_path1,
            'app': mock_path2,
            'img/piano_3.png': mock_path1,
            'app/img/piano_3.png': mock_path2,
            'img/piano_3.png': mock_path3,
        }.get(str(x), MagicMock())
        
        # Mock the file path
        mock_file_path = MagicMock()
        mock_file_path.parent.parent.parent = mock_package_dir
        
        with patch('musical_dynamics.config.Path') as mock_path_class:
            mock_path_class.return_value = mock_file_path
            
            config = Config()
            
            # Should find the first path
            assert config.piano_image_path == mock_path1
    
    @patch('musical_dynamics.config.Path')
    def test_piano_image_path_not_found(self, mock_path):
        """Test behavior when piano image is not found."""
        # Mock all paths to not exist
        mock_path_instance = MagicMock()
        mock_path_instance.exists.return_value = False
        mock_path.return_value = mock_path_instance
        
        config = Config()
        
        # Should be None when no image is found
        assert config.piano_image_path is None
    
    def test_piano_image_path_provided(self):
        """Test when piano image path is explicitly provided."""
        custom_path = Path("/custom/path/piano.png")
        config = Config(piano_image_path=custom_path)
        
        assert config.piano_image_path == custom_path 