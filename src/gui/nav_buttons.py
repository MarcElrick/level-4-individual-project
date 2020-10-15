from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget


class NavigationButtons(QWidget):
    def __init__(self, on_next=None, on_back=None):
        super(NavigationButtons, self).__init__()
        layout = QHBoxLayout()
        self.btn_next = QPushButton('Next')
        self.btn_back = QPushButton('Back')
        if on_next:
            self.btn_next.clicked.connect(on_next)
        else:
            self.btn_next.setDisabled(True)
        if on_back:
            self.btn_back.clicked.connect(on_back)
        else:
            self.btn_back.setDisabled(True)
        layout.addWidget(self.btn_back)
        layout.addWidget(self.btn_next)
        self.setLayout(layout)
