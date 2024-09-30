import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QAction, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QDialog, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

class PasswordDialog(QDialog):
    def __init__(self, correct_password, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correct_password = correct_password
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Enter Password")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter your password")

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_password)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")

        self.keyboard = OnScreenKeyboard(self)

        layout = QVBoxLayout()
        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.error_label)
        layout.addWidget(self.keyboard)
        self.setLayout(layout)

    def check_password(self):
        if self.password_input.text() == self.correct_password:
            self.accept()  # Close dialog and accept input
        else:
            self.error_label.setText("Incorrect password. Try again.")

    def append_char(self, char):
        current_text = self.password_input.text()
        self.password_input.setText(current_text + char)

    def clear_input(self):
        self.password_input.clear()

    def accept_input(self):
        self.check_password()

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Tab Authentication Example")
        self.setGeometry(100, 100, 1280, 800)  # Adjust window size to match display resolution

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.home_tab = QWidget()
        self.tab_widget.addTab(self.home_tab, "Home")
        
        self.config_tab = QWidget()
        self.tab_widget.addTab(self.config_tab, "Configuration")
        self.tab_widget.setTabEnabled(1, False)  # Disable Configuration tab initially

        self.unlock_action = QAction("Unlock Configuration", self)
        self.unlock_action.triggered.connect(self.unlock_configuration_tab)
        self.menuBar().addAction(self.unlock_action)

        self.tab_widget.currentChanged.connect(self.tab_changed)

        # Load and apply the stylesheet
        self.apply_stylesheet('style.qss')

    def apply_stylesheet(self, filepath):
        with open(filepath, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def unlock_configuration_tab(self):
        dialog = PasswordDialog(correct_password="yo")  # Replace with your actual password
        if dialog.exec_() == QDialog.Accepted:
            self.tab_widget.setTabEnabled(1, True)  # Enable Configuration tab
            self.menuBar().removeAction(self.unlock_action)  # Remove unlock action from menu
            QMessageBox.information(self, "Access Granted", "Configuration tab unlocked.")
        else:
            QMessageBox.warning(self, "Access Denied", "Incorrect password.")

    def tab_changed(self, index):
        # Auto-lock Configuration tab when switching away from it
        if index != 1:  # Index 1 is the Configuration tab
            self.tab_widget.setTabEnabled(1, False)
            self.menuBar().addAction(self.unlock_action)  # Re-add unlock action to menu

    def append_char(self, char):
        # Method to handle character addition from the on-screen keyboard
        pass

    def clear_input(self):
        # Method to clear input from the on-screen keyboard
        pass

    def accept_input(self):
        # Method to handle accepting input from the on-screen keyboard
        pass

class OnScreenKeyboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()
        self.setLayout(layout)

        self.is_shifted = False  # Track shift state

        # Define rows of keys with smaller width to fit better on the screen
        self.key_rows = [
            '1234567890',
            'QWERTYUIOP',
            'ASDFGHJKL',
            'ZXCVBNM',
            ' ,.!@#$%^*',
        ]

        # Define shift key for toggling
        self.shift_key = 'Shift'
        
        self.key_buttons = {}
        button_size = QSize(50, 50)  # Smaller button size for better fitting on screen
        
        # Create buttons for each key
        for i, row in enumerate(self.key_rows):
            for j, key in enumerate(row):
                btn = QPushButton(key)
                btn.setFixedSize(button_size)
                btn.clicked.connect(self.handle_key_press)
                layout.addWidget(btn, i, j)
                self.key_buttons[key] = btn

        # Add Shift, Enter, and Clear keys
        shift_btn = QPushButton(self.shift_key)
        shift_btn.setFixedSize(button_size)
        shift_btn.clicked.connect(self.toggle_shift)
        layout.addWidget(shift_btn, len(self.key_rows), 0, 1, 1)  # Place Shift key at the end
        
        enter_btn = QPushButton('Enter')
        enter_btn.setFixedSize(button_size)
        enter_btn.clicked.connect(self.handle_key_press)
        layout.addWidget(enter_btn, len(self.key_rows), 1, 1, 1)  # Place Enter key beside Shift key

        clear_btn = QPushButton('Clear')
        clear_btn.setFixedSize(button_size)
        clear_btn.clicked.connect(self.clear_input)
        layout.addWidget(clear_btn, len(self.key_rows), 2, 1, 1)  # Place Clear key at the end

        # Set a maximum width for the keyboard
        self.setMaximumWidth(1100)  # Adjust this value as needed

    def handle_key_press(self):
        sender = self.sender()
        key = sender.text()

        if key == 'Shift':
            self.toggle_shift()
        elif key == 'Enter':
            self.parent().accept_input()
        elif key == 'Clear':
            self.clear_input()
        else:
            if self.is_shifted and key.isalpha():
                key = key.upper()
            self.parent().append_char(key)

    def toggle_shift(self):
        self.is_shifted = not self.is_shifted
        for key, button in self.key_buttons.items():
            if key.isalpha():
                button.setText(key.upper() if self.is_shifted else key.lower())

    def clear_input(self):
        self.parent().clear_input()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())