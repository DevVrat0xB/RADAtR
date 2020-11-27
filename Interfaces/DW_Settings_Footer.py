"""
Dependent widget which contains 'back' and 'next' buttons to show different setting categories.
This is a component of "Settings" and must be placed inside it only.
"""
from Global.Styles.Colors import *
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QPushButton, QLabel
)


# represents footer section inside 'Settings' window
class SettingsFooter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # variable dependencies
        self.currentScreenIndex = 0
        self.warningMessage = "Test Message"

        # main layout of the widget
        self.mainLayout = QHBoxLayout(self)

        # this widget contains 3 parts in the order (prompts, back button, next button)
        self.promptArea = QWidget(self)
        self.promptAreaLayout = QHBoxLayout(self.promptArea)
        self.promptText = QLabel(self.warningMessage, self.promptArea)
        self.promptAreaLayout.addWidget(self.promptText)
        self.backButton = QPushButton('< Back')
        self.nextButton = QPushButton('Next >')
        self.nextButton.setEnabled(False)

        # font family, size and color
        self.navTextFont = QFont()
        self.navTextFont.setBold(False)
        self.navTextFont.setPointSize(13)  # in pixels
        self.setFont(self.navTextFont)

        # adding both widget into main layout
        self.mainLayout.addWidget(self.promptArea, 2)
        self.mainLayout.addWidget(self.backButton)
        self.mainLayout.addWidget(self.nextButton)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)

    # function which displays a warning message inside prompt area
    def show_warning(self, warning):
        self.warningMessage = warning
        self.promptText.setText(self.warningMessage)
        self.promptText.setHidden(False)
        self.promptText.setStyleSheet(
            "color: orange; "
            "font-weight: bold;"
            )

    # function which displays a warning message inside prompt area
    def hide_warning(self):
        self.warningMessage = ""
        self.promptText.setHidden(True)
