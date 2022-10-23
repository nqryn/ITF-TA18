import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



class JavaScripAlerts(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.browser.get("https://the-internet.herokuapp.com/")
        self.browser.find_element(By.LINK_TEXT, value="JavaScript Alerts").click()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        time.sleep(5)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_js_alert(self):
        js_alert= self.browser.find_element(By.XPATH, value="//button[normalize-space()='Click for JS Alert']")
        js_alert.click()
        alert_window= self.browser.switch_to.alert
        alert_window.accept()
        result_text = self.browser.find_element(By.XPATH, value="(//p[@id='result'])[1]")
        self.assertTrue(result_text.is_displayed(), 'false')

    def test_js_confirm_ok(self):
        confirm_ok = self.browser.find_element(By.XPATH, value="(//button[normalize-space()='Click for JS Confirm'])[1]")
        confirm_ok.click()
        confirm_window = self.browser.switch_to.alert
        confirm_window.accept()

    def test_js_confirm_cancel(self):
        confirm_cancel = self.browser.find_element(By.XPATH, value="(//button[normalize-space()='Click for JS Confirm'])[1]")
        confirm_cancel.click()
        confirm_window = self.browser.switch_to.alert
        confirm_window.dismiss()

    def test_js_prompt_ok(self):
        prompt_ok = self.browser.find_element(By.XPATH, value="(//button[normalize-space()='Click for JS Prompt'])[1]")
        prompt_ok.click()
        prompt_window = self.browser.switch_to.alert
        prompt_window.send_keys("Enter")
        prompt_window.accept()

    def test_js_prompt_cancel(self):
        prompt_cancel = self.browser.find_element(By.XPATH, value="(//button[normalize-space()='Click for JS Prompt'])[1]")
        prompt_cancel.click()
        time.sleep(5)
        prompt_window = self.browser.switch_to.alert
        prompt_window.dismiss()
        time.sleep(5)

