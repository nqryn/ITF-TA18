import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get("https://the-internet.herokuapp.com/")
        button_form = self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a')
        button_form.click()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_url_corect(self):
        get_url = self.browser.current_url
        print("The current url is:" + str(get_url))
        self.assertEqual(self.browser.current_url, "https://the-internet.herokuapp.com/login",
                         'Nu se potriveste url-ul')

    def test_title_page(self):
        self.assertEqual(self.browser.title, 'The Internet', 'Titlul paginii nu se potriveste')

    def test_button_login_displayed(self):
        button_login = self.browser.find_element(By.XPATH, '//*[@id="login"]/button/i')
        self.assertTrue(button_login.is_displayed(), 'Butonul de login nu apare')

    def test_loginare_fara_credentiale(self):
        buton_login = self.browser.find_element(By.XPATH, '//*[@id="login"]/button')
        buton_login.click()
        mesaj_eroare = self.browser.find_element(By.XPATH, '//*[@id="flash"]')
        self.assertTrue(mesaj_eroare.is_displayed(), 'Eroare deoarece nu apare mesajul cu atentionarea utilizatorului')

    @unittest.skip
    def test_login_credentiale_gresite(self):
        self.browser.find_element(By.ID, 'username').send_keys('ceva')
        self.browser.find_element(By.ID, 'password').send_keys('altceva')
        self.browser.find_element(By.XPATH, '//*[@id="login"]/button').click()

        expect_message = 'Your username is invalid!'
        self.assertTrue(expect_message in self.browser.find_element(By.ID, 'flash').text, 'Nu exista mesajul de eroare')

    def test_user_pass_valid(self):
        self.browser.find_element(By.ID, 'username').send_keys('tomsmith')
        self.browser.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.browser.find_element(By.XPATH, '//*[@id="login"]/button').click()
        self.assertTrue('/secure' in self.browser.current_url, 'Url-un nu este securizat')
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "flash")))
        mesaj_succes = self.browser.find_element(By.XPATH, '//*[@id="flash"]')
        self.assertTrue(mesaj_succes.is_displayed(), 'Mesajul de logare cu succes nu apare')
        self.assertTrue('secure area!' in mesaj_succes.text, 'Mesajul de succes nu contine secure area!')

    def test_usercorect_logut(self):
        self.browser.find_element(By.ID, 'username').send_keys('tomsmith')
        self.browser.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.browser.find_element(By.XPATH, '//*[@id="login"]/button').click()
        self.browser.find_element(By.LINK_TEXT, 'Logout').click()
        self.assertEqual(self.browser.current_url, 'https://the-internet.herokuapp.com/login', 'Nu am ajuns la pagina '
                                                                                               'dorita')
