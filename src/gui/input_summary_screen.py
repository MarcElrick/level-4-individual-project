from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from gui.nav_buttons import NavigationButtons
import sys


class InputSummaryScreen(QWidget):
    def __init__(self, on_next=None, on_back=None):
        super(InputSummaryScreen, self).__init__()

        self.nav_buttons = NavigationButtons(on_next=on_next, on_back=on_back)

        self.layout = QGridLayout()
        self.layout.addWidget(self.nav_buttons)
        self.setLayout(self.layout)
