from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QPushButton,  QSpinBox
from PyQt5.QtCore import Qt
from gui.nav_buttons import NavigationButtons
from gui.custom_components import CustomTitle, CustomFieldLabel, DeleteButton, ActionButton
from helper import getFilenameFromPath, sortFileTimeList
import os


class FilePickerScreen(QWidget):
    def __init__(self, page_state=None, on_next=None, on_back=None,  redraw=None):
        super(FilePickerScreen, self).__init__()
        self.state = page_state
        self.on_next = on_next
        self.on_back = on_back
        #self.redraw = redraw
        self.build_ui()

    def build_ui(self):
        self.outerLayout = QVBoxLayout()
        self.title = CustomTitle(
            "Step 2: Pick files and enter experiment time-points.")

        self.innerLayout = QVBoxLayout()

        # Create all pairing items from existing pairs.
        for pairing in self.state.file_time_pairs:
            self.innerLayout.addWidget(
                PairListItem(pairing, self.remove_pairing, self.validate))

        self.nav_buttons = NavigationButtons(
            on_next=self.onNextClick, on_back=self.on_back)
        self.nav_buttons.btn_next.setDisabled(
            len(self.state.file_time_pairs) == 0)

        self.btn_add = ActionButton("Choose Files")
        self.btn_add.clicked.connect(self.add_files)

        self.outerLayout.addWidget(self.title)
        self.outerLayout.addLayout(self.innerLayout)
        self.outerLayout.addWidget(self.btn_add, alignment=Qt.AlignCenter)
        self.outerLayout.addWidget(self.nav_buttons)

        self.setLayout(self.outerLayout)
        self.validate()

    def add_files(self):
        filter = "Mass Spec Files (*.mzml)"
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFiles)
        files = dialog.getOpenFileNames(
            self, "Open files", "~", filter)[0]

        for f in files:
            self.state.add_record(filepath=f)
            self.innerLayout.addWidget(
                PairListItem(self.state.file_time_pairs[-1], self.remove_pairing, self.validate))
        self.validate()

    def remove_pairing(self, record):
        self.state.remove_record(record.key)
        if(len(self.state.file_time_pairs) == 0):
            self.nav_buttons.btn_next.setDisabled(True)

        self.validate()

    def onNextClick(self):
        self.state.file_time_pairs = sortFileTimeList(
            self.state.file_time_pairs)
        self.on_next()

    def validate(self):
        filepaths = list(map(lambda x: x.filepath, self.state.file_time_pairs))
        times = list(map(lambda x: x.time, self.state.file_time_pairs))

        self.nav_buttons.btn_next.setEnabled(
            not any(filepaths.count(x) > 1 for x in filepaths) and not any(
                times.count(x) > 1 for x in times) and len(filepaths) >= 5

        )


class PairListItem(QWidget):
    def __init__(self, record, on_delete, on_validate):
        super(QWidget, self).__init__()
        self.record = record
        self.on_delete = on_delete
        self.on_validate = on_validate
        self.layout = QHBoxLayout()

        self.path_label = CustomFieldLabel('File')

        self.btn_choose_file = QPushButton("Choose File...")
        if record.filepath != "":
            self.btn_choose_file.setText(getFilenameFromPath(record.filepath))
        self.btn_choose_file.clicked.connect(self.getFilepath)

        self.time_entry = QSpinBox()
        self.time_entry.wheelEvent = lambda *event: None
        self.time_entry.setValue(record.time)
        self.time_entry.setRange(0, 1000)
        self.time_entry.valueChanged.connect(self.onTimeChange)

        self.btn_delete = DeleteButton("Delete")
        self.btn_delete.clicked.connect(self.deletePairing)

        self.layout.addWidget(self.path_label)
        self.layout.addWidget(self.btn_choose_file)
        self.layout.addWidget(CustomFieldLabel("Time-point(hours)"))
        self.layout.addWidget(self.time_entry)
        self.layout.addWidget(self.btn_delete)
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

    def deletePairing(self):
        self.on_delete(self.record)
        self.setParent(None)

    def getFilepath(self):
        self.record.filepath = os.path.abspath(QFileDialog.getOpenFileName(
            QFileDialog(), "Open File", "~", "Mass Spec files(*.mzML)")[0])
        self.btn_choose_file.setText(getFilenameFromPath(self.record.filepath))
        self.on_validate()

    def onTimeChange(self, value):
        self.record.time = value
        self.on_validate()
