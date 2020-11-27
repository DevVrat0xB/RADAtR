"""
A dependent widget which represents settings window footer (placed inside 'Settings' window).
It containing buttons like 'back' and 'next'. This widget will decide which (bare) widget must be
displayed upon the clicks of 'back' and 'next' buttons.

structure of this widget:
         _____________________________________
        |                                                      |
        |                                                      |
        |        All the widgets which are       |
        |         stacked together and            |
        |     controlled by footer section      |
        |               (Stacked Section)             |
         _____________________________________
        |               (Footer Section)              |
         ______________________________________
        
"""
from Interfaces.CW_Settings_Stack import SettingCategories
from Interfaces.DW_Settings_Footer import SettingsFooter
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout
)


# contains 2 components (settings categories widgets and footer widget)
class SettingsStackNFooter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # variable dependencies
        """following references are used to point the respective functions for 'next' and 'back' button,
            which are defined in 'BasicInfoInput' widget. These references are supposed to be passed
            to the 'footer' widget"""
        self.nextButtonFunctionRef = None
        self.backButtonFunctionRef = None

        # main layout of the widget
        self.mainLayout = QVBoxLayout(self)

        self.settingsFooter = SettingsFooter(self)
        # section that will contain all the other widgets
        self.settingCategories = SettingCategories(self, self.settingsFooter)

        # font family, size and color
        self.navTextFont = QFont()
        self.navTextFont.setBold(False)
        self.navTextFont.setPointSize(13)  # in pixels
        self.setFont(self.navTextFont)

        # adding both widget into main layout
        self.mainLayout.addWidget(self.settingCategories, 3)
        self.mainLayout.addWidget(self.settingsFooter)
        self.mainLayout.setContentsMargins(0, 0, 10, 10)
        self.setLayout(self.mainLayout)
