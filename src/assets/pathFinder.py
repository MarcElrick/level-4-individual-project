# Code found at this stack overflow answer: https://stackoverflow.com/questions/49791273/pyinstaller-program-that-reads-a-csv
import os
import sys


def get_resource_path(relative):
    application_path = os.path.abspath(".")
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    return os.path.join(application_path, relative)
