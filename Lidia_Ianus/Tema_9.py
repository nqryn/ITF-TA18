import unittest
import time

import content as content
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#
# browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# initial_url = "https://the-internet.herokuapp.com/"
# browser.get(initial_url)
#
# browser.maximize_window()
#

# time.sleep(2)
#
#
#
# # ??? Erroare daca facem assert ==
# assert initial_url != browser.current_url, f'INVALID URL {initial_url} and found {second_url}'

class FirstTestcase(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get("https://the-internet.herokuapp.com/")
        self.browser.maximize_window()
        self.browser.implicitly_wait(3)
        a_page = self.browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[21]/a")
        a_page.click()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_authentification_page(self):
         second_url = self.browser.current_url
         print(second_url)
         pass

    def test_noul_url(self):
        url_initial = self.browser.current_url
        url_expected = "https://the-internet.herokuapp.com/"
        self.assertEqual(url_expected, url_initial, 'URL changed')
        time.sleep(3)
        pass

    def test_title(self):
        #title_displayed = "The Internet"
        title = self.browser.find_element(by=By.CSS_SELECTOR, value="head > title")
        print(title)
        # self.assertEqual(title_displayed, title, "wrong title")
        pass








