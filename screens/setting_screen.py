import random

from appium.webdriver.common.touch_action import TouchAction

from screens.base_screen import Screen
from selenium.webdriver.common.by import By


class SettingScreen(Screen):
    SETTINGS_BUTTON = (By.ID, "com.nulltree.roundbell:id/setting_button")
    TRAINING_BUTTON_RIGHT = (By.ID, "com.nulltree.roundbell:id/training_up")
    TRAINING_BUTTON_LEFT = (By.ID, "com.nulltree.roundbell:id/training_down")
    TRAINING_TIME_VALUE = (By.ID, "com.nulltree.roundbell:id/training_time")
    SOUND_SLIDER = (By.ID, "com.nulltree.roundbell:id/sb_volume")
    WIDGET = (By.CLASS_NAME, "android.widget.ScrollView")

    def open(self):
        assert self.get_element(*self.SETTINGS_BUTTON)
        self.click(*self.SETTINGS_BUTTON)

    def tab_right_button_training_time_option(self):
        self.click(*self.TRAINING_BUTTON_RIGHT)

    def tab_left_button_training_time_option(self):
        self.click(*self.TRAINING_BUTTON_LEFT)

    def get_training_time(self):
        training_time_value_text = self.get_element(*self.TRAINING_TIME_VALUE).text
        training_time_value_int = int(training_time_value_text.replace(":", ""))
        return training_time_value_int

    def training_time_should_be_increase_10_sec(self):
        training_time = self.get_training_time()
        assert training_time == 310

    def training_time_should_be_decrease_10_sec(self):
        training_time = self.get_training_time()
        assert training_time == 300

    def get_sound_value(self, sound_slider):
        return round(float(sound_slider.text))

    def scroll_up_screen(self):
        frame = self.get_element(*self.WIDGET)
        startx = frame.location.get('x') + (frame.size.get('width') / 2)
        starty = frame.location.get('y') + ((frame.size.get('height') / 2) - 5)
        endx = startx
        endy = starty - 200
        self.driver.swipe(startx, starty, endx, endy, 400)

    def move_slider_sound_settings(self):
        sound_slider = self.get_element(*self.SOUND_SLIDER)
        self.scroll_up_screen()
        start = sound_slider.location.get('x')
        end = sound_slider.size.get('width')
        y = sound_slider.location.get('y')
        actions = TouchAction(self.driver)
        # move slider to end
        actions.press(None, start, y).move_to(None, end, y).release().perform()

    def is_changed_sound_slider(self):
        sound_slider = self.get_element(*self.SOUND_SLIDER)
        assert self.get_sound_value(sound_slider) == 15
