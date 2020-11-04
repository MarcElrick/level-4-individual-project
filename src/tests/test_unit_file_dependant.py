from data_processing.lipid_kinetics import *
import unittest
from molmass import Formula
import os
import sys


class LipidKineticsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_path = os.path.abspath(os.path.join('../../test_files'))
        if cls.test_path not in sys.path:
            sys.path.append(cls.test_path)

    def test_compute_lipid_kinetics(self):
        os.chdir('..')
        os.chdir('..')
        os.chdir('test_files')
        compute_lipid_kinetics({
            "formula": Formula("C4356H4"),
            "adduct": '[M+H]+',
            "isotopeDepth": 5,
            "retentionTime": 100.0,
            "retentionTimeTolerance": 10.0,
            "mass": 1000.0,
            "massTolerance": 20.0,
            "massToleranceUnits": 'ppm'
        }, [["0_pp_d20_pos_1.mzML", 0], [
            "8_pp_d20_pos_1.mzML", 8], ["24_pp_s3_pos_1.mzML", 24], ["48_pp_d20_pos_1.mzML", 48], ["72_pp_d20_pos_1.mzML", 72], [["96_pp_d20_pos_1.mzML", 96]]])

    def test_get_isotope_intensity(self):
        get_isotope_intensity({
            "formula": Formula("C42H82NO8P"),
            "adduct": '[M+H]+',
            "isotopeDepth": 5,
            "retentionTime": 10.47*60,
            "retentionTimeTolerance": 60,
            "mass": 760.5836,
            "massTolerance": 50.0,
            "massToleranceUnits": 'ppm'
        }, ["0_pp_d20_pos_1.mzML", 0])


if __name__ == '__main__':
    unittest.main()
