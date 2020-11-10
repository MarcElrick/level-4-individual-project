from molmass import Formula, FormulaError
from assets.pathFinder import get_resource_path
from helper import mass2iso, parse_adduct_file

import os


class LipidDetailsScreenState:
    def __init__(self):
        self.lipid_formula = ""

        self.charge_mode = 'Positive'

        self.setAdductList('positive.csv')
        self.adduct_index = 0

        self.isotope_depth = 0

        self.retention_time = 0.0
        self.retention_time_tolerance = 0.0
        self.mass = 0.0
        self.mass_tolerance = 0.0

        self.mass_tolerance_units_index = 0
        self.mass_tolerance_units_list = ['ppm', 'Da']

    def get_data_string_summary(self):
        return {
            "Lipid Formula": self.lipid_formula,
            "Adduct": self.adduct_list[self.adduct_index],
            "Charge Mode": self.charge_mode,
            "Isotope Depth": self.isotope_depth,
            "Retention Time": str(self.retention_time) + "s",
            "Retention Time Tolerance": str(self.retention_time_tolerance) + "s",
            "Mass": self.mass,
            "Mass Tolerance": str(self.mass_tolerance) +
            self.mass_tolerance_units_list[self.mass_tolerance_units_index]
        }

    def get_data_summary(self):
        return {
            "formula": self.lipid_formula,
            "adduct": self.adduct_list[self.adduct_index],
            "chargeMode": self.charge_mode,
            "isotopeDepth": self.isotope_depth,
            "retentionTime": str(self.retention_time) + "s",
            "retentionTimeTolerance": str(self.retention_time_tolerance) + "s",
            "mass": self.mass,
            "massTolerance": str(self.mass_tolerance),
            "massToleranceUnits": self.mass_tolerance_units_list[self.mass_tolerance_units_index]
        }

    def setLipidFormula(self, text):
        self.lipid_formula = Formula(text).formula

    def setAdductIndex(self, value):
        self.adduct_index = value
        mass_multi = self.adduct_list[self.adduct_index][2]
        mass_add = self.adduct_list[self.adduct_index][1]
        try:
            mono_iso_mass = Formula(self.lipid_formula).mass
            self.setMass(mass2iso(
                mono_iso_mass, mass_multi, mass_add))
        except FormulaError:
            pass

    def setIsotopeDepth(self, value):
        self.isotope_depth = value

    def setRetentionTime(self, value):
        self.retention_time = value

    def setRetentionTimeTolerance(self, value):
        self.retention_time_tolerance = value

    def setMass(self, value):
        self.mass = value

    def setMassTolerance(self, value):
        self.mass_tolerance = value

    def setMassToleranceUnits(self, value):
        self.mass_tolerance_units_index = value

    def setChargeMode(self, value):
        self.charge_mode = value
        self.setAdductList(value.lower()+'.csv')
        self.setAdductIndex(0)

    def setAdductList(self, filename):
        self.adduct_list = parse_adduct_file(get_resource_path(
            os.sep.join(['assets', filename])))

    def getAdductLabels(self, adduct_list):
        return list(map(lambda x: x[0], adduct_list))
