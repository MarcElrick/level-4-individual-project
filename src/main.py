import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from gui.lipid_details_screen import LipidDetailsScreen


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 600, 600)
    win.setWindowTitle("Lipid Infererence")
    LipidDetailsScreen(win)

    win.show()
    sys.exit(app.exec_())


window()
