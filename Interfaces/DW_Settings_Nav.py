"""
 A dependent widget (DW) which is supposed to be a component of another widget (i.e Settings widget)
 It contains only the text of different categories or section of settings. (E.g Fee, Basic Info of school etc)
"""
from Global.Styles.Colors import *
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel
)


# represents navigation section inside 'Settings' window
class SettingsNav(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # appearance of the window (changing background as dark)
        self.setAutoFillBackground(True)
        self.navPalette = self.palette()
        self.navPalette.setColor(self.backgroundRole(), pycharm_dark_blue)
        self.navPalette.setColor(self.foregroundRole(), QColor('lightGrey'))
        self.setPalette(self.navPalette)

        # main layout of the widget
        self.mainLayout = QVBoxLayout(self)

        # options entries
        self.basicInfoText = QLabel('Basic Information')
        self.feeStructureText = QLabel('Fee Structure')

        # font family, size and color
        self.navTextFont = QFont()
        self.navTextFont.setBold(False)
        self.navTextFont.setPointSize(13)  # in pixels
        self.setFont(self.navTextFont)

        self.mainLayout.addWidget(self.basicInfoText)
        self.mainLayout.addWidget(self.feeStructureText)
        self.mainLayout.addStretch(1)
        self.mainLayout.setContentsMargins(20, 20, 0, 0)
        self.setLayout(self.mainLayout)
