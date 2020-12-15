from state.lipid_details_screen_state import LipidDetailsScreenState
from state.file_picker_screen_state import FilePickerScreenState
from state.input_summary_screen_state import InputSummaryScreenState
from state.progress_screen_state import ProgressScreenState


class StateController:
    def __init__(self):
        self.screen1 = LipidDetailsScreenState()
        self.screen2 = FilePickerScreenState()
        self.screen3 = InputSummaryScreenState(
            self.screen1.get_data_string_summary,
            self.screen2.get_data_string_summary)
        self.screen4 = ProgressScreenState(
            self.screen1.get_lipid_data, self.screen2.get_data_string_summary)

    def wipe_state(self):
        self.__init__()
