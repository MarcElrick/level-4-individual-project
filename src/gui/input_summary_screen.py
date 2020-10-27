from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QPushButton, QLayout, QVBoxLayout
from gui.nav_buttons import NavigationButtons
from PyQt5.QtCore import Qt

from gui.custom_components import CustomTitle, SummaryDisplayCard, ActionButton
from helper import getFilenameFromPath
import sys


class InputSummaryScreen(QWidget):
    def __init__(self, page_state=None, on_next=None, on_back=None):
        super(InputSummaryScreen, self).__init__()
        self.outer_layout = QVBoxLayout()
        self.inner_layout = QGridLayout()
      #  self.inner_layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.outer_layout.addWidget(CustomTitle(
            'Step 3: Review analysis details'))
        self.displaySummaryInfo(
            page_state.get_lipid_info(), page_state.get_file_info())

        self.outer_layout.addItem(self.inner_layout)

        self.btn_start = ActionButton('Start Analyisis')
        self.btn_start.setMaximumWidth(150)
        self.outer_layout.addWidget(self.btn_start)
        self.btn_back = QPushButton('Back')
        self.btn_back.clicked.connect(on_back)
        self.btn_back.setMaximumWidth(150)

        self.outer_layout.addWidget(self.btn_back)
        self.outer_layout.setAlignment(Qt.AlignHCenter)
        self.setLayout(self.outer_layout)

    def displaySummaryInfo(self, lipid_dict, file_list):
        row = 0
        col = 0
        for key, val in lipid_dict.items():
            self.inner_layout.addWidget(
                SummaryDisplayCard(key, str(val)), row, col)
            if(col == 2):
                col = 0
                row += 1
            else:
                col += 1

        # Take a new line
        row += 1

        self.inner_layout.addWidget(SummaryDisplayCard(
            "Files", *map(getFilenameFromPath, list(zip(*file_list))[0])), row, 0, 1, 2)

        self.inner_layout.addWidget(SummaryDisplayCard(
            "Times", *map(str, list(zip(*file_list))[1])
        ), row, 2, 1, 3)
