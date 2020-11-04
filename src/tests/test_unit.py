import unittest
from state.file_picker_screen_state import FilePickerScreenState
from state.lipid_details_screen_state import LipidDetailsScreenState
from state.input_summary_screen_state import InputSummaryScreenState
from data_processing.lipid_kinetics import *
from molmass import Formula

# Smoke test to verify test suite runs


class SmokeTest(unittest.TestCase):

    def test_smoke(self):
        self.assertEqual('foo'.upper(), 'FOO')


class FilePickerScreenStateTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.state = FilePickerScreenState()
        cls.files = cls.state.file_time_pairs

    def test_update_record_exists(self):
        self.state.add_record(['test.mzml', 8])
        self.state.update_record(['another.mzml', 8], 0)
        self.assertEqual(self.files[0], ['another.mzml', 8])

    def test_add_pair_to_empty_index(self):
        self.assertEqual(self.files, [])
        self.state.add_record(['test.mzml'])
        self.assertEqual(self.files[0], ['test.mzml'])

    def test_remove_pair_removes_correct_pair(self):
        self.state.add_record(['test8.mzml', 8, 0])
        self.state.add_record(['test16.mzml', 16, 0])
        self.state.remove_record(0)
        self.assertEqual(self.files, [['test16.mzml', 16, 0]])


class InputSummaryScreenStateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lipid_state = LipidDetailsScreenState()
        cls.file_picker_state = FilePickerScreenState()
        cls.state = InputSummaryScreenState(
            get_lipid_info=cls.lipid_state.get_data_string_summary, get_file_info=cls.file_picker_state.get_data_string_summary)

    def test_lipid_info_is_correct(self):
        self.lipid_state.setLipidFormula("C4356H4")
        self.lipid_state.setAdductIndex(0)
        self.lipid_state.setIsotopeDepth(5)
        self.lipid_state.setMass(100.000)
        self.lipid_state.setMassTolerance(20)
        self.lipid_state.setMassToleranceUnits(0)
        self.lipid_state.setRetentionTime(100.000)
        self.lipid_state.setRetentionTimeTolerance(20)

        self.assertDictEqual({"Lipid Formula": Formula("C4356H4").formula, "Isotope Depth": 5,
                              "Adduct": "[M+H]+", "Mass": 100.0, "Mass Tolerance": "20ppm",
                              "Retention Time": "100.0s",
                              "Retention Time Tolerance": "20s"}, self.state.get_lipid_info())

    def test_file_info_is_correct(self):
        self.file_picker_state.add_record(["zero.mzML", 0])
        self.file_picker_state.add_record(["one.mzML", 1])
        self.file_picker_state.add_record(["two.mzML", 2])
        self.file_picker_state.add_record(["three.mzML", 3])

        self.assertEqual(self.state.get_file_info(), [["zero.mzML", 0], [
                         "one.mzML", 1], ["two.mzML", 2], ["three.mzML", 3]])


class LipidKineticsTests(unittest.TestCase):
    def test_compute_lipid_kinetics(self):
        compute_lipid_kinetics({
            "formula": Formula("C4356H4"),
            "adduct": '[M+H]+',
            "isotopeDepth": 5,
            "retentionTime": 100.0,
            "retentionTimeTolerance": 10.0,
            "mass": 1000.0,
            "massTolerance": 20.0,
            "massToleranceUnits": 'ppm'
        }, [["zero.mzML", 0], [
            "one.mzML", 1], ["two.mzML", 2], ["three.mzML", 3]])

    def test_get_isotope_intensity(self):
        filepath = 'C:\\Users\\marce\\PycharmProjects\\test_files\\'
        get_isotope_intensity({
            "formula": Formula("C42H82NO8P"),
            "adduct": '[M+H]+',
            "isotopeDepth": 5,
            "retentionTime": 10.47*60,
            "retentionTimeTolerance": 60,
            "mass": 760.5836,
            "massTolerance": 50.0,
            "massToleranceUnits": 'ppm'
        }, [filepath + "0_pp_d20_pos_1.mzML", 0])


if __name__ == '__main__':
    unittest.main()
