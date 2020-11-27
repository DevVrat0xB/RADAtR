import sys
from testFile2 import *
from PyQt5.QtWidgets import (
    QWidget, QMainWindow, QApplication,
    QVBoxLayout, QAction
)


class MainWidget(QMainWindow):
    def __init__(self, base=None):
        super(MainWidget, self).__init__(base)

        # configuring geometry of the application
        screen_resolution = get_screen_resolution()
        widget_geometries = generate_widget_geometry_based_on(screen_resolution)
        self.setGeometry(*widget_geometries)

        # experimental UI component
        self.bar = self.menuBar()

        # menu bar options
        self.appOption = self.bar.addMenu("Application")         # main-option1
        quit_app_action = QAction("Quit", self)                                # sub-option1
        quit_app_action.setShortcut("Ctrl+Q")
        self.appOption.addAction(quit_app_action)
        # calling for desired function upon clicking/selecting an sub-option
        self.appOption.triggered[QAction].connect(self.quit_application)

        self.studentOption = self.bar.addMenu("Student")        # main-option2
        self.studentOption.addAction("Registration")                    # sub-option1
        self.studentOption.addAction("View Information")            # sub-option2
        self.studentOption.addAction("Fee Records")                    # sub-option3

        self.settingsOption = self.bar.addMenu("Settings")      # main-option3
        self.settingsOption.addAction("Basic Info")                        # sub-option1
        self.settingsOption.addAction("Fee Structure")                  # sub-option2

        # container for all bare-widgets
        self.mainContainer = QWidget(self)
        # self.mainContainer.setStyleSheet("border: 1px solid black;")
        self.mainContainerLayout = QVBoxLayout(self.mainContainer)
        self.setCentralWidget(self.mainContainer)

    @ staticmethod
    def quit_application():
        exit(0)


def main():
    window = QApplication(sys.argv)
    window.setStyle('Fusion')
    main_app_window = MainWidget()
    main_app_window.show()
    sys.exit(window.exec_())


if __name__ == '__main__':
    main()