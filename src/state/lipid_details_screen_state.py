class LipidDetailsScreenState:
    def __init__(self):
        self.isotope_formula = ""

        self.adduct_list = ['Item1', 'Item2', 'Item3', 'Item4', 'Item5']
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
            "Isotope Formula": self.isotope_formula,
            "Adduct": self.adduct_list[self.adduct_index],
            "Retention Time": str(self.retention_time) + "s",
            "Retention Time Tolerance": str(self.retention_time_tolerance) + "s",
            "Mass": self.mass,
            "Mass Tolerance": str(self.mass_tolerance) + self.mass_tolerance_units_list[self.mass_tolerance_units_index]
        }

    def setIsotopeFormula(self, text):
        self.isotope_formula = text

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
