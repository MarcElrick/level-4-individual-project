# This file represents all state management utilities required by the application.
# This is a custom solution as most existing solutions (e.g. MVC etc) are far more complex than necessary.

from state.lipid_details_screen_state import ScreenOneState


class StateController:
    def __init__(self):
        self.screen1 = ScreenOneState()
        #self.screen2 = ScreenTwoState()
        #self.screen3 = ScreenThreeState()
        #self.screen4 = ScreenFourState()
