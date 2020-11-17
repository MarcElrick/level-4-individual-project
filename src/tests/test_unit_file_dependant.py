from data_processing.lipid_kinetics import compute_lipid_kinetics, get_isotope_intensities, get_max_mass
from data_processing.file_creation import create_plot
import unittest
from molmass import Formula
import os
from mass_spec_utils.data_import.mzml import MZMLFile
import re


class LipidKineticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lipid = {
            "label": 'PC 34:1',
            "formula": Formula("C42H82NO8P"),
            "adduct": '[M+H]+',
            "isotopeDepth": 6,
            "retentionTime": 10.47*60,
            "retentionTimeTolerance": 60,
            "mass": 760.5836,
            "massTolerance": 50.0,
            "massToleranceUnits": 'ppm'
        }
        cls.test_folder = (os.getcwd())
        os.chdir('..')
        os.chdir('..')
        os.chdir('test_files_reduced')
        cls.test_files_folder = os.getcwd()

    def test_compute_lipid_kinetics(self):
        os.chdir(self.test_files_folder)
        output = compute_lipid_kinetics(self.lipid, [["0_pp_d20_pos_1.mzML", 0], [
            "8_pp_d20_pos_1.mzML", 8], ["48_pp_d20_pos_1.mzML", 48], ["72_pp_d20_pos_1.mzML", 72], ["96_pp_d20_.mzML", 96]])

        create_plot(
            self.lipid['label'], output, output_filename=os.getcwd() + os.sep + re.sub(r'[^\w]', ' ', self.lipid['label']).replace(' ', '_')+'.png')

    def test_get_isotope_intensities(self):
        os.chdir(self.test_files_folder)
        get_isotope_intensities(self.lipid, ["0_pp_d20_pos_1.mzML", 0])
        print

    def test_get_max_mass(self):
        os.chdir(self.test_files_folder)
        test_file = MZMLFile("0_pp_d20_pos_1.mzML")
        (max_i, max_mz) = get_max_mass(
            test_file.scans[0], 0, 1000)

        # These values were manually read for this specific scan via TOPPView
        self.assertEqual(max_i, 28188312.0)
        self.assertAlmostEqual(max_mz, 703.57514030)


if __name__ == '__main__':
    unittest.main()
