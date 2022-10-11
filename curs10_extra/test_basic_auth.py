"""
Pentru a putea testa o pagina care are Basic Authentication, folosim o sintaxa speciala in URL:

https://USERNAME:PASSWORD@restul_urlului
Unde USERNAME si PASSWORD se inlocuiesc cu valorile necesare.

"""

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeTestCase(unittest.TestCase):
    BASE_URL = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
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

    def test_get_in(self):
        ok_text = self.browser.find_element(By.XPATH, "//p").text
        self.assertEqual(ok_text, "Congratulations! You must have the proper credentials.")
