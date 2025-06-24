"""
Main entry point for the Musical Dynamics Training Software.
"""

import argparse
import logging
import sys
from pathlib import Path
from .midi_handler import MidiHandler
from .gui import DynamicsVisualizer


def setup_logging(verbose: bool = False) -> None:
    """
    Set up logging configuration.

    Args:
        verbose: Enable verbose logging if True
    """
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


def main() -> None:
    """Main application entry point."""
    parser = argparse.ArgumentParser(
        description="Musical Dynamics Training Software - Visualize your piano dynamics in real-time",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Use default MIDI port
  %(prog)s --port 1          # Use MIDI port 1
  %(prog)s --list-ports      # List available MIDI ports
  %(prog)s --mock-midi       # Use mock MIDI input (no device needed)
  %(prog)s --verbose         # Enable verbose logging
        """
    )

    parser.add_argument(
        "--port",
        default="0",
        help="MIDI port number or name (default: 0)"
    )

    parser.add_argument(
        "--list-ports",
        action="store_true",
        help="List available MIDI ports and exit"
    )

    parser.add_argument(
        "--mock-midi",
        action="store_true",
        help="Use a mock MIDI handler for testing without a device"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )

    args = parser.parse_args()

    # Set up logging
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)

    try:
        # List ports if requested
        if args.list_ports:
            from rtmidi.midiutil import list_ports
            print("Available MIDI input ports:")
            ports = list_ports()
            for i, port in enumerate(ports):
                print(f"  {i}: {port}")
            return

        logger.info("Starting Musical Dynamics Training Software")

        # Initialize MIDI handler (mock or real)
        if args.mock_midi:
            from .mock_midi_handler import MockMidiHandler
            logger.info("Using mock MIDI handler (no device needed)")
            midi_handler = MockMidiHandler()
        else:
            logger.info(f"Connecting to MIDI port: {args.port}")
            midi_handler = MidiHandler(args.port)

        # Create and run GUI
        visualizer = DynamicsVisualizer(midi_handler)
        visualizer.run()

    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Application error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()