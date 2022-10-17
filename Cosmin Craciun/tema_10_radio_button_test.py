import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class RadioButtonsTestCase(unittest.TestCase):
    BASE_URL = "https://formy-project.herokuapp.com/"

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.find_element(by=By.XPATH, value="/html/body/div/div/li[12]/a").click()
        self.radio_button_1 = self.browser.find_element(value="radio-button-1")
        self.radio_button_2 = self.browser.find_element(by=By.XPATH, value="//*[@value='option2']")
        self.radio_button_3 = self.browser.find_element(by=By.XPATH, value="//*[@value='option3']")

    def tearDown(self) -> None:
        self.browser.quit()

    def test_radio_button_1(self):
        self.radio_button_1.click()
        assert self.radio_button_1.is_selected()

    def test_radio_button_2(self):
        self.radio_button_2.click()
        time.sleep(2)
        assert self.radio_button_2.is_selected()

    def test_radio_button_3(self):
        self.radio_button_3.click()
        assert self.radio_button_3.is_selected()

    def test_buttons_2_3_not_selected(self):
        self.radio_button_1.click()
        self.assertFalse(self.radio_button_2.is_selected())
        self.assertFalse(self.radio_button_3.is_selected())

    def test_buttons_1_3_not_selected(self):
        self.radio_button_2.click()
        self.assertFalse(self.radio_button_1.is_selected())
        self.assertFalse(self.radio_button_3.is_selected())

    def test_buttons_1_2_not_selected(self):
        self.radio_button_3.click()
        self.assertFalse(self.radio_button_1.is_selected())
        self.assertFalse(self.radio_button_2.is_selected())
