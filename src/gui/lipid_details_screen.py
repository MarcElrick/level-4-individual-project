from molmass import Formula, FormulaError
from gui.custom_components import (
    CustomTitle, CustomFieldLabel, ActionButton, DeleteButton)
from PyQt5.QtCore import Qt
from helper import mass2ion
from gui.nav_buttons import NavigationButtons
from PyQt5.QtWidgets import (QWidget, QFormLayout, QVBoxLayout, QHBoxLayout,
                             QComboBox, QLineEdit, QSpinBox, QDoubleSpinBox,
                             QRadioButton, QScrollArea, QSizePolicy)

from gui.collapsible_section import Section
from assets import strings


class LipidDetailsScreen(QWidget):
    def __init__(self, page_state=None, on_next=None, on_back=None):
        super(LipidDetailsScreen, self).__init__()
        self.page_state = page_state

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
        self.nav_buttons = NavigationButtons(on_next=on_next)

        self.build_ui(on_next=on_next, on_back=on_back)
        self.validate_and_enable_progression()

    def build_ui(self, on_next, on_back):
        self.screen_layout = QVBoxLayout()
        self.title = CustomTitle("Step 1: Enter lipid Information")
        self.screen_layout.addWidget(self.title)

        charge_btn_container = QHBoxLayout()
        charge_btn_container.addWidget(CustomFieldLabel("Charge Mode"))
        charge_btn_container.addWidget(self.btn_positive)
        charge_btn_container.addWidget(self.btn_negative)
        self.screen_layout.addLayout(charge_btn_container)

        wrapper = QWidget()
        wrapper.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

        self.content_layout = QVBoxLayout(wrapper)
        self.content_layout.setSizeConstraint(5)

        for lipid in self.page_state.lipids:
            newLipid = LipidListItem(
                self.page_state, lipid,  self.validate_and_enable_progression)
            self.content_layout.addWidget(newLipid)
            newLipid.validate_lipid_formula(newLipid.lipid.lipid_formula)

        scroll_area = QScrollArea()
        scroll_area.setWidget(wrapper)
        scroll_area.setWidgetResizable(True)

        new_lipid_btn = ActionButton('New Lipid')
        new_lipid_btn.clicked.connect(self.add_lipid)

        self.screen_layout.addWidget(scroll_area)
        self.nav_buttons.btn_next.setEnabled(False)
        self.screen_layout.addWidget(new_lipid_btn)
        self.screen_layout.addWidget(self.nav_buttons)
        self.setLayout(self.screen_layout)

    def charge_mode_toggled(self, value):
        self.page_state.setChargeMode(value)

        for i in range(self.content_layout.count()):
            self.content_layout.itemAt(i).widget().charge_mode_toggled(value)

    def add_lipid(self):

        self.page_state.add_lipid()
        self.content_layout.addWidget(LipidListItem(
            self.page_state, self.page_state.lipids[-1], self.validate_and_enable_progression))

        for i in range(self.content_layout.count()-1):
            self.content_layout.itemAt(
                i).widget().section.toggleButton.setChecked(False)
            self.content_layout.itemAt(
                i).widget().section.toggle(False)

    def validate_and_enable_progression(self):
        self.nav_buttons.btn_next.setEnabled(
            self.page_state.validate_lipids())


class LipidListItem(QWidget):
    def __init__(self, page_state, lipid, on_change):
        super(QWidget, self).__init__()

        self.on_change = on_change
        self.lipid = lipid
        self.page_state = page_state

        self.section = Section(self.lipid.name, 100, self)

        self.lipid_layout = QFormLayout()

        self.lipid_name = QLineEdit(parent=self.section)
        self.lipid_name.setText(self.lipid.name)
        self.lipid_name.textChanged.connect(self.update_lipid_name)
        self.lipid_name.setToolTip(strings.tooltips['lipidName'])

        self.lipid_formula = QLineEdit(parent=self.section)
        self.lipid_formula.setText(self.lipid.lipid_formula)
        self.lipid_formula.textChanged.connect(self.validate_lipid_formula)

        self.adduct_type = QComboBox(parent=self.section)
        self.adduct_type.addItems(
            self.page_state.getAdductLabels(self.lipid.adduct_list))
        self.adduct_type.setCurrentIndex(self.lipid.adduct_index)
        self.adduct_type.currentIndexChanged.connect(
            self.updateAdduct)

        self.isotope_depth = QSpinBox(parent=self.section)
        self.isotope_depth.wheelEvent = lambda *event: None
        self.isotope_depth.setRange(0, 9)
        self.isotope_depth.setValue(self.lipid.isotope_depth)
        self.isotope_depth.valueChanged.connect(self.update_isotope_depth)
        self.isotope_depth.setToolTip(strings.tooltips["isotopeDepth"])
        self.isotope_depth.setToolTipDuration(0)

        self.retention_time = QDoubleSpinBox(decimals=0, parent=self.section)
        self.retention_time.wheelEvent = lambda *event: None
        self.retention_time.setRange(0, 1000)
        self.retention_time.setValue(self.lipid.retention_time)
        self.retention_time.valueChanged.connect(self.update_retention_time)

        self.retention_time_tolerance = QDoubleSpinBox(
            decimals=0, parent=self.section)
        self.retention_time_tolerance.wheelEvent = lambda *event: None
        self.retention_time_tolerance.setRange(0, 100)
        self.retention_time_tolerance.setValue(
            self.lipid.retention_time_tolerance)
        self.retention_time_tolerance.valueChanged.connect(
            self.update_retention_time_tolerance)

        self.mass = QDoubleSpinBox(decimals=20, parent=self.section)
        self.mass.wheelEvent = lambda *event: None
        self.mass.setRange(0, 10000)
        self.mass.setValue(
            self.lipid.mass)
        self.mass.valueChanged.connect(
            self.lipid.setMass)

        self.mass_tolerance = QDoubleSpinBox(decimals=6, parent=self.section)
        self.mass_tolerance.wheelEvent = lambda *event: None
        self.mass_tolerance.setRange(0, 100)
        self.mass_tolerance.setValue(
            self.lipid.mass_tolerance)
        self.mass_tolerance.valueChanged.connect(
            self.update_mass_tolerance)

        self.mass_tolerance_units = QComboBox(parent=self.section)
        self.mass_tolerance_units.addItems(
            self.lipid.mass_tolerance_units_list)
        self.mass_tolerance_units.setCurrentIndex(
            self.lipid.mass_tolerance_units_index)
        self.mass_tolerance_units.currentIndexChanged.connect(
            self.lipid.setMassToleranceUnits)

        self.remove_btn = DeleteButton('Remove Lipid')
        self.remove_btn.clicked.connect(self.remove_lipid)
        self.build_ui()
        self.on_change()

    def build_ui(self):

        self.lipid_layout.addRow(
            CustomFieldLabel('Lipid Name'), self.lipid_name)

        self.lipid_layout.addRow(CustomFieldLabel(
            "Lipid Formula"), self.lipid_formula)

        self.lipid_formula_label = CustomFieldLabel("", alignment='left')
        hill_not_label = CustomFieldLabel("Hill Notation: ")
        hill_not_label.setAlignment(Qt.AlignLeft)
        self.lipid_layout.addRow(CustomFieldLabel(
            "Hill Notation: "), self.lipid_formula_label)

        self.lipid_layout.addRow(CustomFieldLabel(
            "Adduct Type"), self.adduct_type)

        self.lipid_layout.addRow(CustomFieldLabel(
            "Number of Isotopes"), self.isotope_depth)

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

        self.lipid_layout.addRow(rt_container)
        self.lipid_layout.addRow(mass_container)
        self.lipid_layout.addWidget(self.remove_btn)
        self.section.setContentLayout(self.lipid_layout)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.section)
        self.section.toggleButton.setChecked(True)
        self.section.toggle(True)

    def charge_mode_toggled(self, value):
        self.adduct_type.clear()
        self.adduct_type.addItems(
            self.page_state.getAdductLabels(self.page_state.adduct_list))

    def update_lipid_name(self, text):
        self.section.setTitle(text)
        self.lipid.setName(text)

    def update_retention_time(self, value):
        self.lipid.setRetentionTime(value)
        self.on_change()

    def update_retention_time_tolerance(self, value):
        self.lipid.setRetentionTimeTolerance(value)

    def update_mass_tolerance(self, value):
        self.lipid.setMassTolerance(value)
        self.on_change()

    def update_isotope_depth(self, value):
        self.lipid.setIsotopeDepth(value)
        self.on_change()

    def remove_lipid(self):
        self.setParent(None)
        self.page_state.remove_lipid(self.lipid.key)
        self.on_change()

    def validate_lipid_formula(self, text):
        f = Formula(text)
        try:
            self.lipid.setLipidFormula(text)
            self.lipid_formula.setStyleSheet("border: 1px solid green")
            self.lipid_formula_label.setText(f.formula)
            self.mass.setValue(
                mass2ion(f.isotope.mass,
                         self.lipid.adduct_list[self.lipid.adduct_index][2],
                         self.lipid.adduct_list[self.lipid.adduct_index][1]))
            self.mass.update()
        except FormulaError:
            self.lipid_formula.setStyleSheet("border: 1px solid red")
            self.lipid_formula_label.setText("")
        finally:
            self.on_change()

    def updateAdduct(self, value):
        self.lipid.setAdductIndex(value)
        self.mass.setValue(self.lipid.mass)
