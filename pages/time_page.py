from time import sleep

from pages.base_page import Page
from selenium.webdriver.common.by import By


class TimePage(Page):
    START_BUTTON = (By.ID, "com.nulltree.roundbell:id/start_button")
    STOP_BUTTON = (By.ID, "com.nulltree.roundbell:id/stop_button")
    RESET_BUTTON = (By.ID, "com.nulltree.roundbell:id/reset_button")
    TIME_TEXT_FIELD = (By.ID, "com.nulltree.roundbell:id/time_textview")
    ROUND_LABEL = (By.ID, "com.nulltree.roundbell:id/round_textview")

    def open(self):
        assert self.get_element(*self.ROUND_LABEL)

    def tap_start(self):
        self.click(*self.START_BUTTON)
        sleep(3)

    def tap_stop(self):
        self.click(*self.STOP_BUTTON)

    def tap_reset(self):
        self.click(*self.RESET_BUTTON)

    def get_time(self):
        # get time as text and modify it to int(e.x. 03:00 to 300)
        time_text = self.get_element(*self.TIME_TEXT_FIELD).text
        time_int = int(time_text.replace(":", ""))
        return time_int

    def time_started(self):
        # time changed after Start click
        sleep(3)
        time = self.get_time()
        assert time < 300

    def time_stopped(self):
        # time no changed after Stop click
        time_1 = self.get_time()
        sleep(2)
        time_2 = self.get_time()
        assert time_1 == time_2
