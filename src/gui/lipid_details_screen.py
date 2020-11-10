import sys
from molmass import Formula, FormulaError
from gui.custom_components import CustomTitle, CustomFieldLabel
from PyQt5.QtCore import Qt
from helper import mass2iso
from gui.nav_buttons import NavigationButtons
from PyQt5.QtWidgets import (QWidget, QFormLayout, QVBoxLayout, QHBoxLayout,
                             QComboBox, QLineEdit, QSpinBox, QDoubleSpinBox,
                             QCheckBox, QRadioButton, QButtonGroup)


class LipidDetailsScreen(QWidget):
    def __init__(self, page_state=None, on_next=None, on_back=None):
        super(LipidDetailsScreen, self).__init__()

        self.page_state = page_state
        self.lipid_formula = QLineEdit()
        self.lipid_formula.setText(page_state.lipid_formula)
        self.lipid_formula.textChanged.connect(self.validate_lipid_formula)

        self.btn_positive = QRadioButton('Positive')
        self.btn_negative = QRadioButton('Negative')
        if self.page_state.charge_mode == 'Negative':
            self.btn_negative.setChecked(True)
        else:
            self.btn_positive.setChecked(True)

        self.btn_positive.toggled.connect(
            lambda: self.charge_mode_toggled('Positive'))
        self.btn_negative.toggled.connect(
            lambda: self.charge_mode_toggled('Negative'))

        self.adduct_type = QComboBox()
        self.adduct_type.addItems(
            page_state.getAdductLabels(page_state.adduct_list))
        self.adduct_type.setCurrentIndex(page_state.adduct_index)
        self.adduct_type.currentIndexChanged.connect(
            self.updateAdduct)

        self.isotope_depth = QSpinBox()
        self.isotope_depth.setRange(0, 9)
        self.isotope_depth.setValue(page_state.isotope_depth)
        self.isotope_depth.valueChanged.connect(page_state.setIsotopeDepth)

        self.retention_time = QDoubleSpinBox(decimals=0)
        self.retention_time.setRange(0, 1000)
        self.retention_time.setValue(page_state.retention_time)
        self.retention_time.valueChanged.connect(page_state.setRetentionTime)

        self.retention_time_tolerance = QDoubleSpinBox(decimals=0)
        self.retention_time_tolerance.setRange(0, 100)
        self.retention_time_tolerance.setValue(
            page_state.retention_time_tolerance)
        self.retention_time_tolerance.valueChanged.connect(
            page_state.setRetentionTimeTolerance)

        self.mass = QDoubleSpinBox(decimals=20)
        self.mass.setRange(0, 10000)
        self.mass.setValue(
            page_state.mass)
        self.mass.valueChanged.connect(
            page_state.setMass)

        self.mass_tolerance = QDoubleSpinBox(decimals=6)
        self.mass_tolerance.setRange(0, 100)
        self.mass_tolerance.setValue(
            page_state.mass_tolerance)
        self.mass_tolerance.valueChanged.connect(
            page_state.setMassTolerance)

        self.mass_tolerance_units = QComboBox()
        self.mass_tolerance_units.addItems(
            page_state.mass_tolerance_units_list)
        self.mass_tolerance_units.setCurrentIndex(
            page_state.mass_tolerance_units_index)
        self.mass_tolerance_units.currentIndexChanged.connect(
            page_state.setMassToleranceUnits)

        self.build_ui(on_next=on_next, on_back=on_back)

    def build_ui(self, on_next, on_back):
        self.screen_layout = QVBoxLayout()
        self.title = CustomTitle("Step 1: Enter lipid Information")
        self.screen_layout.addWidget(self.title)

        self.content_layout = QFormLayout()
        self.content_layout.addRow(CustomFieldLabel(
            "Lipid Formula"), self.lipid_formula)

        self.lipid_formula_label = CustomFieldLabel("", alignment='left')
        hill_not_label = CustomFieldLabel("Hill Notation: ")
        hill_not_label.setAlignment(Qt.AlignLeft)
        self.content_layout.addRow(CustomFieldLabel(
            "Hill Notation: "), self.lipid_formula_label)

        charge_btn_container = QHBoxLayout()
        charge_btn_container.addWidget(CustomFieldLabel("Charge Mode"))
        charge_btn_container.addWidget(self.btn_positive)
        charge_btn_container.addWidget(self.btn_negative)

        self.content_layout.addRow(charge_btn_container)

        self.content_layout.addRow(CustomFieldLabel(
            "Adduct Type"), self.adduct_type)

        self.content_layout.addRow(CustomFieldLabel(
            "Isotope Depth"), self.isotope_depth)

        rt_container = QHBoxLayout()
        rt_container.addWidget(CustomFieldLabel(
            "Retention Time(s)"))
        rt_container.addWidget(self.retention_time)
        rt_container.addWidget(CustomFieldLabel(
            "tolerance(s)"))
        rt_container.addWidget(self.retention_time_tolerance)

        self.mass.setDisabled(True)
        mass_container = QHBoxLayout()
        mass_container.addWidget(CustomFieldLabel("Mass(m/z)"))
        mass_container.addWidget(self.mass)
        mass_container.addWidget(CustomFieldLabel("tolerance"))
        mass_container.addWidget(self.mass_tolerance_units)
        mass_container.addWidget(self.mass_tolerance)

        self.content_layout.addRow(rt_container)
        self.content_layout.addRow(mass_container)
        self.screen_layout.addLayout(self.content_layout)
        self.nav_buttons = NavigationButtons(on_next=on_next)
        self.screen_layout.addWidget(self.nav_buttons)
        self.validate_lipid_formula(self.lipid_formula.text())

        self.setLayout(self.screen_layout)

    def charge_mode_toggled(self, value):
        self.page_state.setChargeMode(value)
        self.adduct_type.clear()
        self.adduct_type.addItems(
            self.page_state.getAdductLabels(self.page_state.adduct_list))

    def updateAdduct(self, value):
        self.page_state.setAdductIndex(value)
        self.mass.setValue(self.page_state.mass)

    def validate_lipid_formula(self, text):
        f = Formula(text)
        try:
            self.page_state.setLipidFormula(text)
            self.lipid_formula.setStyleSheet("border: 1px solid green")
            self.lipid_formula_label.setText(f.formula)
            self.nav_buttons.btn_next.setDisabled(False)
            self.mass.setValue(
                mass2iso(f.isotope.mass,
                         self.page_state.adduct_list[self.page_state.adduct_index][2],
                         self.page_state.adduct_list[self.page_state.adduct_index][1]))
            self.mass.update()
        except FormulaError:
            self.lipid_formula.setStyleSheet("border: 1px solid red")
            self.lipid_formula_label.setText("")
            self.nav_buttons.btn_next.setDisabled(True)
