from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar
from gui.custom_components import CustomTitle


class ProgressScreen(QWidget):
    def __init__(self, numLipids, numFiles, page_state=None):
        super(ProgressScreen, self).__init__()
        layout = QVBoxLayout()
        progress_bar = QProgressBar()
        progress_bar.setRange(0, 100)
        page_state.setIncrementSize(100 // (numLipids * numFiles))
        page_state.setProgressIncrementFunction(progress_bar.setValue)

        layout.addWidget(CustomTitle('Performing Analysis'))
        layout.addWidget(progress_bar)
        self.setLayout(layout)
        page_state.startAnalysis()
