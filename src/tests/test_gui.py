import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from gui.gui_controller import MainApp
from gui.lipid_details_screen import LipidDetailsScreen
from gui.file_picker_screen import FilePickerScreen
import sys


# Smoke test to verify test suite works
class SmokeTest(unittest.TestCase):

    def test_smoke(self):
        self.assertEqual('foo'.upper(), 'FOO')


class LipidDetailsScreenTests(unittest.TestCase):
    app = QApplication(sys.argv)
    form = MainApp()

    def test_app_initialises_at_lipid_details_screen(self):
        self.assertIs(type(self.form.centralWidget()), type(LipidDetailsScreen()))

    def test_next_button_opens_file_picker_screen(self):
        # Verify that we are on lipid_details_screen
        self.assertIs(type(self.form.centralWidget()), type(LipidDetailsScreen()))

        # Click next button
        QTest.mouseClick(self.form.centralWidget().nav_buttons.btn_next, Qt.LeftButton)

        # Verify that we are now on FilePickerScreen
        self.assertIs(type(self.form.centralWidget()), type(FilePickerScreen()))
if __name__ == '__main__':
    unittest.main()
