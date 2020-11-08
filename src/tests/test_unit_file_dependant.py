from data_processing.lipid_kinetics import *
import unittest
from molmass import Formula
import os
import sys
import re


class LipidKineticsTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.lipid = {
            "label": 'PC 34:1',
            "formula": Formula("C42H82NO8P"),
            "adduct": '[M+H]+',
            "isotopeDepth": 5,
            "retentionTime": 10.47*60,
            "retentionTimeTolerance": 60,
            "mass": 760.5836,
            "massTolerance": 50.0,
            "massToleranceUnits": 'ppm'
        }
        os.chdir('..')
        os.chdir('..')

    def test_compute_lipid_kinetics(self):

        os.chdir('test_files_reduced')
        output = compute_lipid_kinetics(self.lipid, [["0_pp_d20_pos_1.mzML", 0], [
            "8_pp_d20_pos_1.mzML", 8], ["24_pp_s3_pos_1.mzML", 24], ["48_pp_d20_pos_1.mzML", 48], ["72_pp_d20_pos_1.mzML", 72], ["96_pp_d20_.mzML", 96]])
        os.chdir('..')
        os.chdir('level-4-individual-project')
        os.chdir('src')
        os.chdir('tests')
        create_plot(
            self.lipid['label'], output, output_filename=os.getcwd() + os.sep + re.sub(r'[^\w]', ' ', self.lipid['label']).replace(' ', '_')+'.png')

    def test_get_isotope_intensity(self):
        os.chdir('..')
        os.chdir('test_files_reduced')

        get_isotope_intensity(self.lipid, ["0_pp_d20_pos_1.mzML", 0])


if __name__ == '__main__':
    unittest.main()
