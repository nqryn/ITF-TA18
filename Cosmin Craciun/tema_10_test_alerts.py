"""
Pentru a interactiona cu alert/confirm/prompt, avem nevoie de o sintaxa speciala:
   my_alert = self.browser.switch_to.alert
In felul acesta, mutam focusul pe ferestruica cu alert-ul.
Apoi, avem optiunea de a da accept (adica ok) sau dismiss (adica cancel).
"""

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.remote.webelement import WebElement
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

    """
    Tema pentru acasa:
    faceti metodele de confirm si prompt! => 4 metode
    De fiecare data, pasii sunt:
     - click pe butonul care deschide alert
     - click pe unul dintre butoanele din alert (la prompt punem si text)
     - verificare daca textul din result e cel asteptat
    """

    def test_confirm_ok(self):
        confirm_button = self.browser.find_element(*self.CONFIRM_BUTTON_SELECTOR)
        confirm_button.click()

        confirm_window = self.browser.switch_to.alert
        confirm_window.accept()

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You clicked: Ok"

    def test_confirm_cancel(self):
        confirm_button = self.browser.find_element(*self.CONFIRM_BUTTON_SELECTOR)
        confirm_button.click()

        confirm_window = self.browser.switch_to.alert
        confirm_window.dismiss()

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You clicked: Cancel"

    def test_prompt_ok(self):
        prompt_button = self.browser.find_element(*self.PROMPT_BUTTON_SELECTOR)
        prompt_button.click()

        prompt_window = self.browser.switch_to.alert
        prompt_window.send_keys("No you are not, and stop lying!")
        prompt_window.accept()
        time.sleep(1)

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You entered: No you are not, and stop lying!"

    def test_prompt_cancel(self):
        prompt_button = self.browser.find_element(*self.PROMPT_BUTTON_SELECTOR)
        prompt_button.click()

        prompt_window = self.browser.switch_to.alert
        prompt_window.dismiss()

        result = self.browser.find_element(*self.RESULT_SELECTOR)
        assert result.text == "You entered: null"
