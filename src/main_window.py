from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, 
                             QTextEdit, QMenuBar, QStatusBar)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Windows Network Tool")
        self.setGeometry(100, 100, 800, 600)
        
        self.init_ui()
        self.create_menu_bar()
        self.create_status_bar()
    
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Header
        header_label = QLabel("Windows Network Tool")
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        layout.addWidget(header_label)
        
        # Button layout
        button_layout = QHBoxLayout()
        
        self.scan_button = QPushButton("Scan Network")
        self.connect_button = QPushButton("Connect")
        self.settings_button = QPushButton("Settings")
        
        button_layout.addWidget(self.scan_button)
        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.settings_button)
        
        layout.addLayout(button_layout)
        
        # Output area
        self.output_text = QTextEdit()
        self.output_text.setPlaceholderText("Network information will appear here...")
        layout.addWidget(self.output_text)
        
        central_widget.setLayout(layout)
        
        # Connect signals
        self.scan_button.clicked.connect(self.scan_network)
        self.connect_button.clicked.connect(self.connect_to_device)
        self.settings_button.clicked.connect(self.open_settings)
    
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('File')
        
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Tools menu
        tools_menu = menubar.addMenu('Tools')
        
        scan_action = QAction('Scan Network', self)
        scan_action.triggered.connect(self.scan_network)
        tools_menu.addAction(scan_action)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        
        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def create_status_bar(self):
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")
    
    def scan_network(self):
        self.status_bar.showMessage("Scanning network...")
        self.output_text.append("Starting network scan...")
        # TODO: Implement network scanning functionality
        self.status_bar.showMessage("Scan completed")
    
    def connect_to_device(self):
        self.status_bar.showMessage("Connecting...")
        self.output_text.append("Attempting to connect...")
        # TODO: Implement device connection functionality
        self.status_bar.showMessage("Connection attempt finished")
    
    def open_settings(self):
        self.output_text.append("Opening settings...")
        # TODO: Implement settings dialog
    
    def show_about(self):
        self.output_text.append("Windows Network Tool v1.0\nA PyQt6 application for network management")