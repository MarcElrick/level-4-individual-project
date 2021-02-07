from molmass import Formula, FormulaError
from assets.pathFinder import get_resource_path
from helper import mass2ion, parse_adduct_file
import jsonpickle
import os


class LipidDetailsScreenState:
    def __init__(self):
        self.charge_mode = 'Positive'
        self.lipids = []
        self.setAdductList(self.charge_mode)

        self.lipids = [IndividualLipid(0, self.adduct_list)]
        self.setAdductList(self.charge_mode)
        self.keyCount = 1

    def setChargeMode(self, value):
        self.charge_mode = value
        self.setAdductList(value)

        for lipid in self.lipids:
            lipid.setAdductIndex(0)

    def add_lipid(self):
        self.lipids.append(IndividualLipid(
            self.keyCount, self.adduct_list))
        self.keyCount += 1

    def remove_lipid(self, key):
        for lipid in self.lipids:
            if(lipid.key == key):
                self.lipids.remove(lipid)

    def getAdductLabels(self, adduct_list):
        return list(map(lambda x: x[0], adduct_list))

    def setAdductList(self, filename):
        self.adduct_list = parse_adduct_file(get_resource_path(
            os.sep.join(['assets', filename.lower() + '.csv'])))

        for lipid in self.lipids:
            lipid.adduct_list = self.adduct_list

    def get_lipid_data(self):
        return list(map(lambda x: x.get_lipid_data(), self.lipids))

    def get_data_string_summary(self):
        return list(map(lambda x: x.get_data_string_summary(), self.lipids))

    def save_lipids(self, filename):
        if not os.path.exists('saved_runs'):
            os.makedirs('saved_runs')

        with open("saved_runs/{}.json".format(filename), 'w') as f:
            f.write(jsonpickle.encode(
                {'lipids': self.lipids, 'charge': self.charge_mode}))

    def restore_lipids(self, filename):
        if not os.path.exists('saved_runs'):
            os.makedirs('saved_runs')

        try:
            with open("saved_runs/{}".format(filename), 'r') as f:
                to_import = jsonpickle.decode(f.read())
                self.lipids = to_import['lipids']
                self.charge_mode = to_import['charge']
        except:
            raise Exception

    def validate_lipids(self):
        for lipid in self.lipids:
            if not lipid.isValid():
                return False
        return True


class IndividualLipid:
    def __init__(self, key, adduct_list):

        self.adduct_list = adduct_list
        self.valid = False

        self.lipid_formula = ""
        self.name = ""
        self.setAdductIndex(0)

        self.key = key
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
            self.name: {
                "formula": self.lipid_formula,
                "adduct": self.adduct_list[self.adduct_index],
                "isotopeDepth": str(self.isotope_depth),
                "retentionTime": str(self.retention_time) + "s",
                "retentionTimeTolerance": str(self.retention_time_tolerance) + "s",
                "mass": str(self.mass),
                "massTolerance": str(self.mass_tolerance),
                "massToleranceUnits":
                self.mass_tolerance_units_list[self.mass_tolerance_units_index]
            }
        }

    def get_lipid_data(self):
        return {
            self.name: {
                "formula": self.lipid_formula,
                "adduct": self.adduct_list[self.adduct_index],
                "isotopeDepth": self.isotope_depth,
                "retentionTime": self.retention_time,
                "retentionTimeTolerance": self.retention_time_tolerance,
                "mass": self.mass,
                "massTolerance": self.mass_tolerance,
                "massToleranceUnits":
                self.mass_tolerance_units_list[self.mass_tolerance_units_index]
            }
        }

    def setLipidFormula(self, text):
        self.lipid_formula = Formula(text).formula

    def setAdductIndex(self, value):
        self.adduct_index = value
        if value >= len(self.adduct_list):
            pass
        mass_multi = self.adduct_list[self.adduct_index][2]
        mass_add = self.adduct_list[self.adduct_index][1]
        try:
            mono_iso_mass = Formula(self.lipid_formula).mass
            self.setMass(mass2ion(
                mono_iso_mass, mass_multi, mass_add))
        except FormulaError:
            pass

    def setName(self, text):
        self.name = text

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

    def isValid(self):
        if self.isotope_depth <= 0:
            return False
        if self.lipid_formula == "":
            return False
        if self.retention_time <= 0:
            return False
        if self.mass_tolerance <= 0:
            return False
        return True
