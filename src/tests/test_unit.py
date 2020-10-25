import unittest
from state.file_picker_screen_state import FilePickerScreenState
from state.lipid_details_screen_state import LipidDetailsScreenState


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

    def test_remove_pair_exists(self):
        self.state.add_record(['test.mzml', 8, 0])
        self.state.remove_record(0)
        self.assertEqual(self.files, [])


if __name__ == '__main__':
    unittest.main()
