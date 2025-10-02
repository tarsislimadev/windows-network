# Windows Network Management Application

A PyQt6-based graphical application for Windows network management and device connectivity.

## Features

- Network scanning capabilities
- Device connection management
- User-friendly GUI interface
- Settings configuration

## Requirements

- Python 3.8 or higher
- Windows operating system
- PyQt6 framework

## Installation

### Quick Setup

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Alternative Installation (Windows)

If you encounter build tool issues, use pre-built wheels:
```bash
pip install PyQt6 --only-binary=all
```

### Development Installation

For development purposes:
```bash
pip install -e .
```

## Usage

### Running the Application

```bash
# Run directly
python main.py

# Or run as installed package
windows-network
```

## Project Structure

```
windows-network/
├── main.py              # Application entry point
├── src/                 # Source code directory
│   ├── __init__.py
│   └── main_window.py   # Main application window
├── requirements.txt     # Python dependencies
├── setup.py            # Package setup configuration
└── README.md           # This file
```

## Application Overview

The application provides a clean, intuitive interface with:

- **Menu Bar**: File, Tools, and Help menus for navigation
- **Action Buttons**: Quick access to network scanning and device connection
- **Output Area**: Display results and status information
- **Status Bar**: Real-time feedback and notifications

## Development

The application follows PyQt6 best practices with:

- Modular architecture in the `src/` directory
- Signal/slot pattern for UI interactions
- Extensible design for additional features

## License

See LICENSE file for details.

## Contributing

This project is structured for easy extension. Key areas for development:

- Network scanning implementation
- Device connection protocols
- Settings and configuration options
- Additional UI components
