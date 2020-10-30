from molmass import Formula


class LipidDetailsScreenState:
    def __init__(self):
        self.lipid_formula = ""

        self.adduct_list = ['[M+H]+', '[M+H]+', '[M+H]+', '[M+H]+', '[M+H]+']
        self.adduct_index = 0

        self.isotope_depth = 0

        self.retention_time = 0.0
        self.retention_time_tolerance = 0.0

        self.mass = 0.0
        self.mass_tolerance = 0.0

        self.mass_tolerance_units_index = 0
        self.mass_tolerance_units_list = ['ppm', 'Da']

    def get_data_summary(self):
        return {
            "Lipid Formula": self.lipid_formula,
            "Adduct": self.adduct_list[self.adduct_index],
            "Isotope Depth": self.isotope_depth,
            "Retention Time": str(self.retention_time) + "s",
            "Retention Time Tolerance": str(self.retention_time_tolerance) + "s",
            "Mass": self.mass,
            "Mass Tolerance": str(self.mass_tolerance) + self.mass_tolerance_units_list[self.mass_tolerance_units_index]
        }

    def setLipidFormula(self, text):
        self.lipid_formula = Formula(text).formula

    def setAdductIndex(self, text):
        self.adduct_index = text

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
