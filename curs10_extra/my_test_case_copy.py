import time
from datetime import datetime
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get("https://jules.app/sign-in")
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    # Decorator folosit sa "sarim" peste test (acesta nu va fi executat)
    @unittest.skip
    def test_login_with_correct_email(self):
        email_input = self.browser.find_element(by=By.XPATH, value="//input[@type='text']")
        password_input = self.browser.find_element(by=By.XPATH, value="//input[@type='password']")
        login_button = self.browser.find_element(by=By.XPATH, value="//button[@data-test-id='login-button']")

        # va afisa False, butonul e disabled atunci cand campurile de parola si email nu sunt completate
        print(login_button.is_enabled())

        email_input.send_keys("adella.neacsu@gmail.com")
        # time.sleep(1)
        # email_input.send_keys(Keys.BACKSPACE)
        # time.sleep(1)
        # email_input.send_keys(Keys.BACKSPACE)
        # time.sleep(1)
        # email_input.send_keys(Keys.BACKSPACE)
        # time.sleep(1)
        password_input.send_keys("8-72Characters")
        # assert login_button.is_enabled()
        self.assertFalse(login_button.is_enabled(), "Mesaj de exceptie - optional")

    @unittest.skipIf(datetime.now().year == 2022, "Nu se ruleaza testul acesta in anul 2022")
    def test_forgot_password_link(self):
        forgot_pass_link = self.browser.find_element(by=By.XPATH, value='//a[@data-test-id="forgot-password-link"]')
        forgot_pass_link.click()
        self.assertEqual(self.browser.current_url, "https://jules.app/forgot-password")
