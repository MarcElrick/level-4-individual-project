from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel
from gui.nav_buttons import NavigationButtons
import sys


class LipidDetailsScreen(QWidget):
    def __init__(self, parent=None):
        super(LipidDetailsScreen, self).__init__(parent)
       # self.nav_buttons = NavigationButtons(
        #    on_next=self.next_btn_clicked, on_back=self.next_btn_clicked, parent=parent)
        self.layout = QVBoxLayout()
        self.btn_next = QPushButton('Next')
        self.btn_prev = QPushButton('Back')
        self.init_ui()

    def init_ui(self):
        self.layout.addWidget(self.btn_prev)
        self.layout.addWidget(self.btn_next)
        # self.layout.addWidget(self.nav_buttons)
        self.btn_next.clicked.connect(self.next_btn_clicked)
        self.setLayout(self.layout)

    def next_btn_clicked(self):
        print("Next Button Clicked")
