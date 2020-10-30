from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QPushButton, QMainWindow, QLabel, QSpinBox
from PyQt5.QtCore import Qt
from gui.nav_buttons import NavigationButtons
from gui.custom_components import CustomTitle, CustomFieldLabel, DeleteButton, ActionButton
from helper import getFilenameFromPath
import sys
import os


class FilePickerScreen(QWidget):
    def __init__(self, page_state=None, on_next=None, on_back=None, redraw=None):
        super(FilePickerScreen, self).__init__()
        self.state = page_state
        self.on_next = on_next
        self.on_back = on_back
        self.redraw = redraw
        self.build_ui()

    def build_ui(self):
        self.outerLayout = QVBoxLayout()
        self.title = CustomTitle("Step 2: Pick files and enter times")

        self.innerLayout = QVBoxLayout()

        # Create all pairing items from existing pairs.
        for i in range(0, len(self.state.file_time_pairs)):
            self.innerLayout.addLayout(
                PairListItem(self.state.file_time_pairs[i], lambda i=i: self.remove_pairing(i), lambda i=i: self.state.update_record(self.state.file_time_pairs[i], i)))

        self.nav_buttons = NavigationButtons(
            on_next=self.on_next, on_back=self.on_back)
        self.nav_buttons.btn_next.setDisabled(
            len(self.state.file_time_pairs) == 0)

        self.btn_add = ActionButton("Add File")
        self.btn_add.clicked.connect(self.add_new_pairing)

        self.outerLayout.addWidget(self.title)
        self.outerLayout.addLayout(self.innerLayout)
        self.outerLayout.addWidget(self.btn_add, alignment=Qt.AlignCenter)
        self.outerLayout.addWidget(self.nav_buttons)

        self.setLayout(self.outerLayout)

    def add_new_pairing(self):
        self.nav_buttons.btn_next.setDisabled(False)
        self.state.add_record(
            ["", 0])
        length = len(self.state.file_time_pairs)
        self.innerLayout.addLayout(
            PairListItem(self.state.file_time_pairs[-1], lambda i=length: self.remove_pairing(i-1), lambda i=length: self.state.update_record(self.state.file_time_pairs[i-1], i-1)))

    def remove_pairing(self, index):
        self.state.remove_record(index)
        self.redraw()
        if(len(self.state.file_time_pairs) == 0):
            self.nav_buttons.btn_next.setDisabled(True)


class PairListItem(QHBoxLayout):
    def __init__(self, record, on_delete, on_change):
        super(QHBoxLayout, self).__init__()
        self.record = record
        self.on_change = on_change

        self.path_label = CustomFieldLabel('File')

        self.btn_choose_file = QPushButton("Choose File...")
        if record[0] != "":
            self.btn_choose_file.setText(getFilenameFromPath(record[0]))
        self.btn_choose_file.clicked.connect(self.getFilepath)

        self.time_entry = QSpinBox()
        self.time_entry.setValue(record[1])
        self.time_entry.valueChanged.connect(self.onTimeChange)

        self.btn_delete = DeleteButton("Delete")
        self.btn_delete.clicked.connect(lambda: on_delete())

        self.addWidget(self.path_label)
        self.addWidget(self.btn_choose_file)
        self.addWidget(CustomFieldLabel("Time"))
        self.addWidget(self.time_entry)
        self.addWidget(self.btn_delete)

    def getFilepath(self):
        self.record[0] = os.path.abspath(QFileDialog.getOpenFileName(
            QFileDialog(), "Open File", "~", "Mass Spec files(*.mzML)")[0])
        self.btn_choose_file.setText(getFilenameFromPath(self.record[0]))
        self.on_change()

    def onTimeChange(self, value):
        self.record[1] = value
        self.on_change()
