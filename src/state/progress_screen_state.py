from data_processing.lipid_kinetics import LipidKinetics
from data_processing.file_creation import create_xlsx_output
from threading import Thread


class ProgressScreenState():
    def __init__(self, get_lipid_data, get_file_data):
        self.get_lipid_data = get_lipid_data
        self.get_file_data = get_file_data

        self.progress_percentage = 0
        self.incrementSize = 1
        self.progress_message = ""
        self.incrementProgressBar = None

        self.t = Thread(target=self.performAnalysis)

    def setProgressIncrementFunction(self, fn):
        self.incrementProgressBar = fn

    def setIncrementSize(self, value):
        self.incrementSize = value

    def startAnalysis(self):
        self.t.start()

    def performAnalysis(self):
        kinetics_obj = LipidKinetics(self.incrementProgress)
        output_list = kinetics_obj.compute_lipid_kinetics(
            self.get_lipid_data(), self.get_file_data())
        create_xlsx_output(output_list, self.get_lipid_data(),
                           list(filter(lambda x: x[0], self.get_file_data())))
        self.incrementProgressBar(100)

    def incrementProgress(self):
        self.progress_percentage += self.incrementSize
        self.incrementProgressBar(self.progress_percentage)
