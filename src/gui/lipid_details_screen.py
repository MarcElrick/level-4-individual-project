from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QComboBox, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox
from gui.nav_buttons import NavigationButtons
from gui.custom_components import CustomTitle, CustomFieldLabel
import sys


class LipidDetailsScreen(QWidget):
    def __init__(self, page_state=None, on_next=None, on_back=None):
        super(LipidDetailsScreen, self).__init__()

        self.isotope_formula = QLineEdit()
        self.isotope_formula.setText(page_state.isotope_formula)
        self.isotope_formula.textChanged.connect(page_state.setIsotopeFormula)

        self.adduct_type = QComboBox()
        self.adduct_type.addItems(page_state.adduct_list)
        self.adduct_type.setCurrentIndex(page_state.adduct_index)
        self.adduct_type.currentIndexChanged.connect(page_state.setAdductIndex)

        self.isotope_depth = QSpinBox()
        self.isotope_depth.setRange(0, 9)
        self.isotope_depth.setValue(page_state.isotope_depth)
        self.isotope_depth.valueChanged.connect(page_state.setIsotopeDepth)

        self.retention_time = QDoubleSpinBox(decimals=6)
        self.retention_time.setRange(0, 1000)
        self.retention_time.setValue(page_state.retention_time)
        self.retention_time.valueChanged.connect(page_state.setRetentionTime)

        self.retention_time_tolerance = QDoubleSpinBox(decimals=6)
        self.retention_time_tolerance.setRange(0, 100)
        self.retention_time_tolerance.setValue(
            page_state.retention_time_tolerance)
        self.retention_time_tolerance.valueChanged.connect(
            page_state.setRetentionTimeTolerance)

        self.mass = QDoubleSpinBox(decimals=6)
        self.mass.setRange(0, 100)
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
            "Isotope Formula"), self.isotope_formula)

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

        self.setLayout(self.screen_layout)
