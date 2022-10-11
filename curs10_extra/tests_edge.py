import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeTestCase(unittest.TestCase):
    BASE_URL = "https://the-internet.herokuapp.com/"

    def setUp(self) -> None:
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.browser = webdriver.Edge(service=service)
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_mic(self):
        a_b_testing_link = self.browser.find_element(By.LINK_TEXT, "A/B Testing")
        a_b_testing_link.click()
        self.assertEqual(self.browser.current_url, f"{self.BASE_URL}abtest")
