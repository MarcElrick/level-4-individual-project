from molmass import Formula
from data_processing.lipid_kinetics import *
from state.input_summary_screen_state import InputSummaryScreenState
import unittest
from state.file_picker_screen_state import FilePickerScreenState
from state.lipid_details_screen_state import LipidDetailsScreenState, IndividualLipid

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
        self.lipid_state.lipids = [IndividualLipid(0, 'positive')]
        self.myLipid = self.lipid_state.lipids[0]
        self.myLipid.setLipidFormula("C4356H4")
        self.myLipid.setAdductIndex(0)
        self.myLipid.setIsotopeDepth(5)
        self.myLipid.setMass(100.000)
        self.myLipid.setMassTolerance(20)
        self.myLipid.setMassToleranceUnits(0)
        self.myLipid.setRetentionTime(100.000)
        self.myLipid.setRetentionTimeTolerance(20)
        self.maxDiff = None

        self.assertDictEqual({'': {'formula': 'C4356H4', 'adduct': ['[M+H]+', 1.007276452, 1.0, ''], 'isotopeDepth': '5', 'retentionTime': '100.0s',
                                   'retentionTimeTolerance': '20s', 'mass': '100.0', 'massTolerance': '20', 'massToleranceUnits': 'ppm'}}, self.state.get_lipid_info()[0])

    def test_file_info_is_correct(self):
        self.file_picker_state.add_record(["zero.mzML", 0])
        self.file_picker_state.add_record(["one.mzML", 1])
        self.file_picker_state.add_record(["two.mzML", 2])
        self.file_picker_state.add_record(["three.mzML", 3])

        self.assertEqual(self.state.get_file_info(), [["zero.mzML", 0], [
                         "one.mzML", 1], ["two.mzML", 2], ["three.mzML", 3]])
