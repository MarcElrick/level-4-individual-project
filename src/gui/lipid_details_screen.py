from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QVBoxLayout, QSpacerItem, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox
from gui.nav_buttons import NavigationButtons
from gui.custom_components import CustomTitle, CustomFieldLabel
import sys


class LipidDetailsScreen(QWidget):
    def __init__(self, on_next=None, on_back=None):
        super(LipidDetailsScreen, self).__init__()
        self.screen_layout = QVBoxLayout()

        self.title = CustomTitle("Step 1: Enter lipid Information")
        self.screen_layout.addWidget(self.title)

        self.screen_layout.addWidget(self.title)

        self.content_layout = QFormLayout()
        self.content_layout.addRow(CustomFieldLabel(
            "Isotope Formula"), QLineEdit())

        self.content_layout.addRow(CustomFieldLabel(
            "Adduct Type"), QLineEdit())

        self.content_layout.addRow(CustomFieldLabel(
            "Isotope Depth"), QSpinBox())

        self.content_layout.addRow(CustomFieldLabel(
            "Target Retention Time"), QDoubleSpinBox(decimals=5))

        self.screen_layout.addLayout(self.content_layout)

        self.nav_buttons = NavigationButtons(on_next=on_next)
        self.screen_layout.addWidget(self.nav_buttons)

        self.setLayout(self.screen_layout)
