import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class ShopTestCaseEdge(unittest.TestCase):
    def setUp(self) -> None:
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.browser = webdriver.Edge(service=service)
        self.browser.get("http://automationpractice.com/index.php")
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_url_corect(self):
        get_url = self.browser.current_url
        print("The current url is:" + str(get_url))
        self.assertEqual(self.browser.current_url, "http://automationpractice.com/index.php",
                         'The url is incorrect')

    def test_button_sign_in(self):
        self.browser.find_element(By.CLASS_NAME, 'login').click()
        get_url = self.browser.current_url
        self.assertEqual(get_url,
                         'http://automationpractice.com/index.php?controller=authentication&back=my-account')

    def test_sign_without_credentials(self):
        self.browser.find_element(By.CLASS_NAME, 'login').click()
        self.browser.find_element(By.CSS_SELECTOR, '#SubmitLogin > span > i').click()
        error_message = self.browser.find_element(By.XPATH, '//*[@id="center_column"]/div[1]/ol/li').text
        self.assertEqual(error_message, 'An email address required.', 'Error message does not match')

    def test_search_bar(self):
        self.browser.find_element(By.NAME, 'search_query').send_keys('long dress')
        self.browser.find_element(By.NAME, 'submit_search').click()
        result_search = self.browser.find_element(By.CSS_SELECTOR, '#center_column > h1 > span.lighter').text
        self.assertEqual(result_search, '"LONG DRESS"', 'Search does not match')