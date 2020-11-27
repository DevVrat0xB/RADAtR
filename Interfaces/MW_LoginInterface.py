"""
Represent a window (Widget) for inputting all basic information about the school.
This window is meant for admins only and is displayed only after the admin login.
"""
import sys
from Database.database_functions import verify_admin
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout, QHBoxLayout,
    QLineEdit, QLabel, QPushButton
)
from Interfaces.MW_Settings import SettingsWindow
from Global.Styles.Colors import *


# represents whole window
class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # title of the main window
        window_title = 'Window Login'
        self.setWindowTitle(window_title)

        # values are in pixels
        self.windowTopMargin = 100
        self.windowLeftMargin = 300
        self.windowHeight = 100
        self.windowWidth = 300

        # appearance of the window (changing background as dark)
        self.setAutoFillBackground(True)
        self.mainPalette = self.palette()
        self.mainPalette.setColor(self.backgroundRole(), darcula_background)
        self.mainPalette.setColor(self.foregroundRole(), QColor('white'))
        self.setPalette(self.mainPalette)

        # initializing size and the location on screen for the window
        self.setGeometry(self.windowTopMargin, self.windowLeftMargin, self.windowWidth, self.windowHeight)

        # main layout of the widget
        self.mainLayout = QVBoxLayout(self)

        # login form widget
        self.loginForm = QWidget(self)
        self.loginFormLayout = QFormLayout(self.loginForm)
        # login form inputs
        self.usernameField = QLineEdit(self.loginForm)
        self.passwordField = QLineEdit(self.loginForm)
        self.passwordField.setEchoMode(QLineEdit.Password)
        # adding fields into the form layout
        self.loginFormLayout.addRow(QLabel('Username'), self.usernameField)
        self.loginFormLayout.addRow(QLabel('Password'), self.passwordField)

        # buttons area widget
        self.buttonsArea = QWidget(self)
        self.buttonsAreaLayout = QHBoxLayout(self.buttonsArea)
        self.message = 'Login Prompt'
        self.warningPrompt = QLabel(self.message)
        self.warningPrompt.setHidden(True)
        self.loginButton = QPushButton('Login')
        self.loginButton.clicked.connect(self.verify_user)

        self.buttonsAreaLayout.addStretch(1)
        self.buttonsAreaLayout.addWidget(self.warningPrompt, 2)
        self.buttonsAreaLayout.addWidget(self.loginButton)

        # adding above sections (i.e. navigation and context) to the main layout
        self.mainLayout.addWidget(self.loginForm)
        self.mainLayout.addWidget(self.buttonsArea)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)  # remove margins
        self.setLayout(self.mainLayout)

    def verify_user(self):
        username = self.usernameField.text()
        password = self.passwordField.text()

        # verifying administrator name and password from the database
        verified_admin = verify_admin(username, password)
        if verified_admin:
            self.settingsWindow = SettingsWindow()
            self.settingsWindow.show()       # display next window (ie Settings window)
            self.message = ''
            self.warningPrompt.setHidden(True)
            self.setHidden(True)
        else:
            print('Wrong Credentials')
            self.message = 'Wrong Credentials'
            self.warningPrompt.setText(self.message)
            self.warningPrompt.setHidden(False)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    settingsWindow_object = LoginWindow()
    settingsWindow_object.show()
    sys.exit(application.exec_())
