from PyQt5.QtWidgets import (QWidget, QGridLayout, QScrollArea, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from helper import getFilenameFromPath
from gui.custom_components import CustomTitle, SummaryDisplayCard, ActionButton


class InputSummaryScreen(QWidget):
    def __init__(self, page_state=None, on_next=None, on_back=None):
        super(InputSummaryScreen, self).__init__()
        self.outer_layout = QVBoxLayout()

        files_widget = QWidget()
        files_scroll = QScrollArea()
        lipids_scroll = QScrollArea()

        files_layout = QHBoxLayout(files_widget)

        files_layout.addWidget(SummaryDisplayCard(
            "File", *map(getFilenameFromPath, list(zip(*page_state.get_file_info()))[0])))

        files_layout.addWidget(SummaryDisplayCard(
            "Time(Hours)", *map(str, list(zip(*page_state.get_file_info()))[1])
        ))

        lipids_scroll = QScrollArea()
        lipids_scroll.setWidget(
            self.collate_lipid_info(page_state.get_lipid_info()))
        files_scroll = QScrollArea()
        files_scroll.setWidget(files_widget)

        self.outer_layout.addWidget(CustomTitle(
            'Step 3: Review analysis details'))
        self.outer_layout.addWidget(CustomTitle('Lipids'))
        self.outer_layout.addWidget(lipids_scroll)

        self.outer_layout.addWidget(CustomTitle(
            'Files'))
        self.outer_layout.addWidget(files_scroll)

        self.btn_start = ActionButton('Start Analyisis')
        self.btn_start.setMaximumWidth(150)
        self.outer_layout.addWidget(self.btn_start)
        self.btn_back = QPushButton('Back')
        self.btn_back.clicked.connect(on_back)
        self.btn_back.setMaximumWidth(150)
        self.btn_start.clicked.connect(on_next)

        self.outer_layout.addWidget(self.btn_back)
        self.outer_layout.setAlignment(Qt.AlignHCenter)
        self.setLayout(self.outer_layout)

    def collate_lipid_info(self, lipid_info):

        lipid_widget = QWidget()
        layout = QGridLayout()

        lipid_widget.setLayout(layout)
        for index, lipid in enumerate(lipid_info):
            layout.addWidget(SummaryDisplayCard(
                "Name", list(lipid.keys())[0]), 2*index, 0, 1, 1)
            layout.addWidget(SummaryDisplayCard(
                "Formula", list(lipid.values())[0]['formula']), 2*index, 1, 1, 1)
            layout.addWidget(SummaryDisplayCard(
                "Adduct", list(lipid.values())[0]['adduct'][0]), 2*index, 2, 1, 1)
            layout.addWidget(SummaryDisplayCard(
                "Mass (m/z)", list(lipid.values())[0]['mass']), 2*index, 3, 1, 1)
            layout.addWidget(SummaryDisplayCard(
                "Mass Tolerance", list(lipid.values())[0]['massTolerance']
                + list(lipid.values())[0]['massToleranceUnits']), 2*index + 1, 0, 1, 1)
            layout.addWidget(SummaryDisplayCard(
                "Retention Time", list(lipid.values())[0]['retentionTime']), 2*index + 1, 1, 1, 1)
            layout.addWidget(SummaryDisplayCard(
                "Retention Time Tolerance", list(lipid.values())[0]['retentionTimeTolerance']), 2*index+1, 2, 1, 1)
            layout.addWidget(SummaryDisplayCard(
                "Isotope Depth", list(lipid.values())[0]['isotopeDepth']), 2*index+1, 3, 1, 1)

        return lipid_widget
