from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QTextEdit, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QTextCursor
from gui.custom_components import CustomTitle
import sys


# Code snippets taken from
# stackoverflow.com/questions/44432276/print-out-python-console-output-to-qtextedit

class ProgressScreen(QWidget):
    def __init__(self, numLipids, numFiles, page_state=None, on_next=None):
        super(ProgressScreen, self).__init__()
        layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.valueChanged.connect(
            lambda x: self.enable_restart_button(x))
        page_state.setIncrementSize(100 // (numLipids * numFiles))
        page_state.setProgressIncrementFunction(self.progress_bar.setValue)
        self.console = QTextEdit()
        self.console.moveCursor(QTextCursor.Start)
        self.console.ensureCursorVisible()
        self.console.setLineWrapColumnOrWidth(500)
        self.console.setLineWrapMode(QTextEdit.FixedPixelWidth)

        sys.stdout = Stream(newText=self.onUpdateText)

        self.next_btn = QPushButton('Restart')
        self.next_btn.setMaximumWidth(100)
        self.next_btn.setEnabled(False)

        self.next_btn.clicked.connect(on_next)
        layout.addWidget(CustomTitle('Performing Analysis'))
        layout.addWidget(self.console)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.next_btn)
        self.setLayout(layout)
        page_state.startAnalysis()

    def onUpdateText(self, text):
        cursor = self.console.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.console.setTextCursor(cursor)
        self.console.ensureCursorVisible()

    def enable_restart_button(self, value):
        if value == 100:
            self.next_btn.setEnabled(True)


class Stream(QObject):
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))
