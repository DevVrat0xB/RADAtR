"""
Dependent widget which will contain (bare) widgets for different setting categories.
This is a component of "Settings_StackNFooter" and must be placed inside it only.
"""
from Interfaces.W_SchoolInfoForm import SchoolInfoForm
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QStackedWidget
)


# represents all setting categories, placed inside 'Settings_StackNFooter' widget
class SettingCategories(QWidget):
    def __init__(self, parent=None, footer_ref=None):
        super().__init__(parent)

        # main layout of the widget
        self.mainLayout = QVBoxLayout(self)
        # self.setStyleSheet('border: 1px solid white;')

        # container for all the other widgets which are to be stacked
        self.widgetStackContainer = QStackedWidget(self)

        # instantiating all the required widgets
        self.schoolInfoForm = SchoolInfoForm(self, footer_ref)

        # stacking widgets
        self.widgetStackContainer.addWidget(self.schoolInfoForm)
        self.widgetStackContainer.setCurrentIndex(0)

        # font family, size and color
        self.navTextFont = QFont()
        self.navTextFont.setBold(False)
        self.navTextFont.setPointSize(13)  # in pixels
        self.setFont(self.navTextFont)

        # adding both widget into main layout
        self.mainLayout.addWidget(self.widgetStackContainer)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)
