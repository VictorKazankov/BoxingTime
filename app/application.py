from pages.time_page import TimePage
from pages.setting_page import SettingPage


class Application:
    def __init__(self, driver):
        self.time_page = TimePage(driver)
        self.settings_page = SettingPage(driver)
