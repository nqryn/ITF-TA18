import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get("https://the-internet.herokuapp.com/")
        self.browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[21]/a").click()
        self.browser.maximize_window()
        self.browser.implicitly_wait(15)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_1(self):
        self.assertTrue(self.browser.current_url == "https://the-internet.herokuapp.com/login", "Link gresit")

    def test_2(self):
        assert self.browser.title == "The Internet", "Titlu eronat"

    def test_3(self):
        assert self.browser.find_element(by=By.XPATH, value="//h2").text == "Login Page", "text gresit "

    def test_4(self):
        assert self.browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/form/button").is_displayed()

    def test_5(self):
        self.browser.find_element(by=By.LINK_TEXT, value="Elemental Selenium").click()
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        self.assertEqual(self.browser.current_url, "http://elementalselenium.com/", "Linkul nu este corect")

    def test_6(self):
        self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button").click()
        assert self.browser.find_element(by=By.XPATH, value="//*[@id='flash']").is_displayed()
        self.browser.implicitly_wait(5)

    def test_7(self):
        self.browser.find_element(by=By.ID, value="username").send_keys("Lavinia")
        self.browser.find_element(by=By.ID, value="password").send_keys("parola")
        self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button").click()
        error = self.browser.find_element(by=By.XPATH, value="//*[@id='flash']").text
        expected = "Your username is invalid!"
        self.assertTrue(expected in error, "Error in message text is incorrect")
        self.browser.implicitly_wait(3)

    def test_8(self):
        self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button").click()
        self.browser.find_element(by=By.XPATH, value="//*[@id='flash']/a").click()
        time.sleep(2)
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "flash error")))
            not_found = False
        except:
            not_found = True

        assert not_found
        self.browser.implicitly_wait(5)

    def test_9(self):
        list_label = self.browser.find_elements(by=By.TAG_NAME, value="label")
        self.assertEqual(list_label[0].text, "Username", "Textul este incorect")
        self.assertEqual(list_label[1].text, "Password", "Textul este incorect")
        time.sleep(3)
        self.browser.implicitly_wait(5)

    def test_10(self):
        self.browser.find_element(by=By.ID, value="username").send_keys("tomsmith")
        self.browser.find_element(by=By.ID, value="password").send_keys("SuperSecretPassword!")
        self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button").click()
        self.assertTrue(self.browser.current_url.find('/secure'), "Not secure")
        time.sleep(3)
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, "flash")))
        text_logged_secure_area = self.browser.find_element(by=By.XPATH, value="//*[@id='flash']")
        text_logged_secure_area.is_displayed()
        self.assertTrue('secure area!' in text_logged_secure_area.text, "Mesajul nu contine acest text!")

    def test_11(self):
        self.browser.find_element(by=By.ID, value="username").send_keys("tomsmith")
        self.browser.find_element(by=By.ID, value="password").send_keys("SuperSecretPassword!")
        self.browser.find_element(by=By.XPATH, value="//*[@id='login']/button").click()
        self.browser.find_element(by=By.XPATH, value="//*[@id='content']/div/a").click()
        self.assertTrue(self.browser.current_url == "https://the-internet.herokuapp.com/login", "Link gresit")
        time.sleep(5)

