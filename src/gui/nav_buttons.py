from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QSpacerItem


class NavigationButtons(QWidget):

    def __init__(self, on_next=None, on_back=None):
        super(NavigationButtons, self).__init__()
        self.layout = QHBoxLayout()
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

        self.btn_next.setMaximumWidth(150)
        self.btn_back.setMaximumWidth(150)

        self.layout.addWidget(self.btn_back)
        self.layout.addWidget(self.btn_next)
        self.setLayout(self.layout)
