from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from gui.nav_buttons import NavigationButtons

class ProgressScreen(QWidget):
    def __init__(self, on_next=None, on_back=None):
        super(ProgressScreen, self).__init__()

        nav_buttons = NavigationButtons(on_next=on_next, on_back=on_back)

        layout = QGridLayout()
        layout.addWidget(nav_buttons)
        self.setLayout(layout)
