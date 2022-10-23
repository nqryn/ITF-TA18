import unittest
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager


# Intrebari:
# D c nu trebuie definit browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class FirstTestcase(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get("https://the-internet.herokuapp.com/")
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        authentication_page = self.browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[21]/a")
        authentication_page.click()

    def tearDown(self) -> None:
        self.browser.quit()

    # Test 1 - Verifică dacă noul url e corect

    def test_authentication_page(self):
        url_page = self.browser.current_url
        url_authentication = "https://the-internet.herokuapp.com/login"
        print(url_authentication)
        time.sleep(5)
        self.assertEqual(url_page, url_authentication, "Incorrect URL")
        pass

    # Test 2 - Verifică dacă page title e corect

    def test_title(self):
        title_displayed = "The Internet"
        title_taken = self.browser.title
        print(title_taken)
        self.assertEqual(title_displayed, title_taken, "wrong title")
        pass

    # ''' Test 3 - Verifică textul de pe elementul xpath=//h2 e corect'''

    def test_text(self):
        text_displayed = "Login Page"
        text_taken = self.browser.find_element(by=By.XPATH, value='//*[@id="content"]/div/h2')
        assert text_displayed == text_taken.text, 'Text from element xpath=//h2 is incorrect'

    # ''' Test 4 - Verifică dacă butonul de login este displayed'''

    def test_buton_login(self):
        button_login_displayed = "Login"
        button_login_taken = self.browser.find_element(by=By.XPATH, value='//*[@id="login"]/button')
        # button_login_taken = self.browser.find_element(by=By.CSS_SELECTOR, login > button)
        self.assertTrue(button_login_taken is not None, 'Login button is not displayed')
        self.assertEqual(button_login_displayed, button_login_taken.text, 'Login button is not displayed')

    # '''  Test 5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect'''

    def test_elemental_selenium(self):
        elemental_selenium_link = "Elemental Selenium"
        elemental_selenium_taken = self.browser.find_element(By.LINK_TEXT, "Elemental Selenium")
        # elemental_selenium_taken2 = self.browser.find_element(By.LINK_TEXT,'http://elementalselenium.com/')
        assert elemental_selenium_link == elemental_selenium_taken.text, "Incorrect href for 'Elemental Selenium’"

    # ''' Test 6 Lasă goale user și pass - Click login - Verifică dacă eroarea e displayed'''
    class NoSuchElementException:
        pass

    def test_login_error(self):
        self.browser.find_element(by=By.XPATH, value='//*[@id="login"]/button').click()
        time.sleep(3)
        find_login_error = self.browser.find_element(By.ID, "flash")
        # print(find_login_error.id)
        # find_login_error = self.browser.find_element(by=By.XPATH, value='//*[@id="flash"]')
        time.sleep(3)
        self.assertTrue(find_login_error.is_displayed(), "Login error is not displayed")

        login_error_found = False
        try:
            self.browser.find_element(By.ID, "flash2")
            login_error_found = True
        except NoSuchElementException as e:
            print("Login error is displayed")
            self.assertTrue(login_error_found, "Invalid credentials not displayed.")


    # ''' Test 7 - Completează cu user și pass invalide - Click login
    #     - Verifică dacă mesajul de pe eroare e corect
    #     - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
    #     expected = 'Your username is invalid!'
    #     self.assertTrue(expected in actual, 'Error message text is incorrect')'''

    def test_invalid_login(self):
        self.browser.find_element(By.ID, "username").send_keys("Lidia")
        self.browser.find_element(By.ID, "password").send_keys("Parola")
        self.browser.find_element(by=By.XPATH, value='//*[@id="login"]/button').click()
        time.sleep(2)
        try:
            error_element = self.browser.find_element(By.ID, "flash")
            assert "Your username is invalid!" in error_element.text, "Login message is incorrect."
        except NoSuchElementException as e:
            self.assertFalse(True, "Login message does not exist.")