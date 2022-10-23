import time
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


class TestsEdge(unittest.TestCase):


    def setUp(self) -> None:
        self.browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.browser.get("https://jules.app/sign-in/")
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_invalid_email(self):
        email = self.browser.find_element(By.XPATH, value="//input[@placeholder='Enter your email']")
        email.send_keys("invalidemail")
        invalid_email = self.browser.find_element(By.XPATH, value='//*[@id="root"]/div/div[2]/form/div/div[1]/div/p')
        self.assertTrue(invalid_email, "Error message not displayed")

    def test_login_failed(self):
        email = self.browser.find_element(By.XPATH, value="//input[@placeholder='Enter your email']")
        email.send_keys("validemail@gmail.com")
        password = self.browser.find_element(By.XPATH, value='//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input')
        password.send_keys("validpassword")
        login_button = self.browser.find_element(By.XPATH, value='//*[@id="root"]/div/div[2]/form/div/div[3]/button/span[1]')
        login_button.click()
        error_message = self.browser.find_element(By.XPATH, value='//*[@id="root"]/div/div[2]/form/div[1]')
        self.assertTrue(error_message.is_displayed(), "not present")

    def test_unhide_password(self):
        password = self.browser.find_element(By.XPATH, value='//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input')
        password.send_keys("validpassword")
        sleep(2)
        unhide_password_button= self.browser.find_element(By.CSS_SELECTOR, value='svg')
        unhide_password_button.click()
        sleep(2)







