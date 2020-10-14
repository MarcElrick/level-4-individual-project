from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from gui.nav_buttons import NavigationButtons
import sys


class LipidDetailsScreen(QWidget):
    def __init__(self, on_next=None, on_back=None):
        super(LipidDetailsScreen, self).__init__()

        self.nav_buttons = NavigationButtons(on_next=on_next)

        layout = QGridLayout()
        layout.addWidget(self.nav_buttons)
        self.setLayout(layout)
