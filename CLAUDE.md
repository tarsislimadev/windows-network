# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a PyQt6-based Windows network management application. The project uses a standard Python package structure with PyQt6 for the GUI framework.

## Development Commands

### Installation and Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Alternative installation if build tools are missing (Windows)
pip install PyQt6 --only-binary=all

# Development installation
pip install -e .
```

### Running the Application
```bash
# Run the main application
python main.py

# Run as installed package
windows-network
```

## Architecture

### Application Structure
- **Entry Point**: `main.py` - Creates QApplication and shows MainWindow
- **Main Window**: `src/main_window.py` - Contains the primary application window with menu bar, buttons, and output area
- **Package Structure**: Source code organized in `src/` directory with proper `__init__.py`

### UI Architecture
The application follows a standard PyQt6 pattern:
- `MainWindow` inherits from `QMainWindow`
- Central widget uses `QVBoxLayout` with header, button row, and text output area
- Menu system with File, Tools, and Help menus
- Status bar for user feedback
- Signal/slot connections for button interactions

### Key Components
- **MainWindow.init_ui()**: Sets up the main layout with header label, button layout, and output text area
- **MainWindow.create_menu_bar()**: Creates application menus
- **Button handlers**: `scan_network()`, `connect_to_device()`, `open_settings()` - currently contain placeholder implementations

### Extension Points
The application is structured for extension with:
- Network scanning functionality (placeholder in `scan_network()`)
- Device connection capabilities (placeholder in `connect_to_device()`)
- Settings dialog (placeholder in `open_settings()`)
- Additional UI components can be added to `src/` directory

## Dependencies

- **PyQt6**: Main GUI framework (>=6.6.1)
- **Python**: 3.8+ required

Note: PyQt6 installation on Windows may require pre-built wheels due to Visual C++ build tool requirements.