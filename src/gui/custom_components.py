from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
import os

# To work with PyInstaller, we need to get the absolute path for css file.
stylesheet = """
    #title {
        font-size: 30px;
    }

    #field {
        font-size: 15px;
        qproperty-alignment: AlignRight;
        padding: 5px;
    }

    #deleteButton {
        color: #FFF;
        background-color: #B71C1C;
    }

    #addButton {
        color: #FFF;
        background-color: #01579B;
        min-width: 150px;
    }
"""


class DeleteButton(QPushButton):
    def __init__(self, text):
        super(QPushButton, self).__init__()
        self.setText(text)
        self.setObjectName('deleteButton')
        self.setStyleSheet(stylesheet)


class AddButton(QPushButton):
    def __init__(self, text):
        super(QPushButton, self).__init__()
        self.setText(text)
        self.setObjectName('addButton')
        self.setStyleSheet(stylesheet)


class CustomTitle(QLabel):
    def __init__(self, text):
        super(QLabel, self).__init__()
        self.setText(text)
        self.setObjectName('title')
        self.setStyleSheet(stylesheet)


class CustomFieldLabel(QLabel):
    def __init__(self, text):
        super(QLabel, self).__init__()
        self.setText(text)
        self.setObjectName('field')
        self.setStyleSheet(stylesheet)
