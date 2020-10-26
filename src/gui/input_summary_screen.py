from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QPushButton
from gui.nav_buttons import NavigationButtons
from gui.custom_components import CustomTitle, SummaryDisplayCard, ActionButton
from helper import getFilenameFromPath
import sys


class InputSummaryScreen(QWidget):
    def __init__(self, page_state=None, on_next=None, on_back=None):
        super(InputSummaryScreen, self).__init__()

        self.layout = QGridLayout()

        self.layout.addWidget(CustomTitle(
            'Step 3: Review analysis details'), 0, 0, 1, 0)
        self.displaySummaryInfo(
            page_state.get_lipid_info(), page_state.get_file_info())

        self.btn_start = ActionButton('Start Analyisis')
        self.layout.addWidget(self.btn_start, 7, 0, 1, 3)
        self.btn_back = QPushButton('Back')
        self.btn_back.clicked.connect(on_back)
        self.layout.addWidget(self.btn_back)

        self.setLayout(self.layout)

    def displaySummaryInfo(self, lipid_dict, file_list):
        row = 3
        col = 0
        for key, val in lipid_dict.items():
            self.layout.addWidget(SummaryDisplayCard(key, str(val)), row, col)
            if(col == 2):
                col = 0
                row += 1
            else:
                col += 1

        # Take a new line
        row += 1

        self.layout.addWidget(SummaryDisplayCard(
            "Files", *map(getFilenameFromPath, list(zip(*file_list))[0])), row, 0, 1, 2)

        self.layout.addWidget(SummaryDisplayCard(
            "Times", *map(str, list(zip(*file_list))[1])
        ), row, 2, 1, 3)
