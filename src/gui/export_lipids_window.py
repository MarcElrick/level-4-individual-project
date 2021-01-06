from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt


class ExportLipidsWindow(QWidget):
    def __init__(self, save_fn):
        super(ExportLipidsWindow, self).__init__()

        self.filename = ""
        self.save_fn = save_fn
        layout = QFormLayout(parent=self)
        self.setWindowModality(Qt.ApplicationModal)

        self.setWindowTitle('Export Lipid Data')

        txt_filename = QLineEdit()
        txt_filename.textChanged.connect(self.setFilename)

        exit_button = QPushButton("Close")
        exit_button.clicked.connect(lambda: self.close())

        self.save_button = QPushButton("Save")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save)

        layout.addRow(QLabel("Filename"), txt_filename)
        layout.addRow(exit_button, self.save_button)

    def save(self):
        self.save_fn(self.filename)
        self.close()

    def setFilename(self, text):
        self.filename = text

        if(text == ""):
            self.save_button.setEnabled(False)
        else:
            self.save_button.setEnabled(True)
