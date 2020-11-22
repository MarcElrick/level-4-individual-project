import sys
from PyQt5.QtWidgets import QMainWindow, QAction
from gui.lipid_details_screen import LipidDetailsScreen
from gui.file_picker_screen import FilePickerScreen
from gui.input_summary_screen import InputSummaryScreen
from gui.progress_screen import ProgressScreen
from gui.add_adduct_window import AddAdductWindow


class MainApp(QMainWindow):

    def __init__(self, state):
        super().__init__()
        self.state = state
        self.init_ui()
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')

        add_adduct_action = QAction('&Add New Adduct', self)
        self.w = AddAdductWindow(self.state.screen1)
        add_adduct_action.triggered.connect(lambda: self.w.show())

        quit_action = QAction('&Quit', self)
        quit_action.triggered.connect(lambda: sys.exit())

        fileMenu.addAction(add_adduct_action)
        fileMenu.addAction(quit_action)

    def init_ui(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("Lipid Inference")
        self.show()
        self.init_lipid_details_screen()

    def init_lipid_details_screen(self):
        self.setCentralWidget(LipidDetailsScreen(page_state=self.state.screen1,
                                                 on_next=self.init_file_picker_screen))

    def init_file_picker_screen(self):
        self.setCentralWidget(FilePickerScreen(page_state=self.state.screen2,
                                               on_back=self.init_lipid_details_screen,
                                               on_next=self.init_input_summary_screen,
                                               redraw=self.init_file_picker_screen))

    def init_input_summary_screen(self):
        self.setCentralWidget(InputSummaryScreen(page_state=self.state.screen3,
                                                 on_back=self.init_file_picker_screen,
                                                 on_next=self.init_progress_screen))

    def init_progress_screen(self):
        self.setCentralWidget(ProgressScreen(numLipids=1, numFiles=len(self.state.screen2.file_time_pairs),
                                             page_state=self.state.screen4))
