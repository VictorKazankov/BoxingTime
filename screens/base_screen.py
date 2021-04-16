from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Screen:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, how, what):
        try:
            element = WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return element

    def click(self, how, what):
        el = self.get_element(how, what)
        el.click()

    def input(self, text, how, what):
        el = self.get_element(how, what)
        el.click()
        el.clear()
        el.send_keys()
