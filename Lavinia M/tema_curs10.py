import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeTestCase(unittest.TestCase):
    BASE_URL = "https://the-internet.herokuapp.com/javascript_alerts"
    ALERT_BUTTON_SELECTOR = (By.XPATH, "//ul/li[1]/button")
    CONFIRM_BUTTON_SELECTOR = (By.XPATH, "//ul/li[2]/button")
    PROMPT_BUTTON_SELECTOR = (By.XPATH, "//ul/li[3]/button")
    RESULT_SELECTOR = (By.ID, "result")

    def setUp(self) -> None:
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.browser = webdriver.Edge(service=service)
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_simple_alert(self):
        alert_button = self.browser.find_element(*self.ALERT_BUTTON_SELECTOR)
        alert_button.click()

        alert_window = self.browser.switch_to.alert
        alert_window.accept()
        time.sleep(1)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You successfully clicked an alert"

    def test_confirm_ok(self):
        confirm_button = self.browser.find_element(*self.CONFIRM_BUTTON_SELECTOR)
        confirm_button.click()

        confirm_window = self.browser.switch_to.alert
        confirm_window.accept()
        time.sleep(2)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You clicked: Ok"

    def test_confirm_cancel(self):
        confirm_button = self.browser.find_element(*self.CONFIRM_BUTTON_SELECTOR)
        confirm_button.click()

        confirm_window = self.browser.switch_to.alert
        confirm_window.dismiss()
        time.sleep(2)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You clicked: Cancel"

    def test_prompt_ok(self):
        prompt_button = self.browser.find_element(*self.PROMPT_BUTTON_SELECTOR)
        prompt_button.click()

        prompt_window = self.browser.switch_to.alert
        prompt_window.send_keys("Salut! Bine ai venit pe pagina noastra!")
        prompt_window.accept()
        time.sleep(2)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You entered: Salut! Bine ai venit pe pagina noastra!"

    def test_prompt_cancel(self):
        prompt_button = self.browser.find_element(*self.PROMPT_BUTTON_SELECTOR)
        prompt_button.click()

        prompt_window = self.browser.switch_to.alert
        prompt_window.dismiss()
        time.sleep(2)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You entered: null"
