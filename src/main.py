import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.gui_controller import MainApp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainApp()
    sys.exit(app.exec_())
