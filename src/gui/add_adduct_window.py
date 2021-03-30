from gui.custom_components import CustomFieldLabel
from PyQt5.QtWidgets import (
    QWidget, QFormLayout,
    QLineEdit, QPushButton, QDoubleSpinBox, QRadioButton, QHBoxLayout)
from assets.pathFinder import get_resource_path
from PyQt5.QtCore import Qt
import os


class AddAdductWindow(QWidget):
    def __init__(self, state):
        super(AddAdductWindow, self).__init__()

        self.state = state
        self.adductFormula = ""
        self.adduct_mult = 0.0
        self.adduct_add = 0.0
        self.adduct_label = ""
        self.charge_mode = ""

        self.setWindowModality(Qt.ApplicationModal)

        self.setWindowTitle('New Adduct')
        layout = QFormLayout()

        self.btn_positive = QRadioButton('Positive')
        self.btn_negative = QRadioButton('Negative')

        self.btn_positive.clicked.connect(
            lambda: self.charge_mode_toggled('Positive'))
        self.btn_negative.clicked.connect(
            lambda: self.charge_mode_toggled('Negative'))

        charge_btn_container = QHBoxLayout()
        charge_btn_container.addWidget(CustomFieldLabel("Charge Mode"))
        charge_btn_container.addWidget(self.btn_positive)
        charge_btn_container.addWidget(self.btn_negative)

        addition_spinbox = QDoubleSpinBox(decimals=20)
        addition_spinbox.setRange(-100, 100)
        addition_spinbox.valueChanged.connect(self.setAdductAdd)

        multiplication_spinbox = QDoubleSpinBox(decimals=20)
        multiplication_spinbox.setRange(0, 1)
        multiplication_spinbox.valueChanged.connect(self.setAdductMult)

        btn_cancel = QPushButton('Cancel')
        btn_cancel.clicked.connect(lambda: self.close())
        self.btn_submit = QPushButton('Submit')
        self.btn_submit.setEnabled(False)
        self.btn_submit.clicked.connect(self.handleSubmit)

        self.txt_adduct_formula = QLineEdit()
        self.txt_adduct_formula.textChanged.connect(self.setAdductFormula)

        self.txt_label = QLineEdit()
        self.txt_label.textChanged.connect(self.setLabel)

        layout.addRow(CustomFieldLabel('Adduct Formula'),
                      self.txt_adduct_formula)
        layout.addRow(charge_btn_container)
        layout.addRow(CustomFieldLabel(
            'Adduct Addition Value'), addition_spinbox)
        layout.addRow(CustomFieldLabel(
            'Adduct Multiplication Value'), multiplication_spinbox)
        layout.addRow(btn_cancel, self.btn_submit)

        self.setLayout(layout)

    def validateInput(self):
        if (self.adductFormula != "" and self.charge_mode != ""
                and self.adduct_mult != 0):
            self.btn_submit.setEnabled(True)
        else:
            self.btn_submit.setEnabled(False)

    def handleSubmit(self):
        filepath = ""

        if self.charge_mode == 'Positive':
            filepath = get_resource_path(
                os.sep.join(['assets', 'positive.csv']))
        elif self.charge_mode == 'Negative':
            filepath = get_resource_path(
                os.sep.join(['assets', 'negative.csv']))

        with open(filepath, 'a') as f:
            f.write('\n' + ','.join([self.adductFormula, str(self.adduct_add), str(
                self.adduct_mult), self.adduct_label]) + ',')

        self.state.adduct_list.append([self.adductFormula, str(
            self.adduct_add), str(self.adduct_mult), str(self.adduct_label)])
        self.state.setAdductList(self.state.charge_mode)

        self.close()

    def charge_mode_toggled(self, value):
        self.charge_mode = value
        self.validateInput()

    def setLabel(self, value):
        self.adduct_label = value

    def setAdductFormula(self, value):
        self.adductFormula = value
        self.validateInput()

    def setAdductAdd(self, value):
        self.adduct_add = value
        self.validateInput()

    def setAdductMult(self, value):
        self.adduct_mult = value
        self.validateInput()
