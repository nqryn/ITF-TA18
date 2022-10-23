import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCaseCurs9(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get("https://the-internet.herokuapp.com/")
        self.browser.find_element(By.CSS_SELECTOR, value="a[href='/login']").click()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    # Test 1- Verifică dacă noul url e corect
    def test_url_check(self):
        actual = self.browser.current_url
        expected = "https://the-internet.herokuapp.com/login"
        self.assertEqual(expected, actual, 'Url is incorrect')

    # Test 2 - Verifică dacă page title e corect
    def test_title_check(self):
        self.assertEqual("The Internet", self.browser.title, 'Wrong Title')

    # Test 3 - Verifică textul de pe elementul xpath=//h2 e corect
    def test_check_xpath(self):
        test_three = self.browser.find_element(By.XPATH, value="//h2").text
        self.assertEqual(test_three, "Login Page")

    # Test 4 - Verifică dacă butonul de login este displayed
    def test_login_button(self):
        login_button = self.browser.find_element(By.XPATH, value="(//i[@class='fa fa-2x fa-sign-in'])[1]")
        self.assertTrue(login_button.is_displayed(), 'No login button')

    # Test 5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect ### wanted to use a different method with .click but doesnt work cause it opens the link in new tab so then im stuck :D, is there a way to get it to open on the original tab?
    def test_elemental_selenium(self):
        elemental_selenium_button = self.browser.find_element(By.LINK_TEXT, value="Elemental Selenium").get_attribute(
            "href")
        self.assertEqual(elemental_selenium_button, "http://elementalselenium.com/")

    # Test 6 - Lasă goale user și pass - Click login - Verifică dacă eroarea e displayed
    def test_empty_credentials(self):
        login_button = self.browser.find_element(By.CSS_SELECTOR, value=".fa.fa-2x.fa-sign-in")
        login_button.click()
        error_button = self.browser.find_element(By.XPATH, value="(//div[@id='flash'])[1]")
        self.assertTrue(error_button.is_displayed(), "No error button")

    # Test 7  - Completează cu user și pass invalide - Click login- Verifică dacă mesajul de pe eroare e corect - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
    def test_invalid_credentials(self):
        username = self.browser.find_element(By.NAME, value="username")
        password = self.browser.find_element(By.NAME, value="password")
        username.send_keys("okay")
        password.send_keys("okay")
        self.browser.find_element(By.CSS_SELECTOR, value=".fa.fa-2x.fa-sign-in").click()
        error_message = self.browser.find_element(By.ID, value="flash").text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in error_message, 'Error message text is incorrect ')

    # Test 8 - Lasă goale user și pass - Click login - Apasă x la eroare - Verifică dacă eroarea a dispărut
    def test_empty_credentials_error(self):
        login_button = self.browser.find_element(By.CSS_SELECTOR, value=".fa.fa-2x.fa-sign-in").click()
        error_button = self.browser.find_element(By.XPATH, value="(//div[@id='flash'])[1]")
        x_button = self.browser.find_element(By.CLASS_NAME, value="close")
        self.assertTrue(error_button.is_displayed(), "No error button")

    # Test 9 - Ia ca o listă toate //label - Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password) - Aici e ok să avem 2 asserturi
    def test_label(self):
        username_tag = self.browser.find_element(By.XPATH, value="//label[normalize-space()='Username']").text
        password_tag = self.browser.find_element(By.XPATH, value="//label[normalize-space()='Password']").text
        self.assertEqual(username_tag, "Username")
        self.assertEqual(password_tag, "Password")

    # Test 10
    # - Completează cu user și pass valide
    # - Click login
    # - Verifică ca noul url CONTINE /secure
    # - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    # - Verifică dacă elementul cu clasa=’flash succes’ este displayed
    # - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def test_valid_credentials(self):
        username = self.browser.find_element(By.NAME, value="username")
        password = self.browser.find_element(By.NAME, value="password")
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        login_button = self.browser.find_element(By.CSS_SELECTOR, value=".fa.fa-2x.fa-sign-in").click()
        url_nou = self.browser.current_url
        self.assertTrue("/secure" in url_nou, "not in new url")
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "flash")))
        flash_success = self.browser.find_element(By.ID, value="flash")
        self.assertTrue(flash_success.is_displayed(), "You logged into a secure area!")
        self.assertTrue("secure area!" in flash_success.text, "not true")

    # Test 11 - - Completează cu user și pass valide
    # - Click login
    # - Click logout
    # - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    def test_verify_url(self):
        username = self.browser.find_element(By.NAME, value="username")
        password = self.browser.find_element(By.NAME, value="password")
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        login_button = self.browser.find_element(By.CSS_SELECTOR, value=".fa.fa-2x.fa-sign-in").click()
        # logout_button= self.browser.find_element(By.CLASS_NAME, value="button secondary radius").click() # why does this not work?
        logout_button = self.browser.find_element(By.XPATH, value="//a[@class='button secondary radius']").click()
        url_nou = self.browser.current_url
        self.assertEqual(url_nou, "https://the-internet.herokuapp.com/login", "not equal")

    # Test 12
    def test_twelve(self):
        possible_password = self.browser.find_element(By.XPATH, value="//h4[contains(text(),'This is where you can log into the secure area. En')]").text
        password_split = possible_password.split()
        for word in password_split:
            username = self.browser.find_element(By.NAME, value="username")
            username.send_keys('tomsmith')
            password = self.browser.find_element(By.NAME, value="password")
            password.send_keys(word)
            login_button = self.browser.find_element(By.XPATH, value="(//i[@class='fa fa-2x fa-sign-in'])[1]").click()
            login_successful = self.browser.find_element(By.ID, value="flash").get_attribute("class")
            if "success" in login_successful:
                print(f'parola este {word}')
                break
        else:
            print("nu am gasit parola")

# mistakes I made
# left username and username.send_keys outside of the for so it would imput all the passwords in the list but leave the username empty after firrst try
# struggled at last part with if and else if we could quickly review this part.
