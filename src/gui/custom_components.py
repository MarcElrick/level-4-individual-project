from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QLayout, QSizePolicy
from PyQt5.QtCore import Qt
import os

# To work with PyInstaller, we need to get the absolute path for css file.
stylesheet = """
    #title {
        font-size: 30px;
    }

    #field {
        font-size: 15px;
        padding: 5px;
    }

    #deleteButton {
        color: #FFF;
        background-color: #B71C1C;
    }

    #actionButton {
        color: #FFF;
        background-color: #01579B;
        qproperty-sizePolicy: Minimum;

    }

    #summaryLabel {
        font-size:16px;
        color:rgba(0, 0, 0, 0.5);
    }

    #summaryValue{
        font-size:22px;
    }

"""


class SummaryDisplayCard(QWidget):
    def __init__(self, label, *values):
        super(QWidget, self).__init__()
        self.setObjectName('summaryCard')
        self.layout = QVBoxLayout()
        self.label = QLabel(label)
        self.label.setObjectName('summaryLabel')
        self.layout.addWidget(self.label)

        for value in values:
            valueWidget = QLabel(value)
            valueWidget.setObjectName('summaryValue')
            self.layout.addWidget(valueWidget)
        self.layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.layout.setSpacing(0)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setStyleSheet(stylesheet)
        self.setLayout(self.layout)


class DeleteButton(QPushButton):
    def __init__(self, text):
        super(QPushButton, self).__init__()
        self.setText(text)
        self.setObjectName('deleteButton')
        self.setStyleSheet(stylesheet)


class ActionButton(QPushButton):
    def __init__(self, text):
        super(QPushButton, self).__init__()
        self.setText(text)
        self.setObjectName('actionButton')
        self.setStyleSheet(stylesheet)


class CustomTitle(QLabel):
    def __init__(self, text):
        super(QLabel, self).__init__()
        self.setText(text)
        self.setObjectName('title')
        self.setStyleSheet(stylesheet)


class CustomFieldLabel(QLabel):
    def __init__(self, text, alignment=None):
        super(QLabel, self).__init__()
        self.setText(text)
        self.setObjectName('field')
        self.setStyleSheet(stylesheet)
        if alignment == 'left':
            self.setAlignment(Qt.AlignLeft)
        elif alignment == 'center':
            self.setAlignment(Qt.AlignLeft)
        else:
            self.setAlignment(Qt.AlignRight)
