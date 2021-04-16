from screens.time_screen import TimeScreen
from screens.setting_screen import SettingScreen


class Application:
    def __init__(self, driver):
        self.time_screen = TimeScreen(driver)
        self.settings_screen = SettingScreen(driver)
