import os
from assets.pathFinder import get_resource_path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QPushButton, QVBoxLayout,
                             QWidget, QLayout, QSizePolicy)


# To work with PyInstaller, we need to get the absolute path for css file.
stylesheet_file = get_resource_path(os.sep.join(["assets", "styles.css"]))
with open(stylesheet_file, "r") as style:
    stylesheet = style.read()


class SummaryDisplayCard(QWidget):
    def __init__(self, label, *values, parent=None):
        super(QWidget, self).__init__(parent)
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
