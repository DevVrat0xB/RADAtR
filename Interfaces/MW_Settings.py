"""
Represents a setting window, which takes basic information of the school as input as
well as the basic structure of the fee for different students. This is an independent widget.

the structure of the window is like follow:

             _______________Settings Window__________________
            |                       |                                                |
            |       Nav          |          Stack and Footer            |
            |                       |                                                |
            ___________________________________________________

"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget,  QHBoxLayout
)
from Global.Styles.Colors import *
from Interfaces.DW_Settings_Nav import SettingsNav
from Interfaces.CW_Settings_StackNFooter import SettingsStackNFooter


# represents whole "Settings" window
class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # title of the main window
        window_title = 'Settings'
        self.setWindowTitle(window_title)

        # values are in pixels
        self.windowTopMargin = 30
        self.windowLeftMargin = 50
        self.windowHeight = 660
        self.windowWidth = 1000

        # appearance of the window (changing background as dark)
        self.setAutoFillBackground(True)
        self.mainPalette = self.palette()
        self.mainPalette.setColor(self.backgroundRole(), darcula_background)
        self.setPalette(self.mainPalette)

        # initializing size and the location on screen for the window
        self.setGeometry(self.windowTopMargin, self.windowLeftMargin, self.windowWidth, self.windowHeight)

        # main layout of the widget
        self.mainLayout = QHBoxLayout(self)

        # navigation section widget (to be placed on the left side)
        self.navigationSection = SettingsNav(self)

        # context section widget (to be placed on the right side)
        self.contextSection = SettingsStackNFooter(self)

        # adding above sections (i.e. navigation and context) to the main layout
        self.mainLayout.addWidget(self.navigationSection, 1)
        self.mainLayout.addWidget(self.contextSection, 3)

        self.mainLayout.setContentsMargins(0, 0, 0, 0)         # remove margins
        self.setLayout(self.mainLayout)


def main():
    window = QApplication(sys.argv)
    window.setStyle('Fusion')
    main_app_window = SettingsStackNFooter()
    main_app_window.show()
    sys.exit(window.exec_())


if __name__ == '__main__':
    main()
