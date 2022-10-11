from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import unittest


class SignInTest(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.chrome.get("https://jules.app/sign-in")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_corect_page_name(self) -> None:
        self.assertEqual(self.chrome.title, "Jules", "Incorrect page title")

    def test_logo_displayed(self) -> None:
        self.assertTrue(self.chrome.find_element(by=By.XPATH, value="//img[@alt='Jules']").is_displayed(),
                        "Logo not displayed!")
