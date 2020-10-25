from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QPushButton, QMainWindow, QLabel, QSpinBox
from PyQt5.QtCore import Qt
from gui.nav_buttons import NavigationButtons
from gui.custom_components import CustomTitle, CustomFieldLabel, DeleteButton, AddButton
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
        self.layout = QVBoxLayout()
        self.title = CustomTitle("Step 2: Pick files and enter times")

        # All file pair objects will be placed here:
        self.innerLayout = QVBoxLayout()
        for i in range(len(self.state.file_time_pairs)):
            self.innerLayout.addLayout(
                PairListItem(self.state.file_time_pairs[i], self.remove_pairing, self.state.update_record))

        self.layout.addWidget(self.title)
        self.nav_buttons = NavigationButtons(
            on_next=self.on_next, on_back=self.on_back)
        self.btn_add = AddButton("Add File")
        self.btn_add.clicked.connect(self.add_new_pairing)
        self.layout.addLayout(self.innerLayout)
        self.layout.addWidget(self.btn_add, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.nav_buttons)
        self.setLayout(self.layout)

    def add_new_pairing(self):
        self.state.file_time_pairs.append(
            ["", 0, len(self.state.file_time_pairs)])

        self.innerLayout.addLayout(
            PairListItem(self.state.file_time_pairs[-1], self.remove_pairing, self.state.update_record))

    def remove_pairing(self, index):
        self.state.remove_record(index)
        self.redraw()


class PairListItem(QHBoxLayout):
    def __init__(self, record, on_delete, on_change):
        super(QHBoxLayout, self).__init__()
        self.record = record

        self.on_change = on_change

        self.path_label = CustomFieldLabel('File')
        self.addWidget(self.path_label)

        self.path_label
        self.btn_choose_file = QPushButton("Choose File...")
        self.btn_choose_file.clicked.connect(self.getFilepath)
        self.addWidget(self.btn_choose_file)

        self.addWidget(CustomFieldLabel("Time"))
        self.time_entry = QSpinBox()
        self.time_entry.setValue(record[1])
        self.time_entry.valueChanged.connect(self.onTimeChange)
        self.addWidget(self.time_entry)

        self.btn_delete = DeleteButton("Delete")
        self.btn_delete.clicked.connect(lambda: on_delete(record[2]))
        self.addWidget(self.btn_delete)

    def getFilepath(self):
        self.record[0] = os.path.abspath(QFileDialog.getOpenFileName(
            QFileDialog(), "Open File", "~", "Mass Spec files(*.mzML)")[0])
        self.btn_choose_file.setText(getFilenameFromPath(self.record[0]))

        self.on_change(self.record)

    def onTimeChange(self, value):
        self.record[1] = value
        self.on_change(self.record)


def getFilenameFromPath(filepath):
    if filepath == "":
        return ""
    return os.path.abspath(filepath).split(os.sep)[-1]
