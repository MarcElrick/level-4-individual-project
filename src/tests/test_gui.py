import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from gui.gui_controller import MainApp
from gui.lipid_details_screen import LipidDetailsScreen
from gui.file_picker_screen import FilePickerScreen
from gui.input_summary_screen import InputSummaryScreen
from gui.progress_screen import ProgressScreen
from state.state_controller import StateController
import sys


# Smoke test to verify test suite runs
class SmokeTest(unittest.TestCase):

    def test_smoke(self):
        self.assertEqual('foo'.upper(), 'FOO')


class LipidDetailsScreenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
        cls.state = StateController()
        cls.form = MainApp(cls.state)

    def test_app_initialises_at_lipid_details_screen(self):
        self.assertIs(type(self.form.centralWidget()),
                      type(LipidDetailsScreen()))

    def test_next_button_opens_file_picker_screen(self):
        # Verify that we are on lipid_details_screen
        self.assertIs(type(self.form.centralWidget()),
                      type(LipidDetailsScreen()))

        # Click next button
        QTest.mouseClick(self.form.centralWidget(
        ).nav_buttons.btn_next, Qt.LeftButton)

        # Verify that we are now on FilePickerScreen
        self.assertIs(type(self.form.centralWidget()),
                      type(FilePickerScreen()))

    def test_back_button_is_disabled(self):

        # Verify that we are now on FilePickerScreen
        self.assertIs(self.form.centralWidget(
        ).nav_buttons.btn_back.isEnabled(), False)


class FilePickerScreenTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
        cls.state = StateController()
        cls.form = MainApp(cls.state)

    @classmethod
    def setUp(cls):
        cls.form.init_file_picker_screen()

    def test_next_button_opens_input_summary_screen(self):
        QTest.mouseClick(self.form.centralWidget(
        ).nav_buttons.btn_next, Qt.LeftButton)
        self.assertIs(type(self.form.centralWidget()),
                      type(InputSummaryScreen()))

    def test_back_button_opens_lipid_details_screen(self):
        QTest.mouseClick(self.form.centralWidget(
        ).nav_buttons.btn_back, Qt.LeftButton)
        self.assertIs(type(self.form.centralWidget()),
                      type(LipidDetailsScreen()))


class InputSummaryScreenTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
        cls.state = StateController()
        cls.form = MainApp(cls.state)

    @classmethod
    def setUp(cls):
        cls.form.init_input_summary_screen()

    def test_next_button_opens_progress_screen(self):
        QTest.mouseClick(self.form.centralWidget(
        ).nav_buttons.btn_next, Qt.LeftButton)
        self.assertIs(type(self.form.centralWidget()), type(ProgressScreen()))

    def test_back_button_opens_file_picker_screen(self):
        QTest.mouseClick(self.form.centralWidget(
        ).nav_buttons.btn_back, Qt.LeftButton)
        self.assertIs(type(self.form.centralWidget()),
                      type(FilePickerScreen()))


if __name__ == '__main__':
    unittest.main()
