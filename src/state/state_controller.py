# This file represents all state management utilities required by the application.
# This is a custom solution as most existing solutions (e.g. MVC etc) are far more complex than necessary.

from state.lipid_details_screen_state import LipidDetailsScreenState
from state.file_picker_screen_state import FilePickerScreenState


class StateController:
    def __init__(self):
        self.screen1 = LipidDetailsScreenState()
        self.screen2 = FilePickerScreenState()
        #self.screen3 = ScreenThreeState()
        #self.screen4 = ScreenFourState()
