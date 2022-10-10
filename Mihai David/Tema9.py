from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import unittest


class Login(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get("https://the-internet.herokuapp.com/")
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Form Authentication']").click()
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)

    def tearDown(self) -> None:
        time.sleep(2)
        self.browser.quit()

    def test_url(self):  # verificare url nou
        self.assertEqual(self.browser.current_url, "https://the-internet.herokuapp.com/login", 'Wrong URL')
        print("Testul a reusit ! Noul url este:", str(self.browser.current_url))

    def test_page_tittle(self):  # verificare titlul paginii
        self.assertEqual(self.browser.title, 'The Internet', 'Titlul paginii nu se potriveste')
        print("Titlul paginii este corect !")

    def test_text_Login_Page(self):  # verificare text
        self.assertEqual(self.browser.find_element(By.XPATH, "//h2").text, "Login Page", "Wrong text")
        print("Textul este corect")

    def test_login_button(self):  # verificare vizibilitate login button
        self.assertTrue(self.browser.find_element(By.XPATH, '//*[@id="login"]/button/i').is_displayed(),
                        "No Login Button!")
        print("Login Button is displayed")

    def test_atribut_link(self):  # verificare atribut
        atribut = self.browser.find_element(By.LINK_TEXT, 'Elemental Selenium')
        atribut = atribut.get_attribute('href')
        print(atribut)
        self.assertEqual(atribut, 'http://elementalselenium.com/', 'Linkurile difera')
        print("Atributul este corect")

    def test_error_empty_credentials(self):  # login fara username si passwrod
        self.browser.find_element(By.XPATH, "//*[@id='login']/button").click()
        self.assertTrue(self.browser.find_element(By.ID, "flash").is_displayed(), "You can login")
        print("Mesaj de eroare. Nu te poti loga fara username si password")

    def test_wrong_credentials(self):  # login cu username si parola gresita
        self.browser.find_element(By.ID, 'username').send_keys('username')
        self.browser.find_element(By.ID, 'password').send_keys('password')
        self.browser.find_element(By.XPATH, '//*[@id="login"]/button').click()

        expect_message = 'Your username is invalid!'
        self.assertTrue(expect_message in self.browser.find_element(By.ID, 'flash').text, 'You can login')
        print("Nu te poti loga cu username si parola incorecta")

    def test_remove_error_banner(self):
        self.browser.find_element(By.XPATH, '//*[@id="login"]/button').click()
        time.sleep(1)
        # banner = self.browser.find_element(By.CLASS_NAME, "close").click()
        # time.sleep(1)
        self.assertTrue(self.browser.find_element(By.CLASS_NAME, "close").click(), "Bannerul nu a disparut")
        print("Poti inchide bannerul de warning")

    def test_labels(self):
        labels = self.browser.find_element(By.XPATH, "//label")

    def test_user_password_valid(self):
        self.browser.find_element(By.ID, 'username').send_keys('tomsmith')
        self.browser.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.browser.find_element(By.XPATH, '//*[@id="login"]/button').click()

        self.assertTrue('/secure' in self.browser.current_url, 'URL not secured')
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, "flash")))

        login_succesful = self.browser.find_element(By.XPATH, '//*[@id="flash"]')
        self.assertTrue(login_succesful.is_displayed(), "Bannerul nu apare ")
        self.assertTrue('secure area!' in login_succesful.text, 'Bannerul nu contine secure area')
        print("Bannerul contine secure area")

    def test_logut(self):
        self.browser.find_element(By.ID, 'username').send_keys('tomsmith')
        self.browser.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.browser.find_element(By.XPATH, '//*[@id="login"]/button').click()
        self.browser.find_element(By.LINK_TEXT, 'Logout').click()
        self.assertEqual(self.browser.current_url, 'https://the-internet.herokuapp.com/login', "link gresit")
        print("Am ajuns pe pagina de login")
