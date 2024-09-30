import sys
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout, QDialog, 
                             QAction, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
                             QGridLayout, QFrame, QStatusBar, QTabWidget, QStackedWidget, QMessageBox, 
                             QComboBox, QGridLayout)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QPalette
import pyqtgraph as pg

import random
import numpy as np
from scipy.signal import find_peaks
from auth import PasswordDialog, OnScreenKeyboard

class ClickableFrame(QFrame):
    # Custom signal to be emitted when the frame is clicked
    clicked = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.Box)
        self.setStyleSheet("background-color: #1B3B5F; border-radius: 10px;")  # Dark Slate Blue Tile

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
            event.accept()


class IncubatorUI(QWidget):
    def __init__(self):
        super().__init__()

        self.password = "1bI"
        
        # Temperture
        self.current_very_low_temp = 0.0  # Default value
        self.current_low_temp = 10.0      # Default value
        self.current_normal_temp = 20.0   # Default value
        self.current_high_temp = 30.0     # Default value
        self.current_very_high_temp = 40.0 # Default value
        
        # Pulse rate
        self.current_very_low_pulse = 0.0  # Default value
        self.current_low_pulse = 10.0      # Default value
        self.current_normal_pulse = 20.0   # Default value
        self.current_high_pulse = 30.0     # Default value
        self.current_very_high_pulse = 40.0 # Default value

        # SpO2
        self.current_very_low_SpO2 = 0.0  # Default value
        self.current_low_SpO2 = 10.0      # Default value
        self.current_normal_SpO2 = 20.0   # Default value
        self.current_high_SpO2 = 30.0     # Default value
        self.current_very_high_SpO2 = 40.0 # Default value

        # Set window properties
        self.setWindowTitle("Infant Incubator Monitor")
        self.setGeometry(100, 100, 1980, 1080)

        # Set dark blue theme
        self.set_dark_blue_theme()

        # Fonts for consistency
        self.title_font = QFont('Arial', 24, QFont.Bold)
        self.label_font = QFont('Arial', 18)
        self.data_font = QFont('Arial', 22, QFont.Bold)

        # Tabs for navigation
        self.tab_widget = QTabWidget()

        # Initialize tabs
        self.init_dashboard()
        self.init_configuration()
        self.init_history()

        # Load settings from the text file, if available
        self.load_settings()  

        self.tab_widget.setTabEnabled(1, False)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tab_widget)

        # Status Bar
        self.init_status_bar()
        main_layout.addWidget(self.status_bar)

        self.add_reset_button(self.ecg_plot)

        self.setLayout(main_layout)

        # Simulate live updates using QTimer
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_readings)
        self.update_timer.start(1000)  # Update every second

        # Timer to update history periodically
        self.history_update_timer = QTimer(self)
        self.history_update_timer.timeout.connect(self.update_history_plot)  # Update history regularly
        self.history_update_timer.start(2000)  # Update every 2 seconds

        # Historical data storage
        self.history_data = {
            'Ambient Temp': [],
            'Bed Temp': [],
            'Infant Temp': [],
            'Pulse Rate': [],
            'SpO2': [],
            'ECG': [],
            'Ambient Humidity': []
        }

    def set_dark_blue_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(10, 25, 48))  # Dark Blue Background
        palette.setColor(QPalette.WindowText, QColor(220, 220, 255))  # Light Blue-White Text
        palette.setColor(QPalette.Base, QColor(25, 50, 75))  # Tile Background (slate blue)
        palette.setColor(QPalette.AlternateBase, QColor(30, 60, 90))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, QColor(220, 220, 255))  # Light Blue Text
        palette.setColor(QPalette.Button, QColor(20, 45, 70))  # Button Background
        palette.setColor(QPalette.ButtonText, QColor(240, 240, 255))  # Button Text
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Highlight, QColor(100, 120, 200))  # Highlight color
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)

    def init_dashboard(self):
        dashboard_widget = QWidget()
        dashboard_layout = QVBoxLayout()

        # Main Section (Temperature, Vital Signs, Humidity)
        self.init_main_section()
        dashboard_layout.addLayout(self.main_grid)

        # Add Reset Button and Unlock Access Button beside each other
        button_layout = QHBoxLayout()

        # Unlock Access Button
        unlock_button = QPushButton("Unlock Access", self)
        unlock_button.clicked.connect(self.unlock_configuration_tab)
        button_layout.addWidget(unlock_button)

        # Connect tab change event
        self.tab_widget.currentChanged.connect(self.tab_changed)

        dashboard_layout.addLayout(button_layout)

        # Add Dashboard content
        dashboard_widget.setLayout(dashboard_layout)
        self.tab_widget.addTab(dashboard_widget, "Dashboard")

    def init_configuration(self):
        config_widget = QWidget()
        config_layout = QVBoxLayout()

        # Configuration Title
        config_title = QLabel("Configuration Settings")
        config_title.setFont(QFont('Arial', 24, QFont.Bold))
        config_title.setStyleSheet("color: #FFFFFF; margin-bottom: 20px;")
        config_layout.addWidget(config_title, alignment=Qt.AlignCenter)

        # Parameter Range Configuration (Temperature Example)
        temperature_range_layout = QFormLayout()

        temperature_range_title = QLabel("Temperature Ranges")
        temperature_range_title.setFont(QFont('Arial', 18, QFont.Bold))
        temperature_range_layout.addRow(temperature_range_title)

        self.very_low_temp_spinbox = QDoubleSpinBox()
        self.very_low_temp_spinbox.setRange(-273.15, 1000.0)
        self.very_low_temp_spinbox.setDecimals(2)
        self.very_low_temp_spinbox.setValue(self.current_very_low_temp)
        temperature_range_layout.addRow(QLabel("Very Low Temperature Threshold:"), self.very_low_temp_spinbox)

        self.low_temp_spinbox = QDoubleSpinBox()
        self.low_temp_spinbox.setRange(-273.15, 1000.0)
        self.low_temp_spinbox.setDecimals(2)
        self.low_temp_spinbox.setValue(self.current_low_temp)
        temperature_range_layout.addRow(QLabel("Low Temperature Threshold:"), self.low_temp_spinbox)

        self.normal_temp_spinbox = QDoubleSpinBox()
        self.normal_temp_spinbox.setRange(-273.15, 1000.0)
        self.normal_temp_spinbox.setDecimals(2)
        self.normal_temp_spinbox.setValue(self.current_normal_temp)
        temperature_range_layout.addRow(QLabel("Normal Temperature Threshold:"), self.normal_temp_spinbox)

        self.high_temp_spinbox = QDoubleSpinBox()
        self.high_temp_spinbox.setRange(-273.15, 1000.0)
        self.high_temp_spinbox.setDecimals(2)
        self.high_temp_spinbox.setValue(self.current_high_temp)
        temperature_range_layout.addRow(QLabel("High Temperature Threshold:"), self.high_temp_spinbox)

        self.very_high_temp_spinbox = QDoubleSpinBox()
        self.very_high_temp_spinbox.setRange(-273.15, 1000.0)
        self.very_high_temp_spinbox.setDecimals(2)
        self.very_high_temp_spinbox.setValue(self.current_very_high_temp)
        temperature_range_layout.addRow(QLabel("Very High Temperature Threshold:"), self.very_high_temp_spinbox)

        config_layout.addLayout(temperature_range_layout)

        # Pulse rate parameters
        pulse_range_layout = QFormLayout()

        pulse_range_title = QLabel("Pulse Rate Ranges")
        pulse_range_title.setFont(QFont('Arial', 18, QFont.Bold))
        pulse_range_layout.addRow(pulse_range_title)

        self.very_low_pulse_spinbox = QDoubleSpinBox()
        self.very_low_pulse_spinbox.setRange(-273.15, 1000.0)
        self.very_low_pulse_spinbox.setDecimals(2)
        self.very_low_pulse_spinbox.setValue(self.current_very_low_pulse)
        pulse_range_layout.addRow(QLabel("Very Low Pulse Threshold:"), self.very_low_pulse_spinbox)

        self.low_pulse_spinbox = QDoubleSpinBox()
        self.low_pulse_spinbox.setRange(-273.15, 1000.0)
        self.low_pulse_spinbox.setDecimals(2)
        self.low_pulse_spinbox.setValue(self.current_low_pulse)
        pulse_range_layout.addRow(QLabel("Low Pulse Threshold:"), self.low_pulse_spinbox)

        self.normal_pulse_spinbox = QDoubleSpinBox()
        self.normal_pulse_spinbox.setRange(-273.15, 1000.0)
        self.normal_pulse_spinbox.setDecimals(2)
        self.normal_pulse_spinbox.setValue(self.current_normal_pulse)
        pulse_range_layout.addRow(QLabel("Normal Pulse Threshold:"), self.normal_pulse_spinbox)

        self.high_pulse_spinbox = QDoubleSpinBox()
        self.high_pulse_spinbox.setRange(-273.15, 1000.0)
        self.high_pulse_spinbox.setDecimals(2)
        self.high_pulse_spinbox.setValue(self.current_high_pulse)
        pulse_range_layout.addRow(QLabel("High Pulse Threshold:"), self.high_pulse_spinbox)

        self.very_high_pulse_spinbox = QDoubleSpinBox()
        self.very_high_pulse_spinbox.setRange(-273.15, 1000.0)
        self.very_high_pulse_spinbox.setDecimals(2)
        self.very_high_pulse_spinbox.setValue(self.current_very_high_pulse)
        pulse_range_layout.addRow(QLabel("Very High Pulse Threshold:"), self.very_high_pulse_spinbox)

        config_layout.addLayout(pulse_range_layout)

        # SpO2 parameters
        SpO2_range_layout = QFormLayout()

        SpO2_range_title = QLabel("SpO2 Ranges")
        SpO2_range_title.setFont(QFont('Arial', 18, QFont.Bold))
        SpO2_range_layout.addRow(SpO2_range_title)

        self.very_low_SpO2_spinbox = QDoubleSpinBox()
        self.very_low_SpO2_spinbox.setRange(-273.15, 1000.0)
        self.very_low_SpO2_spinbox.setDecimals(2)
        self.very_low_SpO2_spinbox.setValue(self.current_very_low_SpO2)
        SpO2_range_layout.addRow(QLabel("Very Low SpO2 Threshold:"), self.very_low_SpO2_spinbox)

        self.low_SpO2_spinbox = QDoubleSpinBox()
        self.low_SpO2_spinbox.setRange(-273.15, 1000.0)
        self.low_SpO2_spinbox.setDecimals(2)
        self.low_SpO2_spinbox.setValue(self.current_low_SpO2)
        SpO2_range_layout.addRow(QLabel("Low SpO2 Threshold:"), self.low_SpO2_spinbox)

        self.normal_SpO2_spinbox = QDoubleSpinBox()
        self.normal_SpO2_spinbox.setRange(-273.15, 1000.0)
        self.normal_SpO2_spinbox.setDecimals(2)
        self.normal_SpO2_spinbox.setValue(self.current_normal_SpO2)
        SpO2_range_layout.addRow(QLabel("Normal SpO2 Threshold:"), self.normal_SpO2_spinbox)

        self.high_SpO2_spinbox = QDoubleSpinBox()
        self.high_SpO2_spinbox.setRange(-273.15, 1000.0)
        self.high_SpO2_spinbox.setDecimals(2)
        self.high_SpO2_spinbox.setValue(self.current_high_SpO2)
        SpO2_range_layout.addRow(QLabel("High SpO2 Threshold:"), self.high_SpO2_spinbox)

        self.very_high_SpO2_spinbox = QDoubleSpinBox()
        self.very_high_SpO2_spinbox.setRange(-273.15, 1000.0)
        self.very_high_SpO2_spinbox.setDecimals(2)
        self.very_high_SpO2_spinbox.setValue(self.current_very_high_SpO2)
        SpO2_range_layout.addRow(QLabel("Very High SpO2 Threshold:"), self.very_high_SpO2_spinbox)

        config_layout.addLayout(SpO2_range_layout)

        # Alert Configuration
        alert_layout = QFormLayout()

        alert_title = QLabel("Alert Configuration")
        alert_title.setFont(QFont('Arial', 18, QFont.Bold))
        alert_layout.addRow(alert_title)

        self.temp_alert_checkbox = QCheckBox("Enable Temperature Alerts")
        self.humidity_alert_checkbox = QCheckBox("Enable Humidity Alerts")
        alert_layout.addRow(self.temp_alert_checkbox)
        alert_layout.addRow(self.humidity_alert_checkbox)

        config_layout.addLayout(alert_layout)

        # Apply/Save Button
        apply_button = QPushButton("Apply Settings")
        apply_button.clicked.connect(self.save_settings)
        apply_button.setCursor(Qt.PointingHandCursor)
        config_layout.addWidget(apply_button, alignment=Qt.AlignCenter)

        config_widget.setLayout(config_layout)
        self.tab_widget.addTab(config_widget, "Configuration")
    
    def save_settings(self):
        config_data = {
            "temperature": {
                "very_low": self.very_low_temp_spinbox.value(),
                "low": self.low_temp_spinbox.value(),
                "normal": self.normal_temp_spinbox.value(),
                "high": self.high_temp_spinbox.value(),
                "very_high": self.very_high_temp_spinbox.value()
            },
            "pulse": {
                "very_low": self.very_low_pulse_spinbox.value(),
                "low": self.low_pulse_spinbox.value(),
                "normal": self.normal_pulse_spinbox.value(),
                "high": self.high_pulse_spinbox.value(),
                "very_high": self.very_high_pulse_spinbox.value()
            },
            "SpO2": {
                "very_low": self.very_low_SpO2_spinbox.value(),
                "low": self.low_SpO2_spinbox.value(),
                "normal": self.normal_SpO2_spinbox.value(),
                "high": self.high_SpO2_spinbox.value(),
                "very_high": self.very_high_SpO2_spinbox.value()
            }
        }

        with open("incubator_settings.txt", "w") as file:
            for main_key, sub_data in config_data.items():
                file.write(f"[{main_key}]\n")  # Main category (e.g., temperature)
                for key, value in sub_data.items():
                    file.write(f"{key}={value}\n")
        print("Settings saved successfully.")

    def load_settings(self):
        try:
            with open("incubator_settings.txt", "r") as file:
                lines = file.readlines()
                current_category = None  # To track which parameter we are in (e.g., temperature, pulse)
                for line in lines:
                    line = line.strip()
                    if line.startswith("[") and line.endswith("]"):
                        current_category = line[1:-1]  # Extract the category (e.g., temperature)
                    else:
                        key, value = line.split("=")
                        value = float(value)  # Convert the string to a float

                        # Set values for temperature parameters
                        if current_category == "temperature":
                            if key == "very_low":
                                self.current_very_low_temp = value
                            elif key == "low":
                                self.current_low_temp = value
                            elif key == "normal":
                                self.current_normal_temp = value
                            elif key == "high":
                                self.current_high_temp = value
                            elif key == "very_high":
                                self.current_very_high_temp = value

                        # Set values for pulse parameters
                        elif current_category == "pulse":
                            if key == "very_low":
                                self.current_very_low_pulse = value
                            elif key == "low":
                                self.current_low_pulse = value
                            elif key == "normal":
                                self.current_normal_pulse = value
                            elif key == "high":
                                self.current_high_pulse = value
                            elif key == "very_high":
                                self.current_very_high_pulse = value

                        # Set values for SpO2 parameters
                        elif current_category == "SpO2":
                            if key == "very_low":
                                self.current_very_low_SpO2 = value
                            elif key == "low":
                                self.current_low_SpO2 = value
                            elif key == "normal":
                                self.current_normal_SpO2 = value
                            elif key == "high":
                                self.current_high_SpO2 = value
                            elif key == "very_high":
                                self.current_very_high_SpO2 = value

                # Update UI spinboxes with the loaded values
                self.very_low_temp_spinbox.setValue(self.current_very_low_temp)
                self.low_temp_spinbox.setValue(self.current_low_temp)
                self.normal_temp_spinbox.setValue(self.current_normal_temp)
                self.high_temp_spinbox.setValue(self.current_high_temp)
                self.very_high_temp_spinbox.setValue(self.current_very_high_temp)

                self.very_low_pulse_spinbox.setValue(self.current_very_low_pulse)
                self.low_pulse_spinbox.setValue(self.current_low_pulse)
                self.normal_pulse_spinbox.setValue(self.current_normal_pulse)
                self.high_pulse_spinbox.setValue(self.current_high_pulse)
                self.very_high_pulse_spinbox.setValue(self.current_very_high_pulse)

                self.very_low_SpO2_spinbox.setValue(self.current_very_low_SpO2)
                self.low_SpO2_spinbox.setValue(self.current_low_SpO2)
                self.normal_SpO2_spinbox.setValue(self.current_normal_SpO2)
                self.high_SpO2_spinbox.setValue(self.current_high_SpO2)
                self.very_high_SpO2_spinbox.setValue(self.current_very_high_SpO2)

            print("Settings loaded successfully.")
        except FileNotFoundError:
            print("Settings file not found. Using default values.")


    def unlock_configuration_tab(self):
        # Create and show password dialog
        dialog = PasswordDialog(correct_password=self.password)
        if dialog.exec_() == QDialog.Accepted:
            self.tab_widget.setTabEnabled(1, True)  # Enable Configuration tab
            QMessageBox.information(self, "Access Granted", "Restricted Tabs unlocked!")
        else:
            QMessageBox.warning(self, "Access Denied", "Incorrect password.")

    def tab_changed(self, index):
        # Auto-lock Configuration tab when switching away from it
        if index != 1:  # Index 1 is the Configuration tab
            self.tab_widget.setTabEnabled(1, False)

    def init_history(self):
        history_widget = QWidget()
        history_layout = QVBoxLayout()

        # Dropdown to select which parameter's history to view
        self.history_dropdown = QComboBox()
        self.history_dropdown.addItems(['Ambient Temp', 'Bed Temp', 'Infant Temp', 'Pulse Rate', 'SpO2', 'ECG', 'Ambient Humidity'])
        self.history_dropdown.currentIndexChanged.connect(self.update_history_plot)
        history_layout.addWidget(self.history_dropdown)

        # Timeframe selection
        self.timeframe_dropdown = QComboBox()
        self.timeframe_dropdown.addItems(['Last 1 Hour', 'Last 6 Hours', 'Last 12 Hours', 'Last 24 Hours'])
        self.timeframe_dropdown.currentIndexChanged.connect(self.update_history_plot)
        history_layout.addWidget(self.timeframe_dropdown)

        # Historical data plot
        self.history_plot = pg.PlotWidget()
        self.history_plot.setBackground('#1B3B5F')  # Dark Slate Blue
        self.history_plot.setTitle(f"Historical Data", color='w', size='12pt')
        self.history_plot.setLabel('left', 'Value')
        self.history_plot.setLabel('bottom', 'Time')
        
        history_layout.addWidget(self.history_plot)

        # Reset Button
        self.reset_history_button = QPushButton("Reset History View", self)
        self.reset_history_button.clicked.connect(lambda: self.reset_plot_view(self.history_plot))
        history_layout.addWidget(self.reset_history_button, alignment=Qt.AlignRight)

        history_widget.setLayout(history_layout)
        self.tab_widget.addTab(history_widget, "History")

    def create_data_tile(self, label_text, data_text, unit):
        #frame = QFrame()
        frame = ClickableFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet("background-color: #1B3B5F; border-radius: 10px;")  # Dark Slate Blue Tile

        label = QLabel(label_text)
        label.setFont(self.label_font)
        label.setStyleSheet("color: #DCE4FF;")  # Light Blue Text

        data_label = QLabel(f"{data_text} {unit}")
        data_label.setFont(self.data_font)
        data_label.setStyleSheet("color: #66FFFF;")  # Cyan Data Text

        status_label = QLabel("Normal")
        status_label.setFont(self.label_font)
        status_label.setStyleSheet("color: #66FFFF;")  # Default color (Normal)

        vbox = QVBoxLayout()
        vbox.addWidget(label, alignment=Qt.AlignCenter)
        vbox.addWidget(data_label, alignment=Qt.AlignCenter)
        vbox.addWidget(status_label, alignment=Qt.AlignCenter)
        frame.setLayout(vbox)

        return frame, data_label, status_label

    def go_to_history(self, parameter_name):
        # Assuming the History tab is the second tab (index 1)
        index = 2
        self.tab_widget.setCurrentIndex(index)
        self.history_dropdown.setCurrentText(parameter_name)
        self.history_plot.setTitle(f"Historical Data of {parameter_name}", color='w', size='12pt')
        self.update_history_plot()

    def update_status(self, data_label, status_label, value, ranges):
        data_label.setText(f"{value:.2f} {data_label.text().split()[-1]}")  # Retain the unit from the original text
        status = "Normal"
        color = "#66FFFF"  # Default color

        for range_name, (low, high) in ranges.items():
            if low <= value < high:
                status = range_name
                color = self.get_color_for_status(range_name)
                break

        status_label.setText(status)
        status_label.setStyleSheet(f"color: {color};")


    def init_main_section(self):
        self.main_grid = QGridLayout()

        # Temperature Readings
        self.ambient_temp_tile, self.ambient_temp_label, self.ambient_temp_status = self.create_data_tile("Ambient Temp", "00", "°C")
        self.bed_temp_tile, self.bed_temp_label, self.bed_temp_status = self.create_data_tile("Bed Temp", "00", "°C")
        self.infant_temp_tile, self.infant_temp_label, self.infant_temp_status = self.create_data_tile("Infant Temp", "00", "°C")

        # Vital Signs
        self.pulse_rate_tile, self.pulse_rate_label, self.pulse_rate_status = self.create_data_tile("Pulse Rate", "00", "bpm")
        self.spo2_tile, self.spo2_label, self.spo2_status = self.create_data_tile("SpO2", "00", "%")

        # ECG Graph Display using pyqtgraph
        self.ecg_plot = pg.PlotWidget()
        self.ecg_plot.setBackground('#1B3B5F')  # Dark Slate Blue
        self.ecg_plot.setYRange(-1, 1)
        self.ecg_plot.setTitle("ECG Waveform", color='w', size='12pt')
        self.ecg_plot.getPlotItem().hideAxis('bottom')

        # Humidity
        self.humidity_tile, self.humidity_label, self.humidity_status = self.create_data_tile("Ambient Humidity", "00", "%")

        # history navigation on tiles clicked
        # Connect signals for tiles
        self.ambient_temp_tile.clicked.connect(lambda: self.go_to_history('Ambient Temp'))
        self.bed_temp_tile.clicked.connect(lambda: self.go_to_history('Bed Temp'))
        self.infant_temp_tile.clicked.connect(lambda: self.go_to_history('Infant Temp'))
        self.pulse_rate_tile.clicked.connect(lambda: self.go_to_history('Pulse Rate'))
        self.spo2_tile.clicked.connect(lambda: self.go_to_history('SpO2'))
        self.humidity_tile.clicked.connect(lambda: self.go_to_history('Ambient Humidity'))

        # Organize items in grid layout
        self.main_grid.addWidget(self.ambient_temp_tile, 0, 0)
        self.main_grid.addWidget(self.bed_temp_tile, 1, 0)
        self.main_grid.addWidget(self.infant_temp_tile, 2, 0)
        self.main_grid.addWidget(self.pulse_rate_tile, 0, 1)
        self.main_grid.addWidget(self.spo2_tile, 1, 1)
        self.main_grid.addWidget(self.ecg_plot, 2, 1)
        self.main_grid.addWidget(self.humidity_tile, 3, 0, 1, 2)

    def init_status_bar(self):
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("System Status: All systems operational")

    def update_sensor_data(self):
        # Random data for demonstration purposes
        data = {
            'ambient_temp': random.uniform(18.0, 26.0),
            'bed_temp': random.uniform(18.0, 26.0),
            'infant_temp': random.uniform(36.0, 38.0),
            'pulse_rate': random.randint(60, 120),
            'spo2': random.randint(95, 100),
            'humidity': random.uniform(30.0, 70.0)
        }

        # Update temperature labels and status
        self.update_status(self.ambient_temp_label, self.ambient_temp_status, data['ambient_temp'], 
                           { "Very Low": (18.0, 19.0), "Low": (19.0, 20.0), "Normal": (20.0, 24.0), "High": (24.0, 25.0), "Very High": (25.0, 26.0) })
        self.update_status(self.bed_temp_label, self.bed_temp_status, data['bed_temp'], 
                           { "Very Low": (18.0, 19.0), "Low": (19.0, 20.0), "Normal": (20.0, 24.0), "High": (24.0, 25.0), "Very High": (25.0, 26.0) })
        self.update_status(self.infant_temp_label, self.infant_temp_status, data['infant_temp'], 
                           { "Very Low": (35.0, 36.0), "Low": (36.0, 37.0), "Normal": (37.0, 38.0), "High": (38.0, 39.0), "Very High": (39.0, 40.0) })

        # Update pulse rate and SpO2
        self.update_status(self.pulse_rate_label, self.pulse_rate_status, data['pulse_rate'], 
                           { "Very Low": (60, 70), "Low": (70, 80), "Normal": (80, 100), "High": (100, 110), "Very High": (110, 120) })
        self.update_status(self.spo2_label, self.spo2_status, data['spo2'], 
                           { "Very Low": (95, 96), "Low": (96, 97), "Normal": (97, 99), "High": (99, 100), "Very High": (100, 101) })

        # Update humidity
        self.update_status(self.humidity_label, self.humidity_status, data['humidity'], 
                           { "Very Low": (30.0, 40.0), "Low": (40.0, 50.0), "Normal": (50.0, 60.0), "High": (60.0, 65.0), "Very High": (65.0, 70.0) })

        # Update ECG Plot
        self.update_ecg_plot()

        # Store data in history
        self.store_data_in_history(data)

    def get_color_for_status(self, status):
        colors = {
            "Very Low": "#FF6666",    # Red
            "Low": "#FFCC66",        # Light Orange
            "Normal": "#66FFFF",     # Cyan
            "High": "#FFCC66",       # Light Orange
            "Very High": "#FF6666"   # Red
        }
        return colors.get(status, "#66FFFF")

    def update_ecg_plot(self):
        # Generate random ECG data
        x = np.linspace(0, 1, 1000)
        y = np.sin(2 * np.pi * 5 * x) + 0.5 * np.random.normal(size=x.shape)

        # Update ECG plot
        self.ecg_plot.plot(x, y, pen=pg.mkPen(color='c', width=1.5))

    def store_data_in_history(self, data):
        # Append data to history
        self.history_data['Ambient Temp'].append(data['ambient_temp'])
        self.history_data['Bed Temp'].append(data['bed_temp'])
        self.history_data['Infant Temp'].append(data['infant_temp'])
        self.history_data['Pulse Rate'].append(data['pulse_rate'])
        self.history_data['SpO2'].append(data['spo2'])
        self.history_data['Ambient Humidity'].append(data['humidity'])

    def update_history_plot(self):
        # Clear existing plot
        self.history_plot.clear()

        # Get selected parameter and timeframe
        parameter = self.history_dropdown.currentText()
        timeframe = self.timeframe_dropdown.currentText()

        self.history_plot.setTitle(f"Historical Data of {parameter}", color='w', size='12pt')

        # Simulate data based on the selected parameter
        if parameter not in self.history_data:
            return

        x = np.arange(len(self.history_data[parameter]))
        y = self.history_data[parameter]

        # Update plot with new data
        self.history_plot.plot(x, y, pen=pg.mkPen(color='c', width=2))
        self.history_plot.setLabel('left', parameter)
        self.history_plot.setLabel('bottom', 'Time')

    def reset_plot_view(self, plot_widget):
        plot_widget.enableAutoRange()

    def add_reset_button(self, plot_widget):
        reset_button = QPushButton("Reset Plot View", self)
        reset_button.clicked.connect(lambda: self.reset_plot_view(plot_widget))
        self.main_grid.addWidget(reset_button, 3, 1, 1, 1, alignment=Qt.AlignRight)

    def update_readings(self):
        self.update_sensor_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IncubatorUI()
    window.show()
    sys.exit(app.exec_())