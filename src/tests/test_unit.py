from molmass import Formula
from data_processing.lipid_kinetics import *
from state.input_summary_screen_state import InputSummaryScreenState
import unittest
from state.file_picker_screen_state import FilePickerScreenState
from state.lipid_details_screen_state import LipidDetailsScreenState, IndividualLipid
import os

# Smoke test to verify test suite runs


class SmokeTest(unittest.TestCase):

    def test_smoke(self):
        self.assertEqual('foo'.upper(), 'FOO')


class LipidDetailsScreenStateTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.state = LipidDetailsScreenState()
        cls.state.lipids = [IndividualLipid(
            0, [['[M+H]+', 1.007276452, 1.0, '']])]
        cls.myLipid = cls.state.lipids[0]
        cls.myLipid.setLipidFormula("C4356H4")
        cls.myLipid.setAdductIndex(0)
        cls.myLipid.setIsotopeDepth(5)
        cls.myLipid.setMass(100.000)
        cls.myLipid.setMassTolerance(20)
        cls.myLipid.setMassToleranceUnits(0)
        cls.myLipid.setRetentionTime(100.000)
        cls.myLipid.setRetentionTimeTolerance(20)

    def test_get_lipid_data(self):
        self.assertDictEqual({'': {'formula': 'C4356H4', 'adduct': ['[M+H]+', 1.007276452, 1.0, ''], 'isotopeDepth': 5,
                                   'retentionTime': 100.0, 'retentionTimeTolerance': 20, 'mass': 100.0, 'massTolerance': 20, 'massToleranceUnits': 'ppm'}}, self.state.get_lipid_data()[0])

    def test_get_data_string_summary_returns_correct(self):
        self.assertDictEqual({'': {'formula': 'C4356H4', 'adduct': ['[M+H]+', 1.007276452, 1.0, ''], 'isotopeDepth': '5', 'retentionTime': '100.0s',
                                   'retentionTimeTolerance': '20s', 'mass': '100.0', 'massTolerance': '20', 'massToleranceUnits': 'ppm'}}, self.state.get_data_string_summary()[0])

    def test_save_lipids_creates_file(self):
        self.state.save_lipids("test")
        assert(os.path.exists('saved_runs/test.json'))
        os.remove('saved_runs/test.json')

    def test_restore_lipids_restores_state(self):
        self.state.save_lipids("test")
        self.state.lipids = []
        assert(len(self.state.lipids) == 0)

        self.state.restore_lipids("test.json")
        assert(len(self.state.lipids) == 1)
        os.remove('saved_runs/test.json')


class FilePickerScreenStateTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.state = FilePickerScreenState()
        cls.files = cls.state.file_time_pairs

    def test_add_pair_to_empty_index(self):
        self.assertEqual(self.files, [])
        self.state.add_record()
        self.files[0].filepath = 'test.mzml'
        self.assertEqual(self.files[0].filepath, 'test.mzml')

    def test_remove_pair_removes_correct_pair(self):
        self.state.add_record()
        self.files[-1].filepath = "one.mzml"
        self.state.add_record()
        self.files[-1].filepath = "two.mzml"

        self.state.remove_record(0)
        self.assertEqual(self.files[0].filepath, 'two.mzml')


class InputSummaryScreenStateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lipid_state = LipidDetailsScreenState()
        cls.file_picker_state = FilePickerScreenState()
        cls.state = InputSummaryScreenState(
            get_lipid_info=cls.lipid_state.get_data_string_summary, get_file_info=cls.file_picker_state.get_data_string_summary)

    def test_lipid_info_is_correct(self):
        self.lipid_state.lipids = [IndividualLipid(
            0, [['[M+H]+', 1.007276452, 1.0, '']])]
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
        for i in range(4):
            self.file_picker_state.add_record()

        self.file_picker_state.file_time_pairs[0].filepath = "zero.mzML"
        self.file_picker_state.file_time_pairs[0].time = 0
        self.file_picker_state.file_time_pairs[1].filepath = "one.mzML"
        self.file_picker_state.file_time_pairs[1].time = 1
        self.file_picker_state.file_time_pairs[2].filepath = "two.mzML"
        self.file_picker_state.file_time_pairs[2].time = 2
        self.file_picker_state.file_time_pairs[3].filepath = "three.mzML"
        self.file_picker_state.file_time_pairs[3].time = 3

        self.assertEqual(self.state.get_file_info(), [["zero.mzML", 0], [
                         "one.mzML", 1], ["two.mzML", 2], ["three.mzML", 3]])
