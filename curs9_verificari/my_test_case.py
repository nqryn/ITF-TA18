import time
import unittest

from selenium import webdriver
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

    def test_login_with_correct_email(self):
        email_input = self.browser.find_element(by=By.XPATH, value="//input[@type='text']")
        password_input = self.browser.find_element(by=By.XPATH, value="//input[@type='password']")
        login_button = self.browser.find_element(by=By.XPATH, value="//button[@data-test-id='login-button']")

        # va afisa False, butonul e disabled atunci cand campurile de parola si email nu sunt completate
        print(login_button.is_enabled())

        email_input.send_keys("adella.neacsu@gmail.com")
        password_input.send_keys("8-72Characters")
        # assert login_button.is_enabled()
        self.assertTrue(login_button.is_enabled(), "Mesaj de exceptie - optional")

        # In mod normal, avem un singur assert per test case, iar acel assert este fix ultima linie de cod
        login_button.click()

        # Deoarece contul nu e inca activat, trebuie sa apara modalul acela rosu cu activation error
        activation_error_msg = self.browser.find_element(by=By.XPATH, value="//*[text()='Activation Error!']")
        self.assertIsInstance(activation_error_msg, WebElement)

    def test_forgot_password_link(self):
        forgot_pass_link = self.browser.find_element(by=By.XPATH, value='//a[@data-test-id="forgot-password-link"]')
        forgot_pass_link.click()
        self.assertEqual(self.browser.current_url, "https://jules.app/forgot-password")
