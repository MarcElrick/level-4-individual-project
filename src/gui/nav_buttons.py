from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget


class NavigationButtons(QWidget):
    def __init__(self, on_next=None, on_back=None):
        super(NavigationButtons, self).__init__()
        layout = QHBoxLayout()
        btn_next = QPushButton('Next')
        btn_back = QPushButton('Back')
        btn_next.clicked.connect(on_next)
        btn_back.clicked.connect(on_back)
        layout.addWidget(btn_back)
        layout.addWidget(btn_next)
        self.setLayout(layout)
