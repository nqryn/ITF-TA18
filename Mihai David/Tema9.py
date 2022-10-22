from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.common import NoSuchElementException

class Login(unittest.TestCase):
    # MAIN_URL = "https://the-internet.herokuapp.com/"
    # FORM_AUTHENTIFICATION_SELECTOR = (By.XPATH, "//a[@href=='/login']")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.get("https://the-internet.herokuapp.com/")
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        button_form = self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a')
        button_form.click()

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

    ''' def test_remove_banner(self):
        login_button = self.browser.find_element(By.XPATH, "//*[@id='login']/button")
        login_button.click()
        x_close_button = self.browser.find_element(By.CLASS_NAME, "close")
        x_close_button.click()
        time.sleep(2)
        flash_found = False
        try:
            self.browser.find_element(By.ID, "flash")
            flash_found = True
        except NoSuchElementException as e:
            print("Am reusit!")
            self.assertFalse(flash_found)'''

    def test_texte_label(self):
        lista = self.browser.find_elements(By.XPATH, '//label')
        self.assertEqual(lista[0].text, 'Username', 'Textul username-ului nu se potriveste')
        self.assertEqual(lista[1].text, 'Password', 'Textul parolei nu se potriveste')

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

    def test_brute_force(self):
        text_gasit = self.browser.find_element(By.CSS_SELECTOR, '#content > div > h4').text
        print(text_gasit)
        text_split = text_gasit.split(' ')
        for i in range(len(text_split)):
            self.browser.find_element(By.ID, 'username').send_keys('tomsmith')
            self.browser.find_element(By.ID, 'password').send_keys(f'{text_split[i]}')
            self.browser.find_element(By.XPATH, '//*[@id="login"]/button').click()
            if self.browser.current_url == 'https://the-internet.herokuapp.com/secure':
                print(f'Parola secreta este: {text_split[i]}')
                time.sleep(3)
                break
        else:
            print('Nu am reușit să găsesc parola')