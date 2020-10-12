from PyQt5.QtWidgets import QPushButton, QButtonGroup, QWidget


class NavigationButtons(QWidget):
    def __init__(self, on_next=None, on_back=None, parent=None):
        super(NavigationButtons, self).__init__(parent)
        self.group = QButtonGroup(parent)
        self.btn_next = QPushButton('Next')
        self.btn_back = QPushButton('Back')
        #  self.btn_next.clicked.connect(on_next)
        #  self.btn_back.clicked.connect(on_back)
        self.group.addButton(self.btn_back)
        self.group.addButton(self.btn_next)
