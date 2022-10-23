"""
Implementati o clasa Login care sa mosteneasca unittest.TestCase

Gasiti elementele in partea de sus folosind ce selectors doriti voi

setUp()
Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication

tearDown()
Quit browser
"""
import time
from unittest import TestCase

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Login(TestCase):
    MAIN_URL = "https://the-internet.herokuapp.com/"
    # We can use tuples to find our elements easily in all tests
    FORM_AUTHENTICATION_SELECTOR = (By.XPATH, "//a[@href='/login']")
    LOGIN_BUTTON_SELECTOR = (By.XPATH, "//*[@id='login']/button")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.MAIN_URL)
        self.browser.maximize_window()
        # We put this here, because we want to wait for ANY element to be found at most 10 seconds
        # This ONLY needs to be done once! So it is best to put it here, in setUp
        self.browser.implicitly_wait(10)
        form_auth_link = self.browser.find_element(*self.FORM_AUTHENTICATION_SELECTOR)
        form_auth_link.click()

    def tearDown(self) -> None:
        self.browser.quit()

    """
    Test8
    Lasati goale user si pass
    Click login
    Apasa x la eroare
    Verifica ca eroarea a disparut
    """
    def test8(self):
        login_button = self.browser.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()
        x_close_button = self.browser.find_element(By.CLASS_NAME, "close")
        x_close_button.click()
        # Sleep for 2 seconds, so that the flash has time to disappear
        time.sleep(2)
        flash_found = False
        try:
            self.browser.find_element(By.ID, "flash")
            flash_found = True
        except NoSuchElementException as e:
            print("Am reusit!")
        # We use assertFalse because the flash div should no longer exist
        self.assertFalse(flash_found)
        """
        Alte modalitati de a vedea ca un element a disparut
        - cautam cu find elements (plural) si verificam ca am primit o lista goala
        - cautam parintele si verificam ca nu are copii de genul elementului cautat
        """

    """
    Test9
    Ia ca o lista toate //label
    Verifica textul ca textul de pe ele sa fie cel asteptat (Username si Password)
    Aici e ok sa avem 2 asserturi
    """
    """
    Test10
    Completeaza cu user si pass valide
    Click login
    Verifica ca noul url CONTINE /secure
    Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
    Verifica ca elementul cu clasa=’flash succes’ este displayed
    Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’
    """