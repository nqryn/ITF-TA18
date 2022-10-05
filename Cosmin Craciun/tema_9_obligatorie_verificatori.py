import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Internet_Hero(unittest.TestCase):


    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get("https://the-internet.herokuapp.com/")
        self.browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[21]/a").click()
        self.noul_url = self.browser.current_url
        self.browser.implicitly_wait(5)
        self.browser.maximize_window()



    def tearDown(self) -> None:
        self.browser.quit()


# ● Test 1
# Verifică dacă noul url e corect


    def test1_URL_check(self):
        self.assertEqual(self.noul_url, "https://the-internet.herokuapp.com/login",
                         "Error message: Noul URL nu este corect")



# ● Test 2
# - Verifică dacă page title e corect

    def test2_page_title(self):
        page_title = self.browser.title
        self.assertEqual(page_title, "The Internet", "Error message: page title nu este corect (display : none)")

# ● Test 3
# - Verifică textul de pe elementul xpath=//h2 e corect

    def test3_check_element(self):
        element = self.browser.find_element(by=By.XPATH, value="//h2").text
        self.assertEqual(element, "Login Page")

# ● Test 4
# - Verifică dacă butonul de login este displayed

    def test4_login_displayed(self):
        login_button = self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button/i").is_displayed()
        self.assertTrue(login_button, "Error message: button not displayed")


# ● Test 5
# - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test5_link_selenium(self):
        elem_selenium = self.browser.find_element(by=By.LINK_TEXT, value="Elemental Selenium").get_attribute("href")
        self.assertEqual(elem_selenium, "http://elementalselenium.com/")


# ● Test 6
# - Lasă goale user și pass
# - Click login
# - Verifică dacă eroarea e displayed

    def test6_check_error(self):
        self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button/i").click()
        error_message = self.browser.find_element(value="flash").is_displayed()
        self.assertTrue(error_message, "error message: the error is not displayed")


# ● Test 7
# - Completează cu user și pass invalide
# - Click login
# - Verifică dacă mesajul de pe eroare e corect
# - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
# expected = 'Your username is invalid!'
# self.assertTrue(expected in actual, 'Error message text is
# incorrect')

    def test7_incorrect_user_pass(self):

        username = self.browser.find_element(value="username")
        username.send_keys("cicea_bosu")
        password = self.browser.find_element(value="password")
        password.send_keys("cicea_bosu")
        self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button/i").click()
        actual = self.browser.find_element(value="flash").text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')


# ● Test 8
# - Lasă goale user și pass
# - Click login
# - Apasă x la eroare
# - Verifică dacă eroarea a dispărut

    def test_8_error_x_button(self):

        self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button/i").click()
        self.browser.find_element(by=By.CLASS_NAME, value="close").click()
        time.sleep(1)

        try:
            error_message = self.browser.find_element(by=By.XPATH, value="//*[@id='flash']").is_displayed()
            self.assertFalse(error_message, "error message: the error is displayed")
        except NoSuchElementException:
            print("The error is not displayed")


# ● Test 9
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi

    def test_9_label_check(self):

        # label_list = []
        label_list = self.browser.find_elements(by=By.XPATH, value="*//label")
        self.assertEqual(label_list[0].text, "Username")
        self.assertEqual(label_list[1].text, "Password")

# ● Test 10
# - Completează cu user și pass valide
# - Click login
# - Verifică ca noul url CONTINE /secure
# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def test_10_valid_login(self):
        username = self.browser.find_element(value="username")
        username.send_keys("tomsmith")
        password = self.browser.find_element(value="password")
        password.send_keys("SuperSecretPassword!")
        self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button/i").click()
        url_secure = self.browser.current_url
        self.assertIn("/secure", url_secure)
        wait = WebDriverWait(self.browser, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='flash']")))
        elem_wanted = self.browser.find_element(by=By.XPATH, value="//*[@id='flash']")
        self.assertTrue(elem_wanted.is_displayed())
        self.assertIn("secure area!", elem_wanted.text)

# ● Test 11
# - Completează cu user și pass valide
# - Click login
# - Click logout
# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_11_logout(self):
        username = self.browser.find_element(value="username")
        username.send_keys("tomsmith")
        password = self.browser.find_element(value="password")
        password.send_keys("SuperSecretPassword!")
        self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button/i").click()
        self.browser.find_element(by=By.XPATH, value="//*[@id='content']/div/a").click()
        self.assertEqual(self.browser.current_url, "https://the-internet.herokuapp.com/login")


# ● Test 12 - brute force password hacking
# - Completează user tomsmith
# - Găsește elementul //h4
# - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
# potențială parolă.
# - Folosește o structură iterativă prin care să introduci rând pe rând
# parolele și să apeși pe login.
# - La final testul trebuie să îmi printeze fie
# ‘Nu am reușit să găsesc parola’
# ‘Parola secretă este [parola]’

    def test_12_brute_force_password(self):

        potential_password = self.browser.find_element(by=By.XPATH, value="//h4").text.split()
        for parola in potential_password:
            username = self.browser.find_element(value="username")
            username.send_keys("tomsmith")
            password = self.browser.find_element(value="password")
            password.send_keys(parola)
            self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button/i").click()
            if self.browser.current_url == "https://the-internet.herokuapp.com/login":
                print("Nu am reusit sa gasesc parola")
                continue
            else:
                print(f"Parola secreta este {parola}")
                break







