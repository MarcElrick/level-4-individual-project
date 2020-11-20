import re
import numpy as np
from mass_spec_utils.data_import.mzml import MZMLFile
import os
from molmass import Formula
import unittest
from data_processing.file_creation import create_plot, create_xlsx_output, min_func
from data_processing.lipid_kinetics import (compute_lipid_kinetics,
                                            get_isotope_intensities, get_max_mass)


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
        cls.global_output = compute_lipid_kinetics(cls.lipid, [["0_pp_d20_pos_1.mzML", 0],
                                                               ["8_pp_d20_pos_1.mzML", 8],
                                                               ["48_pp_d20_pos_1.mzML", 48],
                                                               ["72_pp_d20_pos_1.mzML", 72],
                                                               ["96_pp_d20_.mzML", 96]])

    def test_compute_lipid_kinetics(self):
        os.chdir(self.test_files_folder)
        output = compute_lipid_kinetics(self.lipid, [["0_pp_d20_pos_1.mzML", 0],
                                                     ["8_pp_d20_pos_1.mzML", 8],
                                                     ["48_pp_d20_pos_1.mzML", 48],
                                                     ["72_pp_d20_pos_1.mzML", 72],
                                                     ["96_pp_d20_.mzML", 96]])
        self.assertEqual(output['kinetic_parameters'],
                         (0.03600730844758999, 0.625699723108793, 0.21129762105351985))
        self.assertEqual(np.shape(output['data_matrix']), (5, 6))

    def test_create_plot_creates_file(self):
        create_plot(
            self.lipid['label'], self.global_output, output_filename=os.getcwd() + os.sep + re.sub(r'[^\w]', ' ', self.lipid['label']).replace(' ', '_')+'.png')
        self.assertTrue(os.path.exists(os.getcwd() + os.sep +
                                       re.sub(r'[^\w]', ' ', self.lipid['label']).replace(' ', '_')+'.png'))

    def test_create_xlsx(self):
        create_xlsx_output(self.global_output, [self.lipid], [
            '0_pp_d20_pos_1.mzML', '8_pp_d20_pos_1.mzML', '48_pp_d20_pos_1.mzML', '72_pp_d20_pos_1.mzML', '96_pp_d20_.mzML'])
        self.assertTrue(os.path.exists(os.getcwd() + os.sep + 'test.xlsx'))

    def test_min_func(self):
        self.assertEqual(min_func([0.05000001, 0.61955977, 0.23437533], False, np.array(
            [0,  8, 48, 72, 96]), np.array([0.61955977, 0.53178616, 0.2799674, 0.23355281, 0.23437533])), 0.0017899450116450211)

    def test_get_isotope_intensities(self):
        os.chdir(self.test_files_folder)
        self.assertEqual(len(get_isotope_intensities(
            self.lipid, ["0_pp_d20_pos_1.mzML", 0])), 7)

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
