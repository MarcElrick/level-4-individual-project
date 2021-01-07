from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog, QFormLayout
from PyQt5.QtCore import Qt
import os


class ImportLipidsWindow(QWidget):
    def __init__(self, import_fn):
        super(ImportLipidsWindow, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle('Import Lipid Data')
        self.import_fn = import_fn

        self.filepath = ""

        layout = QFormLayout(parent=self)

        self.btn_choose_file = QPushButton("Choose File...")
        self.btn_choose_file.clicked.connect(self.choose_file)
        self.lbl_filename = QLabel("")

        btn_import = QPushButton("Import")
        btn_import.clicked.connect(self.submit)

        btn_close = QPushButton("Close")
        btn_close.clicked.connect(lambda x: self.close())

        layout.addRow(self.btn_choose_file, self.lbl_filename)
        layout.addRow(btn_close, btn_import)

    def choose_file(self):
        self.filepath = os.path.abspath(QFileDialog.getOpenFileName(
            QFileDialog(), "Choose File", os.getcwd() + os.sep + 'saved_runs', "JSON files(*.json)")[0]).split(os.sep)[-1]

        self.lbl_filename.setText(self.filepath)

    def submit(self):
        self.import_fn(self.filepath)
        self.close()
