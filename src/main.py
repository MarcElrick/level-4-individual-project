import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.lipid_details_screen import LipidDetailsScreen
from gui.file_picker_screen import FilePickerScreen

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setCentralWidget(LipidDetailsScreen(on_next=self.on_next, on_back=self.on_back))
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("Lipid Infererence")
        self.show()

    def init_file_picker_screen(self):
        self.setCentralWidget(FilePickerScreen(self))

    def init_input_summary_screen(self):
        pass

    def init_progress_screen(self):
        pass

    def on_next(self):
        print("NEXT")

    def on_back(self):
        print('BACK')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainApp()
    sys.exit(app.exec_())
