import sys

from PyQt5.QtWidgets import QApplication
from gui.gui_controller import MainApp
from state.state_controller import StateController


if __name__ == '__main__':
    app = QApplication(sys.argv)
    state = StateController()
    window = MainApp(state)
    sys.exit(app.exec_())
