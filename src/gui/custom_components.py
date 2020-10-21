from PyQt5.QtWidgets import QLabel
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
"""


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
