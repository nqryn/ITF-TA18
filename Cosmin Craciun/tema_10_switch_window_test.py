import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# class RadioButtonsTestCase(unittest.TestCase):
#     BASE_URL = "https://formy-project.herokuapp.com/"
#
#     def setUp(self) -> None:
#         self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#         self.browser.get(self.BASE_URL)
#         self.browser.maximize_window()
#         self.browser.implicitly_wait(10)
#         self.browser.find_element(by=By.XPATH, value="/html/body/div/div/li[13]/a").click()
#
#     def tearDown(self) -> None:
#         self.browser.quit()
#
#     def test_check_if_correct_window(self):
#         switch_window = self.browser.find_element(by=By.XPATH, value="/html/body/div/h1").text
#         self.assertTrue(switch_window, "Switch Window")
#
#     def test_open_new_tab(self):
#         self.browser.find_element(value="new-tab-button").click()
#         new_url = self.browser.current_url
#         self.assertTrue(new_url, "https://formy-project.herokuapp.com/")
#
#     def test_alert_button(self):
#         alert_button = self.browser.find_element(value="alert-button")
#         alert_button.click()
#         alert_message = self.browser.switch_to.alert
#         alert_message.accept()
#         assert alert_button.is_enabled()

    # cum pot verifica daca eroarea mai este activa sau nu? am incercat sa verific daca butoanele sunt enable
    # am incercat sa gasesc eroarea dupa text dar nu o gaseste. XPATH nu are sau nu stiu sa il gasesc.

