from PyQt5.QtWidgets import (QWidget, QGridLayout, QScrollArea,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QSizePolicy, QTableWidget, QTableWidgetItem, QHeaderView)
from PyQt5.QtCore import Qt
from helper import getFilenameFromPath
from gui.custom_components import CustomTitle, SummaryDisplayCard, ActionButton
from gui.collapsible_section import Section


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
        lipids_scroll.setWidgetResizable(True)
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

        table = QTableWidget(len(lipid_info), 9)
        table.setEnabled(False)
        data = {'Name': [list(x.keys())[0] for x in lipid_info],
                'Formula': [list(x.values())[0]['formula'] for x in lipid_info],
                'Adduct': [list(x.values())[0]['adduct'][0] for x in lipid_info],
                'Isotope Depth': [list(x.values())[0]['isotopeDepth'] for x in lipid_info],
                'Retention Time': [list(x.values())[0]['retentionTime'] for x in lipid_info],
                'Retention Time Tolerance': [list(x.values())[0]['retentionTimeTolerance'] for x in lipid_info],
                'Mass': [list(x.values())[0]['mass'] for x in lipid_info],
                'Mass Tolerance': [list(x.values())[0]['massTolerance'] for x in lipid_info],
                'Mass Tolerance Units': [list(x.values())[0]['massToleranceUnits'] for x in lipid_info]
                }
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        horHeaders = []
        for n, key in enumerate(data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QTableWidgetItem(item)
                table.setItem(m, n, newitem)
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)
        table.setHorizontalHeaderLabels(horHeaders)

        return table
